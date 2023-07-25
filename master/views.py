from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from .serializers import *


#-------------Authentication-------------------
class UserRegistrationAPIView(APIView):
    def post(self,request):
        username    = request.data.get('username')
        password    = request.data.get('password')
        email       = request.data.get('email')
        mobile      = request.data.get('mobile')
        first_name  = request.data.get('first_name','')
        last_name   = request.data.get('last_name','')

        if not (username and password and email and mobile):
            return Response({'error': 'Missing required fields'}, status=400)

        try:
            existing_user = User.objects.filter(Q(username=username) | Q(email=email) | Q(mobile=mobile)).last()
            if existing_user:
                error_message = ''
                if existing_user.username == username:
                    error_message += r'Username already exists. '
                if existing_user.email == email:
                    error_message += r'Email already exists. '
                if existing_user.mobile == mobile:
                    error_message += 'Mobile number already exists. '
                return Response({'error': error_message}, status=400)
        except User.DoesNotExist:
            pass

        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password, mobile=mobile,
                    first_name=first_name, last_name=last_name)
        user.save()
        return Response({'success': 'User registered successfully','Is_Success':True}, status=201)

class Login(APIView):

    def post(self,request):
        get_user    = request.data.get("username")
        password    = request.data.get('password')

        cond = Q(username=get_user) | Q(email=get_user) | Q(mobile=get_user)
        username = User.objects.filter(cond).last()
        
        if not username:
            data = {'User': False, 'msg': 'Invalid Username'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                Token.objects.create(user=user)
            except:
                token = Token.objects.get(user=user)
            
            data = {
                'user': True,
                'token': str(token)
            }
            return Response(data, status=status.HTTP_200_OK)
        
        else:
            data = {'User': False, 'msg': 'Invalid password'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        token = Token.objects.get(user = request.user)
        token.delete()
        data = {'status':'You Are Successfully Logout'}
        return Response(data, status=status.HTTP_200_OK)


#---------------Trip----------------------
class TripAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        foo = Trip.objects.all()
        serializer = TripSerializer(foo, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        try:
            serializer = AddUpdateTripSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Trip is Sucessfully Created','is_success':True})
            errors = serializer.errors
            errors['IsSuccess'] = 'False'
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)})
        
    def put(self,request):
        try:
            id = self.request.query_params.get('id')
            foo = Trip.objects.get(id=id)
            serializer = AddUpdateTripSerializer(foo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Trip is Updated Sucessfully','is_success':True})
            errors = serializer.errors
            errors['IsSuccess'] = 'False'
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)})
    
    def delete(self,request):
        try:
            id = self.request.query_params.get('id')
            foo = Trip.objects.get(id=id)
            foo.delete()
            return Response({'msg': 'Trip Deleted successfully','is_success':True})
        except Exception as e:
            return Response({'error': str(e)})

#----------------Expense------------------
class ExpenseAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        obj = Expense.objects.filter(pay_user=request.user)
        serializer = ExpenseSerializer(obj,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AddUpdateExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(pay_user=request.user)
            return Response({'msg':'Expense Added Sucessfully','is_success':True})
        errors = serializer.errors
        errors['IsSuccess'] = 'False'
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
    
class UserPriceDistributed(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        obj = Expense.objects.filter(user_distributed = request.user)
        serializer = ExpenseSerializer(obj,many=True)
        return Response(serializer.data)
    


from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','mobile','profile']

class AddUpdateTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
        model = Trip
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    pay_user = UserSerializer(read_only=True)
    user_distributed = UserSerializer(many=True)
    trip = TripSerializer(read_only=True)
    class Meta:
        model = Expense
        fields = '__all__'
    
class AddUpdateExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ['pay_user']

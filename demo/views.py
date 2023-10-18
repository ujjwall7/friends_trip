from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class FAQHomeAPI(APIView):
    def get(self,request):
        obj = FAQ.objects.all().order_by('-id')[:4]
        serializer = FAQSerializer(obj, many=True)
        return Response(serializer.data)

class ShopByCategoryAPI(APIView):
    def get(self,request):
        obj = ShopByCategory.objects.all().last()
        serializer = ShopByCategorySerializer(obj, many=False)
        return Response(serializer.data)

class QualityMattersHomeAPI(APIView):
    def get(self,request):
        obj = QualityMatters.objects.filter(quality_choice='HomePage').last()
        serializer = QualityMattersHomeSerializer(obj, many=False)
        return Response(serializer.data)

class QualityMattersCardsAPI(APIView):
    def get(self,request):
        obj = QualityMattersCards.objects.all().order_by('-id')[:4]
        serializer = QualityMattersCardsSerializer(obj, many=True)
        return Response(serializer.data)

class OneStopShopAPI(APIView):
    def get(self,request):
        obj = OneStopShop.objects.all().last()
        serializer = OneStopShopSerializer(obj, many=False)
        return Response(serializer.data)

class TestmonialsAPI(APIView):
    def get(self,request):
        obj = Testmonials.objects.all().order_by('-id')
        serializer = TestmonialsSerializer(obj, many=True)
        return Response(serializer.data)

class FAQCategoryAPI(APIView):
    def get(self,request):
        obj = FAQCategory.objects.all().order_by('-id')
        serializer = FAQCategorySerializer(obj, many=True)
        return Response(serializer.data)

class FAQAPI(APIView):
    def get(self,request):
        faq_slug = self.request.query_params.get('faq_category')
        obj2        = FAQDetail.objects.all().last()
        serializer_detail  = FAQDetailSerializer(obj2, many=False)
        if faq_slug:
            try:
                get_obj = FAQ.objects.filter(category__slug = faq_slug)
                serializer = FAQSerializer(get_obj, many=True)
                return Response({'FAQ Detail':serializer_detail.data,'FAQ':serializer.data})
            
            except Exception as e:
                return Response({'error': str(e)})
        else:
            obj         = FAQ.objects.all()
            serializer  = FAQSerializer(obj, many=True)
            return Response({'FAQ Detail':serializer_detail.data,'FAQ':serializer.data})

class ContactsAPI(APIView):
    def get(self,request):
        obj = Contacts.objects.all().last()
        serializer = ContactsSerializer(obj, many=False)
        return Response(serializer.data)

#------------------------Banner------------------------
class HomeBannerAPI(APIView):
    def get(self,request):
        obj = Banner.objects.filter(banner_type='Home').last()
        serializer = BannerSerializer(obj, many=False)
        return Response(serializer.data)

class BlogBannerAPI(APIView):
    def get(self,request):
        obj = Banner.objects.filter(banner_type='Blog').last()
        serializer = BannerSerializer(obj, many=False)
        return Response(serializer.data)

class AboutBannerAPI(APIView):
    def get(self,request):
        obj = Banner.objects.filter(banner_type='About').last()
        serializer = BannerSerializer(obj, many=False)
        return Response(serializer.data)

class CatalogsBannerAPI(APIView):
    def get(self,request):
        obj = Banner.objects.filter(banner_type='Catalogs').last()
        serializer = BannerSerializer(obj, many=False)
        return Response(serializer.data)

class GetInTouchBannerAPI(APIView):
    def get(self,request):
        obj = Banner.objects.filter(banner_type='GetInTouch').last()
        serializer = BannerSerializer(obj, many=False)
        return Response(serializer.data)    

class FAQBannerAPI(APIView):
    def get(self,request):
        obj = Banner.objects.filter(banner_type='FAQ').last()
        serializer = BannerSerializer(obj, many=False)
        return Response(serializer.data)
#------------------------End Banner------------------------

class WhyChoiceUsAPI(APIView):
    def get(self,request):
        obj = WhyChoiceUs.objects.all().last()
        serializer = WhyChoiceUsSerializer(obj, many=False)
        return Response(serializer.data)

class SolutionAllLightingAPI(APIView):
    def get(self,request):
        obj = SolutionAllLighting.objects.all().last()
        serializer = SolutionAllLightingSerializer(obj, many=False)
        return Response(serializer.data)

class OurAchievementsAPI(APIView):
    def get(self,request):
        obj = OurAchievements.objects.all().last()
        serializer = OurAchievementsSerializer(obj, many=False)
        return Response(serializer.data)

class OurTeamsAPI(APIView):
    def get(self,request):
        obj = OurTeams.objects.all().order_by('-id')[:4]
        serializer = OurTeamsSerializer(obj, many=True)
        return Response(serializer.data)

class BlogTagAPI(APIView):
    def get(self,request):
        obj = BlogTag.objects.all().order_by('-id')
        serializer = BlogTagSerializer(obj, many=True)
        return Response(serializer.data)

class BlogAPI(APIView):
    def get(self,request):
        obj = Blog.objects.all()
        serializer = BlogSerializer(obj, many=True)
        return Response(serializer.data)

class TermsAndConditionsAPI(APIView):
    def get(self,request):
        obj = TermsAndConditions.objects.all().last()
        serializer = TermsAndConditionsSerializer(obj, many=False)
        return Response(serializer.data)

class QualityMattersAboutAPI(APIView):
    def get(self,request):
        obj = QualityMatters.objects.filter(quality_choice='About').last()
        serializer = QualityMattersAboutSerializer(obj, many=False)
        return Response(serializer.data)













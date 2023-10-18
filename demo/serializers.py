from rest_framework import serializers
from .models import *


class FAQDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQDetail
        fields = '__all__'

class ShopByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopByCategory
        fields = '__all__'

class QualityMattersHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityMatters
        exclude = ['image','image1']

class QualityMattersAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityMatters
        fields = "__all__"

class QualityMattersCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityMattersCards
        fields = '__all__'

class OneStopShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneStopShop
        fields = '__all__'

class TestmonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testmonials
        fields = '__all__'

class FAQCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQCategory
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    category = FAQCategorySerializer(read_only=True)
    class Meta:
        model = FAQ
        fields = '__all__'

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class WhyChoiceUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoiceUs
        fields = '__all__'

class SolutionAllLightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionAllLighting
        fields = '__all__'

class OurAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAchievements
        fields = '__all__'

class OurTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeams
        fields = '__all__'

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    tags = BlogTagSerializer(many=True)
    class Meta:
        model = Blog
        fields = '__all__'

class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = '__all__'

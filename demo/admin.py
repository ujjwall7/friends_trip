from django.contrib import admin

from .models import *

@admin.register(FAQDetail)
class FAQDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(ShopByCategory)
class ShopByCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(QualityMatters)
class QualityMattersAdmin(admin.ModelAdmin):
    list_display = ('quality_choice', 'title', 'description', 'image', 'image1')

@admin.register(QualityMattersCards)
class QualityMattersCardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')

@admin.register(OneStopShop)
class OneStopShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')

@admin.register(Testmonials)
class TestmonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'description', 'image')

@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('category', 'question', 'answer')

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'address', 'email', 'mobile')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner_type', 'title', 'description', 'image')

@admin.register(WhyChoiceUs)
class WhyChoiceUsAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(SolutionAllLighting)
class SolutionAllLightingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

@admin.register(OurAchievements)
class OurAchievementsAdmin(admin.ModelAdmin):
    list_display = ('happy_clients', 'project_completed', 'phone_support', 'hard_workers')

@admin.register(OurTeams)
class OurTeamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image', 'linkedin', 'instagram', 'twitter')

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_popular_post', 'is_trending_post', 'slug')

@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    path('faq-home/', views.FAQHomeAPI.as_view()),
    path('shop-by-category/', views.ShopByCategoryAPI.as_view()),
    path('quality-matters-homepage/', views.QualityMattersHomeAPI.as_view()),
    path('quality-matters-about/', views.QualityMattersAboutAPI.as_view()),
    path('quality-matters-cards/', views.QualityMattersCardsAPI.as_view()),
    path('one-stop-shop/', views.OneStopShopAPI.as_view()),
    path('testimonials/', views.TestmonialsAPI.as_view()),
    path('faq-category/', views.FAQCategoryAPI.as_view()),
    path('faq/', views.FAQAPI.as_view()),
    path('contacts/', views.ContactsAPI.as_view()),

    #-------------------------Banner----------------------
    path('home-banner/', views.HomeBannerAPI.as_view()),
    path('blog-banner/', views.BlogBannerAPI.as_view()),
    path('about-banner/', views.AboutBannerAPI.as_view()),
    path('catalogs-banner/', views.CatalogsBannerAPI.as_view()),
    path('get-in-touch-banner/', views.GetInTouchBannerAPI.as_view()),
    path('faq-banner/', views.FAQBannerAPI.as_view()),
    #-----------------------End Banner----------------------

    path('why-choice-us/', views.WhyChoiceUsAPI.as_view()),
    path('solution-all-lighting/', views.SolutionAllLightingAPI.as_view()),
    path('our-achievements/', views.OurAchievementsAPI.as_view()),
    path('our-teams/', views.OurTeamsAPI.as_view()),
    path('blog-tag/', views.BlogTagAPI.as_view()),
    path('blog/', views.BlogAPI.as_view()),
    path('terms-and-conditions/', views.TermsAndConditionsAPI.as_view()),
]

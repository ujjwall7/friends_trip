from django.urls import path
from . import views


urlpatterns = [

    #Authentication
    path('user_registration/',views.UserRegistrationAPIView.as_view()),
    path('login/',views.Login.as_view()),
    path('logout/',views.Logout.as_view()),

    path('trip/',views.TripAPI.as_view()),
    path('expense/',views.ExpenseAPI.as_view()),
    path('user_price_distributed/',views.UserPriceDistributed.as_view()),


]


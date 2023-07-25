from django.contrib import admin
from .models import *


@admin.register(User)
class UserDisplay(admin.ModelAdmin):
    list_display = ('username','identity', 'mobile', 'profile', 'role', 'id')

@admin.register(Trip)
class TripDisplay(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'id')

@admin.register(Expense)
class ExpenseDisplay(admin.ModelAdmin):
    list_display = ('trip', 'price', 'price_distibuted', 'image', 'description', )

@admin.register(PersonalExpense)
class ExpenseDisplay(admin.ModelAdmin):
    list_display = ('user','description', 'price', )

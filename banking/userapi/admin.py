from re import I
from django.contrib import admin
from .models import UserDetails,BankingDetails
# Register your models here.

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','address','phone')
    
@admin.register(BankingDetails)
class BankingDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','user','account_number','ifsc_code','bank_name','branch_name','account_type')

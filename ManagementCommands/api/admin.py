from django.contrib import admin
from api.models import Contacts
# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','message', 'date']

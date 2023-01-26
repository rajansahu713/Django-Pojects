from django.contrib import admin
from .models import Blogs

# Register your models here.
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display =["title", "image","body","deleted"]
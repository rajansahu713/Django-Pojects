from django.contrib import admin
from .models import FileUpload

# Register your models here.

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FileUpload._meta.fields]

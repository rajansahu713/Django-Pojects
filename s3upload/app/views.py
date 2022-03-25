from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FileUpload


# Create your views here.

class FileUploadView(APIView):
    def post(self, request, format=None):
        file_obj = request.data['file']
        file_name = request.data['file_name']
        file_upload = FileUpload(file_name=file_name, file=file_obj)
        file_upload.save()
        return Response({"message": "File uploaded successfully"})

        


   




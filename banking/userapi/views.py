from django.shortcuts import render
from .models import UserDetails,BankingDetails
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserDetailsSerializer,BankingDetailsSerializer
# Create your views here.

class UserDetailsViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id is not None:
            user = UserDetails.objects.get(id=id)
            serializer = UserDetailsSerializer(user)
            return Response(serializer.data)
        else:
            users = UserDetails.objects.all()
            serializer = UserDetailsSerializer(users,many=True)
            return Response(serializer.data)


    def post(self,request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.query_params.get('id')
        user = UserDetails.objects.get(id=id)
        user.delete()
        return Response("User Deleted")

    def put(self,request):
        id = request.query_params.get('id')
        user = UserDetails.objects.get(id=id)
        serializer = UserDetailsSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def patch(self,request):
        id = request.query_params.get('id')
        user = UserDetails.objects.get(id=id)
        serializer = UserDetailsSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BankingView(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id is not None:
            banking = BankingDetails.objects.get(id=id)
            serializer = BankingDetailsSerializer(banking)
            return Response(serializer.data)
        banking = BankingDetails.objects.all()
        serializer = BankingDetailsSerializer(banking,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BankingDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.query_params.get('id')
        banking = BankingDetails.objects.get(id=id)
        banking.delete()
        return Response("Banking Deleted")

    def put(self,request):
        id = request.query_params.get('id')
        banking = BankingDetails.objects.get(id=id)
        serializer = BankingDetailsSerializer(banking,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        id = request.query_params.get('id')
        banking = BankingDetails.objects.get(id=id)
        serializer = BankingDetailsSerializer(banking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



from rest_framework import serializers
from userapi.models import UserDetails,BankingDetails


class BankingDetailsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = BankingDetails
        fields = ('id','user','account_number','ifsc_code','bank_name','branch_name','account_type')

class UserDetailsSerializer(serializers.ModelSerializer):
    banking_details = BankingDetailsSerializer(read_only=True,many=True)
    class Meta:
        model = UserDetails
        fields = '__all__'
        
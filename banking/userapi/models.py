from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class BankingDetails(models.Model):
    user = models.ForeignKey(UserDetails,related_name='banking_details', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name


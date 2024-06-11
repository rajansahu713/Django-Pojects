from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name
    
    class Meta:
        unique_together = ['user',"phone"]


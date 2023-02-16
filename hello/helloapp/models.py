from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class CustomUser(models.Model):
    type=(
        ('student','Student'),('teacher','Teacher'),('room woner','Room woner')
    )
    user_type=models.CharField(choices=type, max_length=20,default='student')
    phone=models.IntegerField()
    user=models.OneToOneField(User , on_delete= models.CASCADE)



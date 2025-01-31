from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class User(models.Model):
    CLIENT = 'client'
    PET_SITTER = 'petsitter'

    STATUS_CHOICES = [
        (CLIENT, 'Client'),
        (PET_SITTER, 'Pet Sitter'),
    ]
    name=models.CharField(max_length=255,unique=True,verbose_name='Имя')
    email=models.EmailField(unique=True,verbose_name='Почта')
    password=models.CharField(max_length=255, verbose_name='Пароль')
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=CLIENT, verbose_name='Роль')

    def set_password(self,raw_password):
        self.password=make_password(raw_password)
    def check_password(self, raw_password):
        return check_password(raw_password,self.password)

# Create your models here.

from django.db import models
from users.models import User

class PetOwner(models.Model):
    pass

class PetSitter(models.Model):
    pass


class Order(models.Model):
    STATUS_CHOICES ={
        'Appr' : 'Approved',
        'InPr' : 'InProgress',
        'Done' : 'Done',
        'Decl' : 'Declined'
    }

    created_at = models.DateTimeField(auto_now_add=True)
    petowner = models.OneToOneField(PetOwner, on_delete=models.PROTECT)           # PROTECT ?
    petsitter = models.ForeignKey(PetSitter, on_delete=models.PROTECT)            # PROTECT ?
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)                 
    detail = models.CharField(max_length=500, blank=False)                          # blank?
    approved_by_sitter = models.OneToOneField(User, on_delete=models.PROTECT)       # PROTECT ?

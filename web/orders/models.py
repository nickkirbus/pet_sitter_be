from django.db import models
from users.models import User


class Order(models.Model):
    STATUS_CHOICES ={
        'Crtd' : 'Created',
        'Appr' : 'Approved',
        'InPr' : 'InProgress',
        'Done' : 'Done',
        'Decl' : 'Declined'
    }

    created_at = models.DateTimeField(auto_now_add=True)
    petowner = models.OneToOneField(User, on_delete=models.PROTECT, related_name='petowner')                                              # PROTECT ?
    petsitter = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='petsitter')                        # PROTECT ?
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='Crtd')                 
    detail = models.CharField(max_length=500, blank=False)
    approved_by_sitter = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True, related_name='approved_by_sitter')   # PROTECT ?

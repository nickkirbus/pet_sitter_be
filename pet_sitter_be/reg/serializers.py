from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name','email','password','status']
    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in User.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError("Invalid status. Must be 'client' or 'petsitter'.")
        return value
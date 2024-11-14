from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

        from rest_framework.serializers import ModelSerializer

class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "pk",)
from rest_framework import serializers
from .models import MutsaUser

class UserLoginRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    uid = serializers.CharField()

class UserTokenReissueSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
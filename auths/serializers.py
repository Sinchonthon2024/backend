from rest_framework import serializers
from .models import MutsaUser

class UserLoginRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    uid = serializers.CharField()

class UserTokenReissueSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutsaUser
        fields = ['id','nickname']

class UserResponseSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    home = serializers.CharField()
    school = serializers.CharField()
    region_1depth_name = serializers.CharField()
    region_2depth_name = serializers.CharField()

class UserNicknameSerializer(serializers.Serializer):
    user_name = serializers.CharField()
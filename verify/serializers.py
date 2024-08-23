from rest_framework import serializers
from auths.models import MutsaUser

class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutsaUser
        fields = '__all__'

class UserVerifycodeSerializer(serializers.Serializer):
    verify_code = serializers.CharField()
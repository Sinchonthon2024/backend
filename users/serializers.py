from rest_framework import serializers
from auths.models import MutsaUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutsaUser
        fields = ['id','nickname']

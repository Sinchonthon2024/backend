from rest_framework import serializers
from auths.models import MutsaUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutsaUser
        fields = ['id','nickname']
        

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutsaUser
        fields = ['user_name', 'region_1depth_name', 'region_2depth_name']  # 업데이트 가능한 필드만 선택

    def validate(self, data):
        # 추가적인 유효성 검사를 여기서 할 수 있음
        return data


from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'category', 'detail', 'title', 'text', 'limit', 'link', 'deadline', 'image', 'date']

    def validate(self, data):
        category = data.get('category')
        detail = data.get('detail')
        
        if category == '소셜링' and detail not in ['스터디', '문화', '취미', '여행']:
            raise serializers.ValidationError("소셜링 카테고리에서는 스터디, 문화, 취미, 여행만 선택할 수 있습니다.")
        
        if category == '나눔' and detail not in ['생활용품', '음식', '가구']:
            raise serializers.ValidationError("나눔 카테고리에서는 생활용품, 음식, 가구만 선택할 수 있습니다.")
        
        return data

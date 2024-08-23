from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='writer.user_name', read_only=True)

    class Meta:
        model = Post
        fields = ['user_name', 'id', 'date', 'category', 'detail', 'title', 'text', 'limit', 'link', 'deadline', 'image']

    def validate(self, data):
        category = data.get('category')
        detail = data.get('detail')
        
        if category == '소셜링' and detail not in ['스터디', '문화', '취미', '여행']:
            raise serializers.ValidationError("소셜링 카테고리에서는 스터디, 문화, 취미, 여행만 선택할 수 있습니다.")
        
        if category == '나눔' and detail not in ['생활용품', '음식', '가구']:
            raise serializers.ValidationError("나눔 카테고리에서는 생활용품, 음식, 가구만 선택할 수 있습니다.")
        
        return data

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response = {
            "user_name": instance.writer.user_name,
            "id": instance.id,
            "date": instance.date,
            "post": {
                "category": instance.category,
                "detail": instance.detail,
                "title": instance.title,
                "text": instance.text,
                "limit": instance.limit,
                "link": instance.link,
                "deadline": instance.deadline,
                "image": instance.image.url if instance.image else None,
            }
        }
        return response

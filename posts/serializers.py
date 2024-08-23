from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'category', 'detail', 'title', 'text', 'link', 'deadline', 'image', 'date']

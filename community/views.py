# community/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

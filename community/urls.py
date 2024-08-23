# community/urls.py
from django.urls import path
from .views import PostListCreateView, CommentCreateView, LikeCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),
]

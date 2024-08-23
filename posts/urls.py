from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
]

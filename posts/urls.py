from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
]

from django.urls import path
from .views import CommentCreateView, LikeToggleView

urlpatterns = [
    path('api/posts/<int:post_id>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('api/posts/<int:post_id>/like/', LikeToggleView.as_view(), name='like-toggle'),
]

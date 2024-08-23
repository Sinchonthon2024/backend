from django.urls import path
from .views import MyPostListView, UserInfoUpdateView

urlpatterns = [
    path('api/mypage/mypost/', MyPostListView.as_view(), name='mypost-list'),
    path('api/mypage/info/', UserInfoUpdateView.as_view(), name='user-info-update'),
]

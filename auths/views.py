import os

import requests
import jwt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer

from rest_framework_simplejwt.tokens import RefreshToken

from auths.models import MutsaUser
from .serializers import UserLoginRequestSerializer, UserTokenReissueSerializer
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string

from dotenv import load_dotenv

load_dotenv()  # env 환경변수 로드


def get_jwks_url():
    discovery_url = "https://kauth.kakao.com/.well-known/openid-configuration"
    response = requests.get(discovery_url)
    response.raise_for_status()
    config = response.json()
    return config["jwks_uri"]



# Refresh 토큰으로 Access 토큰 재발급하는 API
@api_view(['POST'])
@permission_classes([AllowAny])
def token_reissue(request):
    refresh_token_serializer = UserTokenReissueSerializer(data=request.data)  # 요청 데이터인 refresh_token을 역직렬화

    if not refresh_token_serializer.is_valid():
        return Response(refresh_token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    refresh_token = refresh_token_serializer.validated_data['refresh_token']

    try:
        user = MutsaUser.objects.get(refresh_token=refresh_token)  # 데이터베이스에서 refresh_token이 같은 유저 조회
    except MutsaUser.DoesNotExist:
        return Response({"detail": "해당 회원이 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Refresh token을 사용하여 새로운 access token 생성
        new_access_token = RefreshToken(refresh_token).access_token
    except jwt.InvalidTokenError:
        return Response({'detail': '유효하지 않은 refresh token입니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    # 새로운 access token 반환
    return Response({
        'access_token': str(new_access_token)
    }, status=status.HTTP_200_OK)
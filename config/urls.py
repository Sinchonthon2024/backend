"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from auths.views import login
from verify.views import SendVerification, CheckVerifycode

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls') ),

    #auth
    path("api/auth/login", login),

    #verify
    path("api/auth/verify", SendVerification),
    path("api/verify/check", CheckVerifycode),


]

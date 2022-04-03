"""travelblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from posts.views import posts, comments, likes, delete_comment
from home.views import home
from aboutme.views import aboutme

# from comments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('posts/', posts, name='posts'),
    path('<slug:slug>/', comments, name='comments'),
    path('like/<slug:slug>', likes, name='likes'),
    path('delete/<comment_id>/', delete_comment, name='delete'),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('aboutme.html', aboutme, name='aboutme'),
]

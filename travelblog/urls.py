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
from posts.views import posts, likes, delete_post, edit_post
from comments.views import comments, delete_comment, edit_comment
from home.views import home
from aboutme.views import aboutme
from contact.views import contact
from profile.views import profile, approve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('posts/', posts, name='posts'),
    path('comments/', include('comments.urls')),
    path('like/<slug:slug>', likes, name='likes'),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('aboutme/', include('aboutme.urls')),
    path('contact/', include('contact.urls')),
    path('profile/', include('profile.urls')),
    path('posts_delete/<post_id>/', delete_post, name='delete_post'),
    path('posts_edit/<post_id>/', edit_post, name='edit_post'),
]

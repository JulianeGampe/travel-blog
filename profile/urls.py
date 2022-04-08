from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('approve/<comment_id>/', views.approve, name='approve'),
]

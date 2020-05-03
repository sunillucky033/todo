from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('profile',views.profile,name='profile'),
    path('profile_view',views.profile_view,name='profile_view'),
]
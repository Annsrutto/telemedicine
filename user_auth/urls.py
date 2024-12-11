from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('register/', views.sign_up, name='register'), # User registration url
    path('login/', views.sign_in, name='login'), # User login url
    path('logout/', views.user_logout, name='logout'), # Logout url
]

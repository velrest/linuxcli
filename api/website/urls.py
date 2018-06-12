from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('commands/', views.commands, name='commands'),
    path('lockout/', views.lockout, name='lockout'),
    path('home/', views.commands, name='commands'),
    path('command/<str:command>/', views.commands, name='commands'),
]

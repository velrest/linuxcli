from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    # Example routes for other shit
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('register/', views.register, name='register'),
]

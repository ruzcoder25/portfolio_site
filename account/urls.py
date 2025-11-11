from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('logout_user/', views.logout_user, name='logout_user'),
]
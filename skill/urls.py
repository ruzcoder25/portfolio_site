from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill_list, name='skill_list'),
    path('create/', views.skill_create, name='skill_create'),
    path('<int:pk>/', views.skill_detail, name='skill_detail'),
    path('<int:pk>/update/', views.skill_update, name='skill_update'),
    path('<int:pk>/delete/', views.skill_delete, name='skill_delete'),
]

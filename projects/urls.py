from django.urls import path
from . import views

urlpatterns = [
    path('project_create/', views.project_create, name='project_create'),
    path('project_list/', views.project_list, name='project_list'),
    path('<int:pk>/project_detail/', views.project_detail, name='project_detail'),
    path('<int:pk>/project_update/', views.project_update, name='project_update'),
    path('<int:pk>/project_delete/', views.project_delete, name='project_delete'),
]
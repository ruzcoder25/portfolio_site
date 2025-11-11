from django.urls import path
from .views import (
    EducationListView,
    EducationCreateView,
    EducationUpdateView,
    EducationDeleteView
)

urlpatterns = [
    path('', EducationListView.as_view(), name='education_list'),
    path('  add/', EducationCreateView.as_view(), name='education_add'),
    path('<int:pk>/edit/', EducationUpdateView.as_view(), name='education_edit'),
    path('<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
]

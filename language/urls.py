from django.urls import path
from .views import (
    LanguageListView,
    LanguageCreateView,
    LanguageUpdateView,
    LanguageDeleteView
)

urlpatterns = [
    # Har bir foydalanuvchi ko‘ra oladigan ro‘yxat
    path('languages/', LanguageListView.as_view(), name='language_list'),

    # Faqat admin uchun CRUD
    path('languages/add/', LanguageCreateView.as_view(), name='language_add'),
    path('languages/<int:pk>/edit/', LanguageUpdateView.as_view(), name='language_edit'),
    path('languages/<int:pk>/delete/', LanguageDeleteView.as_view(), name='language_delete'),
]

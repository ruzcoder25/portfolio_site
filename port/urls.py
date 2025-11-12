from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # foydalanuvchi sahifalari
    path('', include('port_view.urls')),

    # admin bo‘limlari
    path('accounts/', include('account.urls')),
    path('education/', include('education.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('language/', include('language.urls')),
    path('project/', include('projects.urls')),
    path('skill/', include('skill.urls')),
]

# static & media fayllar faqat DEBUG=True bo‘lsa xizmat qilinadi
if settings.DEBUG:
    # Media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Static (devda STATICFILES_DIRS dan)
    if settings.STATICFILES_DIRS:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    else:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

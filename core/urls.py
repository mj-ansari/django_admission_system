from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('admission.urls')), #Request Forwarding To Admission Urls
    path('accounts/', include('accounts.urls')), #Request Forwarding To Authentication Urls
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from leadsapp.views import home_view, profile_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("accounts/profile/", profile_view, name="account_profile"),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

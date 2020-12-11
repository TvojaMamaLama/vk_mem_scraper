from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('API.urls')),
    path('profiles/', include('profiles.urls')),
]

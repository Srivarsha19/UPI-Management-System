from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),      # This is the path for the Django admin interface
    path('', include('core.urls')),       # This includes the URLs from the core app
]

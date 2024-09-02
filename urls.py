from django.contrib import admin
from django.urls import path, include
from core import views  # Corrected import to use core.views directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  # Redirect root URL to index view
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

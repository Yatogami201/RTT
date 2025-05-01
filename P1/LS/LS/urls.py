"""
URL configuration for LS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from login.views import login_view, home_view_vendedor, home_view_cliente, register  
from Vendedor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')), 
    path('search/', include('search.urls')), 
    path("recomendaciones/", include("chat_recomendaciones.urls")),
    path('login/', login_view, name='login'),
    path("vendedor/", home_view_vendedor, name="vendedor"),
    path("cliente/", home_view_cliente, name="cliente"),
    path('register/', register, name='register'), 
    path('', views.inicio, name='inicio'),
    path('vendedor/', views.perfil_view, name='perfil'),
    path('chat/', include('chat.urls')),  
]

# Servir archivos de la carpeta media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

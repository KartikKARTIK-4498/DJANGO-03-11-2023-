"""head URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.test, name="test"),
    path('home/', views.test, name="test"),
    path('search/<str:name>/', views.search, name="search"),
    path('place/<int:place_id>/', views.place, name="place"),
    path('nearby/<str:nearby>/', views.nearby, name="nearby"),
    path('all/', views.all, name="all"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

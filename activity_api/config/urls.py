"""
URL configuration for abduls_assignment_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from apps.todo.api.views import ActivityViewSet

api_prefix = "api/"
api_ver = "v1/"
context_root = api_prefix + api_ver

router = DefaultRouter()
router.register(context_root + r"activity", ActivityViewSet, basename="activity")

urlpatterns = [
    path(context_root + "admin/", admin.site.urls),
]

urlpatterns += router.urls

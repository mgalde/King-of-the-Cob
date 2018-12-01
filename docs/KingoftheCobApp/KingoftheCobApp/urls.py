"""KingoftheCobApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts import views, resources
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Notes', views.NoteView)
router.register('Tasks', views.TaskView)

# Defining home and connected url views for easier use
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('connected/', TemplateView.as_view(template_name='connected.html'), name='connected'),
    path('kanban/', TemplateView.as_view(template_name='kanban.html'), name='kanban'),
    path('api/workhorse/', include(router.urls)),
]

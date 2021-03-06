from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from . import views, resources
from .views import NoteView, TaskView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Notes', views.NoteView)
router.register('Tasks', views.TaskView)

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/developer/', views.DeveloperSignUpView.as_view(), name='developer_signup'),
    path('signup/owner/', views.OwnerSignUpView.as_view(), name='owner_signup'),
    path('signup/scrumaster/', views.ScrumasterSignUpView.as_view(), name='scrumaster_signup'),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/workhorse/', include(router.urls)),
]

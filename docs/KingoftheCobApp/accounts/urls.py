from django.urls import include, path
from django.contrib import admin
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/developer/', views.DeveloperSignUpView.as_view(), name='developer_signup'),
    path('signup/owner/', views.OwnerSignUpView.as_view(), name='owner_signup'),
    path('signup/scrumaster/', views.ScrumasterSignUpView.as_view(), name='scrumaster_signup'),
]

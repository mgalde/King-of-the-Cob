from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db import models, migrations
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from .forms import DeveloperSignUpForm, OwnerSignUpForm, ScrumasterSignUpForm
from .models import User
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.db import migrations
from .decorators import scrumaster_required, owner_required, developer_required
from .forms import DeveloperSignUpForm, OwnerSignUpForm, ScrumasterSignUpForm, TicketForm
from .models import User, Note, Task
# Using Charts in Django
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer, TaskSerializer


User = get_user_model()

# This is where a user can select the type of user to sign up as
class SignUp(TemplateView):
    template_name = 'signup.html'

# This defines developer user and assignes the user as a developer
class DeveloperSignUpView(CreateView):
    model = User
    form_class = DeveloperSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'developer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('connected')

# This defines the Owner user and assignes the user as a Product Owner
class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('connected')

# This defines the Scrumaster user and assignes the user as a SCRUM Master
class ScrumasterSignUpView(CreateView):
    model = User
    form_class = ScrumasterSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'scrumaster'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('connected')


@method_decorator([login_required], name='dispatch')
class NoteView(viewsets.ModelViewSet):
        queryset = Note.objects.all()
        serializer_class = NoteSerializer

@method_decorator([login_required], name='dispatch')
class TaskView(viewsets.ModelViewSet):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer
        def get(self, request, format=None):
            return JsonResponse()

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Registration
from .forms import RegistrationForm

# Registration Views

class RegistrationListView(LoginRequiredMixin, ListView):
    model = Registration
    template_name = 'registrations/list.html'
    context_object_name = 'registrations'

class RegistrationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'registrations/create.html'
    permission_required = 'add_registration'
    success_url = '/registrations/'
    success_message = 'Registration created successfully!'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class RegistrationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'registrations/update.html'
    permission_required = 'change_registration'
    success_url = '/registrations/'
    success_message = 'Registration updated successfully!'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class RegistrationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Registration
    template_name = 'registrations/delete.html'
    permission_required = 'delete_registration'
    success_url = '/registrations/'
    success_message = 'Registration deleted successfully!'

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)


def homepage(request):
    return render(request, 'homepage.html')
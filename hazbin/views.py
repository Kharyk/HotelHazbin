from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Registration
from .forms import RegistrationForm

from django.contrib.auth.decorators import login_required, permission_required


@login_required
def homepage(request):
    return render(request, 'homepage.html')

@login_required
@permission_required('can_add_registration')
def createpage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration created successfully!')
            return redirect('listpage')
    else:
        form = RegistrationForm()
    return render(request, 'create.html', {'form': form})

@login_required
@permission_required('can_delete_registration')
def deletepage(request, pk):
    Registration.objects.get(pk=pk).delete()
    messages.success(request, 'Registration deleted successfully!')
    return redirect('listpage')

@login_required
def listpage(request):
    registrations = Registration.objects.all()
    return render(request, 'egistration_list.html', {'registrations': registrations})

@login_required
@permission_required('can_change_registration')
def updatepage(request, pk):
    registration = Registration.objects.get(pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration updated successfully!')
            return redirect('listpage')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'update.html', {'form': form})

@login_required
def logpage(request):
    return render(request, 'log.html')

@login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration created successfully!')
            return redirect('listpage')
    else:
        form = RegistrationForm()
    return render(request, 'egister.html', {'form': form})
    # Registration Views
"""
class RegistrationListView(LoginRequiredMixin, ListView):
    model = Registration
    template_name = 'registrations/registration_list.html'
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
"""



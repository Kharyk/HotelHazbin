from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Registration, Client, Administration, Schedule, HotelRooms
from .forms import RegistrationForm

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login



@login_required
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def logpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        client = authenticate(request, username=username, password=password)
        if client is not None:
            login(request, client)
            return redirect('hotelrooms')
        else:
            return render(request, "log.html", {'error': 'Invalid username or password'})
    return render(request, "log.html")


@login_required
def logout(request):
    return render(request, "homepage.html")



@login_required
def createpage(request):
    if request.method== 'POST':
        user = Client(name=request.POST.get("name"),
               email=request.POST.get("email"),
               account_type=request.POST.get("accounttype"),
               password=request.POST.get("password"),)
        user.save()
    return render(request, "for_user/create.html")


@login_required
def registerpage(request):
    if request.method == 'POST':
        name = request.POST.get("username")
        client, created = Client.objects.get_or_create(name=name)
        hotelroom_number = request.POST.get("hotel_room")
        try:
            hotelroom = HotelRooms.objects.get(number=hotelroom_number)
        except HotelRooms.DoesNotExist:
            return render(request, "for_user/register_u.html", {'error': 'Hotel room does not exist'})
        
        administration = Administration.objects.first()
        
        regist = Registration(
            client=client,
            hotelroom=hotelroom,
            administration=administration,
            start_date_time=request.POST.get("start_datetime"),
            end_date_time=request.POST.get("end_datetime"),
        )
        regist.save()
        return redirect('registration')
    return render(request, "for_user/register_u.html")


@login_required
def hotelroomspage(request):
    return render(request, 'for_user/hotelrooms.html')

@login_required
def deletepage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        registrations = Registration.objects.filter(client__name=name)
        if registrations.exists():
            registrations.delete()
            return redirect('registration')  
        else:
            return render(request, "for_user/delete.html", {'error': 'No registration found with that name'})
    return render(request, "for_user/delete.html")

@login_required
def addadmin(request):
    if request.method=='POST':
        admin = Administration(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
        )
        admin.save()
    return render(request, "for_admin/addadmin.html")

@login_required
def schedule(request):
    if request.method == "POST":
        administration_name = request.POST.get("name")
        administration = Administration.objects.get(name=administration_name)
        schedule = Schedule(
            day_time=request.POST.get("day_time"),
            end_time=request.POST.get("end_time"),
            administration=administration,
        )
        schedule.save()
    return render(request, "for_admin/schedule.html")

@login_required
def registlist(request):
    registrations = Registration.objects.all()
    return render(request, "for_admin/registration_list.html", {'registrations': registrations})

@login_required
def info(request):
    return render(request, "for_user/info.html")













"""@permission_required('can_add_registration')
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
    # Registration Views """
    
    
    
    
    
    
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



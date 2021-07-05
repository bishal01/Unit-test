from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users,checkgroup
from django.contrib.auth.models import Group

# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='patient')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def doctor_register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='doctor')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'doctor_register.html', {'form': form})



@allowed_users(allowed_roles=['doctor','patient'])
@login_required(login_url="login")
def profile(request):
    return render(request,'profile.html')


@login_required(login_url="login")
@allowed_users(allowed_roles=['doctor'])
@checkgroup
def doctor(request):
    return render(request,'doctor.html')

@allowed_users(allowed_roles=['patient','doctor'])
@login_required(login_url="login")
def patient(request):
 return render(request,'patient.html')

def profile_redirect(request):
    group=None
    if request.user.groups.exists():
        group=request.user.groups.all()[0].name
    if group=='patient':
        return redirect('patient')

    if group=='doctor':
        return redirect('doctor')




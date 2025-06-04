from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, LoginForm
from .models import UserProfile


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(
                user=user,
                cidade=form.cleaned_data['cidade'],
                estado=form.cleaned_data['estado'],
                segmento=form.cleaned_data['segmento'],
                plano='gratuito',
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard_view(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'accounts/dashboard.html', {'profile': profile})


def logout_view(request):
    logout(request)
    return redirect('login')

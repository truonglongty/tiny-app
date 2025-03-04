from django.shortcuts import render, redirect
from django.contrib import messages
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
=======
from django.shortcuts import redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import LoginView
from .models import CustomUser
>>>>>>> main

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

<<<<<<< HEAD
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Your account has been blocked.')
        else:
            messages.error(request, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
    return render(request, 'users/login.html')
=======
class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        if user.is_blocked:
            messages.error(self.request, "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ quản trị viên để biết thêm chi tiết.")
            return redirect('login')
        auth_login(self.request, user)
        return super().form_valid(form)
>>>>>>> main

@login_required
def profile(request):
    if request.user.is_active == False:
        messages.error(request, 'Your account has been blocked.')
        auth_logout(request)
        return redirect('login')
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

User = get_user_model()

@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    users = CustomUser.objects.all()
    if request.method == 'POST':
        user_ids = request.POST.getlist('user_ids')
        action = request.POST.get('action')
        if action == 'block':
            CustomUser.objects.filter(id__in=user_ids).update(is_blocked=True)
            messages.success(request, "Selected users have been blocked.")
        elif action == 'unblock':
            CustomUser.objects.filter(id__in=user_ids).update(is_blocked=False)
            messages.success(request, "Selected users have been unblocked.")
        return redirect('manage_users')
    return render(request, 'users/manage_users.html', {'users': users})
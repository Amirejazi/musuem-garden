from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class RegisterUserView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterUserForm()
        return render(request, 'accounts_app/register_user.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username']
            )
            user.set_password(data['password1'])
            user.save()
            messages.success(request, 'ثبت نام با موفقیت انجام شد :)', 'success')
            return redirect('main:index')
        else:
            messages.error(request, 'اطلاعات مورد نظر معتبر نمی باشد!', 'danger')
            return render(request, 'accounts_app/register_user.html', {'form': form})

# ================================================================================================
class LoginUserView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'accounts_app/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f"{user.first_name} {user.last_name} خوش آمدید :)", 'success')
                next_url = request.GET.get('next')
                if next_url is not None:
                    return redirect(next_url)
                else:
                    return redirect('main:index')
            else:
                messages.warning(request, "نام کاربری یا رمز عبور اشتباه است!",)
                return render(request, 'accounts_app/login.html', {'form': form})
        else:
            messages.warning(request, "اطلاعات وارد شده معتبر نمی باشد!", 'danger')
            return render(request, 'accounts_app/login.html', {'form': form})

# ================================================================================================
class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'خداحافظ کوچولو')
        return redirect('main:index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('main:index')
        return super().dispatch(request, *args, **kwargs)
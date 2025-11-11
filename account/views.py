from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileForm, LoginForm

def login_admin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Email yoki parol noto‘g‘ri!")
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

@login_required
def profile(request):
    # Foydalanuvchi o‘z profilini ko‘radi
    user = request.user
    context = {'user': user}
    return render(request, 'admin/profile/profile.html', context)

@login_required
def update_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil muvaffaqiyatli yangilandi")
            return redirect('profile')
        else:
            messages.error(request, "Ma'lumotlarni tekshirib qayta urinib ko‘ring")
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'admin/profile/update_profile.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Siz tizimdan chiqdingiz")
    return redirect('login_admin')

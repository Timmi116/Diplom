from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileForm, PhotoUploadForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            response = redirect('/profile/')
            response.set_cookie('user_id', str(user.id))
            return response
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, 'title': 'Регистрация'})

def profile(request):
    if request.method == 'POST':
        user_id = request.COOKIES.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        form = ProfileForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            
            response = redirect('/upload_photo/')
            response.set_cookie('user_id', str(user.id))
            return response
    else:
        user_id = request.COOKIES.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        form = ProfileForm(instance=user)
    return render(request, 'profile.html', {'form': form, 'title': 'Профиль'})

def upload_photo(request):
    if request.method == 'POST':
        user_id = request.COOKIES.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        form = PhotoUploadForm(request.POST, request.FILES, instance=user)
        
        if form.is_valid():
            form.save()
            return redirect('/congratulations/')
    else:
        user_id = request.COOKIES.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        form = PhotoUploadForm(instance=user)
    return render(request, 'upload_photo.html', {'form': form, 'title': 'Загрузка фотографии'})

def congratulations(request):
    return render(request, 'congratulations.html', {'title': 'Поздравления!'})
from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'gender', 'email', 'password']
        labels = {
            'username': 'Имя пользователя',
            'age': 'Возраст',
            'gender': 'Пол',
            'email': 'Электронная почта',
            'password': 'Пароль',
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['date_of_birth', 'place_of_birth', 'address', 'biography']
        labels = {
            'date_of_birth': 'Дата рождения',
            'place_of_birth': 'Место рождения',
            'address': 'Адрес проживания',
            'biography': 'Биография',
        }

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']
        labels = {
            'profile_picture': 'Фотография',
        }
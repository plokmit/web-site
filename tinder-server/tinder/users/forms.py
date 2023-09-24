import itertools

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User
from main.models import Interests

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Введите пароль",
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    INTERESTS = tuple(i for i in Interests.objects.values_list())
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Введите Фамилию",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Введите эл. почту",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Введите пароль повторно",
    }))

    age = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'number'
    }))
    interests = forms.MultipleChoiceField(choices=INTERESTS,
                                          widget=forms.CheckboxSelectMultiple(attrs={
        'placeholder': 'Интересы'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Описание'
    }))
    image = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'placeholder': 'Фото',
    }))
    prefer_age_min = forms.IntegerField(widget=forms.NumberInput(attrs={
        'id': 'age-min',
        'min': "18",
        'max': "99",
    }))
    prefer_age_max = forms.IntegerField(widget=forms.NumberInput(attrs={
        'id': 'age-max',
        'min': "18",
        'max': "99",
    }))
    prefer_location = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'location',
    }))
    prefer_distance_min = forms.IntegerField(widget=forms.NumberInput(attrs={
        'id': 'distance-min',
        'min': "0",
        'max': "99",
    }))
    prefer_distance_max = forms.IntegerField(widget=forms.NumberInput(attrs={
        'id': 'distance-max',
        'min': "0",
        'max': "99",
    }))
    def clean_interests(self):
        data = [int(i) for i in self.cleaned_data.get('interests')]
        temp_data = Interests.objects.all()
        temp_data = [str(i) for i in Interests.objects.all()]
        new_data = str()
        for i in data:
            new_data += temp_data[i-1] + ', '
        return new_data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1',
                  'password2', 'age', 'interests', 'description', 'image', 'prefer_age_min',
                  'prefer_age_max','prefer_location', 'prefer_distance_min', 'prefer_distance_max']


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Фамилия",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя пользователя',
        'readonly': True,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Электронная почта",
        'readonly': True,
    }))

    image = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'placeholder': 'Фото',
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image']


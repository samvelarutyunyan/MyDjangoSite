import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.template.context_processors import request

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddPageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = None

    title = forms.CharField(max_length=255, label="Заголовок",widget=forms.TextInput(attrs={'class': 'form-input'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 33, 'rows': 7,'class': 'form-input'}), label="Текст")
    author = forms.ModelChoiceField(queryset=User.objects.filter(), label='Автор')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")

    # ---- Связка с моделю существующей, только надо в классе вместо form.Form написать form.ModelForm ----
    # -----------------------------------------------------------------------------------------------------
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].empty_label = "Не выбрана"
    #
    # class Meta:
    #     model = Post
    #     fields = ['title', 'body', 'author', 'category']
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-input'}),
    #         'body': forms.Textarea(attrs={'cols': 33, 'rows': 7,'class': 'form-input'}),
    #     }
    # ------------------------------------------------------------------------------------------------------
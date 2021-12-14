from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import User, WorkerProfile

class CompanySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'username')
        labels = { 
            'name': '会社名',
            'username': 'ID'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        user.is_worker = False
        if commit:
            user.save()
        return user

class WorkerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'username', )
        labels = { 
            'name': '氏名',
            'username': 'ID'
        }

    def save(self):
        user = super().save(commit=False)
        user.is_worker = True
        user.is_company = False
        user.save()
        return user


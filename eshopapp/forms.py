from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'postal_code', 'city']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
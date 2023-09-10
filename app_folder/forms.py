from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from app_folder.models import Account

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email = forms.EmailField(help_text="Required. Add a valid email address", widget = forms.EmailInput(attrs = {'class': 'form-control'}))
    
    
    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        try:
            app_folder = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f" Email {email} has been taken already")
    
    def get_username(self):
        username = self.cleaned_data.get('username').lower()
        try:
            app_folder = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f" Username {username} has been taken already")
        
        
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
       
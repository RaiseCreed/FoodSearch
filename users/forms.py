from typing import Any
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalogue.models import Profile


class CustomUserForm(UserCreationForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name': 'Name'
        }


class ProfileForm(ModelForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            
    class Meta:
        model = Profile
        fields = ['username','email','image']
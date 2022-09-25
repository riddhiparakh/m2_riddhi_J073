from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import toDo

class CreateUserform(UserCreationForm):
  class Meta:
    model=User
    fields=['username','email','password1','password2']
    
class toDoForm(forms.ModelForm):
    class Meta:
        model=toDo

        fields="__all__"
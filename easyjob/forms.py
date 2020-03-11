from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control',
                                                                         'placeholder':'Username'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Password',
                                                                }),required=True,label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                  'placeholder':'Password',
                                                                  }),required=True,label='Confirm Password')
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'
                                                                           ,'placeholder':'Firstname',
                                                                           }))
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']

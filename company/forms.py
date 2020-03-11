from .models import Company,Job
from django import forms

class CreateCompany(forms.ModelForm):
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    website=forms.URLField(widget=forms.URLInput(attrs={'class':'form-control'}))
    company_type=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model=Company
        exclude =['user']

class Addpost(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


    class Meta:
        model= Job
        exclude =['company']


class Updatejob(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


    class Meta:
        model =Job
        exclude =['company']
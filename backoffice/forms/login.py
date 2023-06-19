from django import forms
from django.forms import ModelForm, TextInput
from api_fewnu_compta import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'fullName']
        widgets = {
            'fullName': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Nom complet'
                }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Telephone'
                }),
        }

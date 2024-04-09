"""Forms are created to fetch data"""
from django import forms
from django.contrib.auth.models import User
from .models import Movie, Review

"""having basic movie fiels"""
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'director', 'poster']
        widgets = {
            'release_date': forms.SelectDateWidget(empty_label="---"),
        }

"""Class for registraton of new user"""
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

"""class for retriving user reviews"""        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

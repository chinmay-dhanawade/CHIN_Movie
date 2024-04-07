from django import forms
from .models import Movie
from django.contrib.auth.models import User
from .models import Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'director', 'poster']
        widgets = {
            'release_date': forms.SelectDateWidget(empty_label="---"),
        }

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

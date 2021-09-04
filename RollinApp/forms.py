from django import forms
from .models import *
from django.contrib.auth.models import User


class AddMatches(forms.ModelForm):
    class Meta:
        model= Match
from django import forms
from .models import *

class LoginTableForm(forms.ModelForm):
    """Form definition for LoginTable."""

    class Meta:
        """Meta definition for LoginTableform."""

        model = LoginTable
        fields = ('username','password','email')
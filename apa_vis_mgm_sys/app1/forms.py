from django import forms
from .models import *   #Todo

class VisitorForm(forms.ModelForm):
    """Form definiton for Todo."""

    class Meta:
        """Meta definiton for Todoform."""
        model = Visitor
        # fields = '__all__'
        fields = ['status']

# class PassForm(forms.ModelForm):
#     """Form definiton for Todo."""

#     class Meta:
#         """Meta definiton for Todoform."""
#         model = Pass
#         fields = '__all__'





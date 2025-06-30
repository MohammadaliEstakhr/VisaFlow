"""
This module defines Django forms for VisaApplication model.
Used for validating and processing user input.
"""

"""
This module defines Django forms for the Visa Application model.
Used for user input validation and rendering.
"""

from django import forms
from .models import VisaApplication

class VisaApplicationForm(forms.ModelForm):
    class Meta:
        model = VisaApplication
        fields = '__all__'

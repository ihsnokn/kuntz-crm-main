from dataclasses import field
from django import forms
from files.models import Lawyer

class LawyerModelForm(forms.ModelForm):
    class Meta:
        model= Lawyer
        fields = (
            'user',
        )
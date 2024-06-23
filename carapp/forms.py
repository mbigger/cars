from django import forms
from .models import *

class courseform(forms.ModelForm):
    class Meta:
        model  =  coursemodule
        fields = ("__all__")


class questionsform(forms.ModelForm):
    class Meta:
        model  =  questions
        fields = ("__all__")

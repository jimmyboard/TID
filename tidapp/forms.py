# -*- coding: utf-8 -*-
from tidapp.models import Advisory
from django import forms

# Create your models here.

class AdvisoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the name.")
    tel = forms.CharField(max_length=128, help_text="Please enter the tel.")
    content = forms.CharField(widget=forms.Textarea, help_text="Please enter the content.")

    class Meta:
        model = Advisory
        fields = ('name', 'tel', 'content')

from django import forms
from django.db.models import fields
from .models import *



class CsvModelForm(forms.ModelForm):
  class Meta:
    model = Csv
    fields = ('file_name',)
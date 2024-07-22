from django import forms
from . import models

class EnquiryForm(forms.ModelForm):
    class Meta:
        model =models.Enquiry
        exclude = ('time',) 

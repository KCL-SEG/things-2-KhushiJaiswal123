"""Forms of the project."""

# Create your forms here.
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(),'quantity': forms.NumberInput()}
    #name = forms.CharField(label='Name', max_length=35)
    #description = forms.CharField(label='Description', max_length=120, widget=forms.Textarea)
    #quantity = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)], widget=forms.NumberInput)

"""Forms of the project."""

# Create your forms here.
from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label='Name', max_length=35)
    description = forms.CharField(label='Description', max_length=120, widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput)
    # description = forms.Textarea(label='Description', max_length=120)
    # quantity = forms.NumberInput(label='Quantity', max_length=50)


    # min_length = 0 for quantity?

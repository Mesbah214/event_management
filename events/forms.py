from django import forms

class EventForm(forms.Form):
    title = forms.CharField(max_length=250)
    description = forms.CharField()
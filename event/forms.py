from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name','date_event','description','mainImage']
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'mainImage': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'date_event': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def clean(self):        
        return self.cleaned_data
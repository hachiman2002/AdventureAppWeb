from django import forms
from .models import Destinations

class DestinationsForm(forms.ModelForm):
    
    class Meta:
        model = Destinations
        fields = ['name', 'mainImage', 'image1', 'image2', 'image3', 'image4', 'image5',
                'distance', 'suitable_disabled', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mainImage': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image1': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image2': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image3': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image4': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image5': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'distance': forms.NumberInput(attrs={'class':'form-control'}),
            'suitable_disabled': forms.CheckboxInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
        
    def clean(self):        
        return self.cleaned_data
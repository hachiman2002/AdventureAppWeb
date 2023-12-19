from django import forms
from .models import Accommodations

class AccommodationsForm(forms.ModelForm):
    
    class Meta:
        model = Accommodations
        fields = ['name', 'mainImage', 'image1', 'image2', 'image3',
                'address', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mainImage': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image1': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image2': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image3': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
        
    def clean(self):        
        return self.cleaned_data
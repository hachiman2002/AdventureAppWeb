from django import forms
from .models import Social

class SocialForm(forms.ModelForm):
    
    class Meta:
        model = Social
        fields = ['name_key', 'name', 'url']
        widgets = {
            'name_key': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'url': forms.TextInput(attrs={'class':'form-control'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
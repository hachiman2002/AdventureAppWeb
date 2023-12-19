from django import forms
from .models import Pages

class PageForm(forms.ModelForm):
    
    class Meta:
        model = Pages
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
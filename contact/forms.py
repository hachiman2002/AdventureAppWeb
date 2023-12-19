from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Nombre", widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(required=True, label="Correo electronico",widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    content = forms.CharField(required=True, label="Contenido", widget=forms.Textarea(
        attrs={'class': 'form-control'}
    ),min_length=10, max_length=200)
    
    
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Adventure curacautin: nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),#cuerpo
                "no-contestar@inbox.mailtrap.io", #email_origen
                ["adventure@gmail.com"], #email_destino,
                reply_to=[email]
            )
            try:
                email.send()
                #todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    return render(request, 'contact/contact.html', {'form':contact_form})
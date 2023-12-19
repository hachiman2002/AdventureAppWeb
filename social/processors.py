from .models import Social

def context_dict(request):
    context = {}
    links = Social.objects.all()
    for link in links:
        context[link.name_key] = link.url
    return context
from django.shortcuts import render


# Create your views here.
def contact(request):
    template = 'contact/contact.html'
    context = {

    }
    return render(request, template, context)

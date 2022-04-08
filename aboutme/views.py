from django.shortcuts import render


# Create your views here.
def aboutme(request):
    template = 'aboutme/aboutme.html'
    context = {
    }
    return render(request, template, context)

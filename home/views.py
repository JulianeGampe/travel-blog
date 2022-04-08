from django.shortcuts import render


# Create your views here.
def home(request):
    template = 'home/index.html'
    context = {

    }
    return render(request, template, context)

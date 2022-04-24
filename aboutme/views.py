from django.shortcuts import render


def aboutme(request):
    template = 'aboutme/aboutme.html'
    context = {

    }
    return render(request, template, context)

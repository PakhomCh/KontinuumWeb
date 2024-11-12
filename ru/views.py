from django.shortcuts import render


def home(request):
    return render(request, 'ru/home.html', {})

def ascention(request):
    return render(request, 'ru/ascention.html', {})

def dynastika(request):
    return render(request, 'ru/dynastika.html', {})

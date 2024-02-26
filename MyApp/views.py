from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def furniture(request):
    return render(request, 'furniture.html')


def about(request):
    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')

from django.shortcuts import render


def landing(request):
    return render(request, "landing.html")

def features(request):
    return render(request, "features.html")

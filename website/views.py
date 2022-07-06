from django.shortcuts import render


def default(request):
    return render(request, "default.html")

def app(request):
    return render(request, "app.html")

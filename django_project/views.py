from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def image(request):
    return render(request, "image.html")


def memes(request):
    return render(request, "memes.html")


def quote(request):
    return render(request, "quote.html")


def text(request):
    return render(request, "text.html")

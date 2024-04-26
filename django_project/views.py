from django.shortcuts import render

from . import util


def index(request):
    return render(request, "index.html")


def image(request):
    return render(request, "image.html")


def memes(request):
    return render(request, "memes.html")


def quote(request):
    return render(request, "quote.html")


def text(request):
    text = util.generate_text()
    rendering = {"text": text}
    return render(request, "text.html", rendering)

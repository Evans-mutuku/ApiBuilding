from django.shortcuts import render

from . import util


def index(request):
    return render(request, "index.html")


def image(request):
    return render(request, "image.html")


def memes(request):
    memes = util.get_jokes()
    student = util.generate_students()
    rendering = {"memes": memes, "student": student}
    return render(request, "memes.html", rendering)


# quote just renders more info on quote.html
def quote(request):
    return render(request, "quote.html")


def text(request):
    text = util.generate_text()
    student = util.generate_students()
    rendering = {"text": text, "student": student}
    return render(request, "text.html", rendering)

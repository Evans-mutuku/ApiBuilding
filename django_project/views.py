from django.shortcuts import render

from . import util


def index(request):
    return render(request, "index.html")


def image(request):
    image = util.generate_images()
    rendering = {"image": image}
    return render(request, "image.html", rendering)


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

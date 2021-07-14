from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'coloring/index.html')

def home(request):
    return render(request, 'coloring/home.html')

def rec_easy(request):
    return render(request, 'coloring/rec_easy.html')

def rec_hard(request):
    return render(request, 'coloring/rec_hard.html')

def color_relaxed(request):
    return render(request, 'coloring/color_relaxed.html')

def color_creative(request):
    return render(request, 'coloring/color_creative.html')

def info(request):
    return render(request, 'coloring/info.html')

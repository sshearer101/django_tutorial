from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def newMethod(request):
    return HttpResponse("Our first app.")

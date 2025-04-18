from django.shortcuts import render

from django.http import HttpResponse


def catalog_view(request):
    return HttpResponse("каталог")
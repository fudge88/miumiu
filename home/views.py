from django.shortcuts import render
# from django.views.generic import TemplateView


def index(request):
    """ view to return index page"""
    return render(request, 'home/index.html')


def location(request):
    """ view for location/map"""
    return render(request, 'home/map.html')

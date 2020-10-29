from django.shortcuts import render
# from django.views.generic import TemplateView


def index(request):
    """ view to return index page"""
    bag = request.session.get('bag', {})
    bag_item = len(bag)

    context = {
        'bag_item': bag_item
    }
    return render(request, 'home/index.html', context)


def location(request):
    """ view for location/map"""
    bag = request.session.get('bag', {})
    bag_item = len(bag)

    context = {
        'bag_item': bag_item
    }
    return render(request, 'home/map.html', context)

from django.shortcuts import render

# Create your views here.


def shopping_bag(request):
    """ view to return the hsopping bag page"""
    return render(request, 'bag/bag.html')

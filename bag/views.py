from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

# Create your views here.


def shopping_bag(request):
    """ view to return the hsopping bag page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantiity of the chosen product to the bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))

def remove_item(request, item_id):
    """ Remove item from shopping bag"""

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
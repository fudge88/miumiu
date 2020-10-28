from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
from products.models import Product


def shopping_bag(request):
    """ renders shopping bag page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantiity of the chosen product to the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """Adjust the quantity of the specified product in the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_item(request, item_id):
    """ Removes item from shopping bag"""
    product = Product.objects.get(pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.info(request, (f'Removed {product.name} '
                                f'from your basket'))

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        print(f"ERROR: {e}")
        messages.error(request, f'Error removing item from your basket: {e}')
        return HttpResponse(status=500)

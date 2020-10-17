from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponse
import random

from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductReviewForm


# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    try:
        random_products_no = random.sample(range(0, len(products)), 4)
    except:
        random_products_no = random.sample(
            range(0, len(products)), len(products))
    print(random_products_no)
    random_products = []
    for r in random_products_no:
        random_products.append(products[r])

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'random_products': random_products
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        review = request.POST['review']
        # subject = request.POST['subject']
        product_review_obj = ProductReview(
            Product=product,
            User=request.user,
            review=review,
            # subject = subject
        )
        product_review_obj.save()
        print('saved')

    product_reviews = ProductReview.objects.filter(Product=product).order_by('-created_at')

    context = {
        'product': product,
        'product_reviews': product_reviews,
        'reviews_count': len(product_reviews)
    }
    print(product)

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


# PRODUCT REVIEWS
@login_required
def product_review(request, product_id):
    """ A view to show one product's details """
    if request.method == "POST":
        product = Product.objects.get(id=product_id)
        review = request.POST['review']
        product_review_obj = ProductReview(
            Product=product,
            User=request.user,
            review=review
        )
        product_review_obj.save()
        print('saved')

    product_reviews = ProductReview.objects.filter(pk=product_id).order_by('-created_at')
    print(product_reviews)
    review_form = ProductReviewForm()

    context = {
        'review_form': review_form,
        'product_reviews': product_reviews,
    }

    return render(request, 'products/product_detail.html', context)


def add_product_review(request, product_id):

    """
    Handles the POST request for review form. Saves the form and redirects
    to the product selected page
    """
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', context)

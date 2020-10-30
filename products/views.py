from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

from .models import Product, Category, ProductReview
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from .forms import ProductForm, ProductReviewForm


def all_products(request):
    """
    show all products, including sorting and search queries
    pulls random products from db for in-house promotion carousel
    """
    products = Product.objects.all()
    try:
        random_products_no = random.sample(range(0, len(products)), 12)
    except:
        random_products_no = random.sample(
            range(0, len(products)), len(products))

    random_products = []
    for r in random_products_no:
        random_products.append(products[r])

    query = None
    categories = None
    sort = None
    direction = None

# sorting options
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
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # pagination please see README.md for refernces
    post_list = products
    paginator = Paginator(post_list, 12)
    page = request.GET.get('page')

    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)

    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)

    bag = request.session.get('bag', {})
    bag_item = len(bag)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'random_products': random_products,
        'page': page,
        'posts': posts,
        'bag_item': bag_item
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    shows individual product details. Users who are authenticated
    filters through their orders if user has purchased more then 'none',
    the user is then able to write a review. Please see README.md
    for refernces, also had support fom tutors.
    """
    product = get_object_or_404(Product, pk=product_id)

    previous_order = False
    if request.user.is_authenticated:
        order_objs = Order.objects.filter(
            user_profile=UserProfile.objects.get(user=request.user)
            )

        for i in order_objs:
            p = OrderLineItem.objects.filter(product=product).filter(
                order=Order.objects.get(order_number=i.order_number))
            if len(p) > 0:
                previous_order = True
                break

    if request.method == 'POST':
        review = request.POST['review']
        product_review_obj = ProductReview(
            Product=product,
            User=request.user,
            review=review,
        )
        product_review_obj.save()

    product_reviews = ProductReview.objects.filter(
        Product=product).order_by('-created_at')

    bag = request.session.get('bag', {})
    bag_item = len(bag)

    context = {
        'product': product,
        'product_reviews': product_reviews,
        'reviews_count': len(product_reviews),
        'previous_order': previous_order,
        'bag_item': bag_item
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Adding a product to the store only superuser/admin can do this,
    all other users would be redirected back to home.
    """
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
            messages.error(
                request, 'Failed to add product. Check the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    editing a product to the store only superuser/admin can do this,
    all other users would be redirected back to home.
    """
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
            messages.error(
                request, 'Failed to update product. Check the form is valid.'
                )
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
    """
    deleting a product to the store only superuser/admin can do this,
    all other users would be redirected back to home.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def product_review(request, product_id):
    """
    product reviews are filtered to that specific product_id,
    written myself using guides, please see README.md for references
    """
    product_reviews = ProductReview.objects.filter(
        pk=product_id).order_by('-created_at')
    review_form = ProductReviewForm()

    context = {
        'review_form': review_form,
        'product_reviews': product_reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product_review(request, product_id):
    """
    product reviews are added to that specific product_id,
    written myself using guides, please see README.md for references
    """
    product = get_object_or_404(Product, pk=product_id)
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

    return render(request, 'products/product_detail.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from django.db.models import Q
from django.contrib import messages

# View for the home page


def home_page(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

# View for listing all products


def product_list(request):
    products = Product.objects.all().order_by('product_id')
    return render(request, 'products/products_list.html', {'products': products})

# View for displaying product details


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/products_details.html', {'product': product})

# View for submitting a review


def submit_review(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        review_text = request.POST.get('review')

        if review_text and review_text.strip():  # Checking for non-empty review
            Review.objects.create(product=product, review_text=review_text)
        else:
            # Display a warning message if review is blank
            messages.warning(request, "Review cannot be blank.")

    return redirect('products:product_details', product_id=product_id)

# View for searching products by name


def search_products(request):
    query = request.GET.get('query')

    if query and len(query) >= 3:
        products = Product.objects.filter(Q(product_name__icontains=query))
        return render(request, 'products/search_page.html', {'products': products, 'query': query})
    else:
        alert_message = "Please enter at least three characters."
        messages.warning(request, alert_message)
        return redirect(request.META.get('HTTP_REFERER'))

# View for searching products by type


def product_type_search(request, product_type):
    products = Product.objects.filter(product_type=product_type)
    return render(request, 'products/product_type_search.html', {'products': products, 'query': product_type})

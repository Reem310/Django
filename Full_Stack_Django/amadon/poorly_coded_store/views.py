from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Order, Product


def index(request):
    context = {
        "all_products": Product.objects.all(),
    }
    return render(request, "store/index.html", context)


def total(request):
    if request.method == 'POST':
        quantity_from_form = int(request.POST["quantity"])
        product = Product.objects.get(id=request.POST["product_id"])
        price_from_form = float(product.price)
        total_charge = quantity_from_form * price_from_form
        request.session['total_charge'] = total_charge
        request.session['total_items'] += quantity_from_form
        request.session['total_spent'] += total_charge
        print("Charging credit card...")
        order = Order.objects.create(
            quantity_ordered=quantity_from_form,
            total_price=total_charge,
        )
        order.save()
        return redirect(f'/checkout')
    else:
        return redirect('/')


def checkout(request):
    context = {
        "total_charge": request.session['total_charge'],
        "total_items": request.session['total_items'],
        "total_spent": request.session['total_spent'],
    }
    return render(request, "store/checkout.html", context)

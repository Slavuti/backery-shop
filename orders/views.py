from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Order
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# payments view added 5
def create_checkout_session(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': f'Order #{order.id}',
                },
                'unit_amount': int(order.total_price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/orders/success/',
        cancel_url='http://127.0.0.1:8000/orders/cancel/',
    )

    order.stripe_payment_intent = session.id
    order.save()

    return redirect(session.url, code=303)

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')
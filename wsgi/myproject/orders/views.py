from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
#from .tasks import order_created
from cart.cart import Cart


# it takes the request of the Card app and check the request method with POST and calls the order form
# it the form is valid and it saves form and then for loops in the cart to create order items and sends the request to the created.html page
# else ordercreateform and sends to create.html with cart and form

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            #order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})

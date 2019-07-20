from django.shortcuts import render, get_object_or_404
from .models import Order,OrderItem
from django.contrib.auth.decorators import login_required
from operator import attrgetter
def thanks (request, order_id):
	if order_id:
		customer_order = get_object_or_404 (Order, id=order_id)
		
		
	return render (request,'thanks.html', {'customer_order':customer_order})	


@login_required()
def orderHistory(request):
	if request.user.is_authenticated:
		print(str(request.user))
		email = str(request.user.email)
		order_details = Order.objects.filter(emailAddress=email)
		return render(request, 'order/orders_list.html', {'order_details':order_details})

@login_required()
def viewOrder(request,order_id):
	if request.user.is_authenticated:
		email = str(request.user.email)
		order = Order.objects.get(id=order_id, emailAddress=email)
		order_items = OrderItem.objects.filter(order=order)
		order_items = sorted(order_items, key=attrgetter('slot'))
		total_before=0
		for item in order_items:
			if item.ride == True:
				item.price = item.product.price+15
			total_before+=item.price

		return render (request, 'order/order_detail.html',{'order':order,'order_items':order_items,'total_before':total_before })		
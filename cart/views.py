from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Product
from .models import Cart, CartItem,Coupon
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from django.http import HttpResponse
from datetime import datetime
from order.models import Order,OrderItem
from django.contrib.auth.models import User


def _cart_id (request) :
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart

def add_cart (request , product_id,**kwargs):

	
	product = Product.objects.get(id=product_id)
	try:
		cart = Cart.objects.get (cart_id = _cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
			cart_id = _cart_id(request))
		cart.save()

	
	cart_item = CartItem.objects.create(
		product=product,
		slot = request.session['slot'],
		cart = cart ,
		total = product.price
			)
	
	try: cart_item.location = request.user.profile.location
	except:
		cart_item.location= request.session['location']
	finally:pass		
	cart_item.save()

	return redirect ("cart:cart_detail")


def cart_detail (request, total = 0 , counter = 0, cart_items = None,carid=None):

	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter (cart= cart, active=True)
		if carid != None:
			item = CartItem.objects.get(id=carid)
			item.ride = not item.ride
			if item.ride == True:
				item.total += 15
				item.save()
			else:
				item.total = item.product.price
				item.save()
			if 'stripe_total' in request.session:
				del request.session['stripe_total']
			return redirect('cart:cart_detail')
				
		location = request.session.get('location')
		if location:
			itemid = request.session.get('itemid') #From location.view
			if itemid:
				itm = CartItem.objects.get( id = itemid)
				itm.location = location
				itm.save()
				del request.session['location']
				del request.session['itemid']
			else:
				for itm in cart_items:
					itm.location = request.session['location']
					itm.save()
				 
		
		for item in cart_items:
			total += item.total	
	
	except ObjectDoesNotExist:
		pass

	

	stripe.api_key = settings.STRIPE_SECRET_KEY
	
	stripe_total = int(total*100)

	if 'stripe_total' in request.session:
		stripe_total = request.session['stripe_total']
		total = format((float(stripe_total)/100),'.2f')
		

   		
		

	description = 'GGAcademy - New Order'
	data_key = settings.STRIPE_PUBLISHABLE_KEY
	if request.method == 'POST':
	
		if 'coupon' in request.POST:
			
			if 'stripe_total' in request.session:
				del request.session['stripe_total']
				
				
			try:
				test=Coupon.objects.get(code = request.POST['coupon'])

				stripe_total=0
				for cart_item in  cart_items:
					stripe_total += (int((cart_item.total)) *(100-test.discount))

	
				
				request.session['stripe_total'] = stripe_total

				return redirect('cart:cart_detail')
			except ObjectDoesNotExist:	
				pass

		else:
			
			try:
				token = request.POST ['stripeToken']
				email = request.POST ['stripeEmail']
				billingName= request.POST['stripeBillingName']
				billingAddress1 = request.POST['stripeBillingAddressLine1']
				billingcity = request.POST ['stripeBillingAddressCity']
				billingPostcode = request.POST ['stripeBillingAddressZip']
				customer = stripe.Customer.create(
					 email = email,
					 source = token)
				charge = stripe.Charge.create (
					amount = stripe_total,
					currency = 'usd',
					description = description,
					customer= customer.id)
				del request.session['stripe_total']
			

				try:
					order_details = Order.objects.create(
						token = token,
						total = total,
						emailAddress = email,
						description = description,
						billingAddress1=  billingAddress1,
						billingCity = billingcity,
						billingPostcode = billingPostcode,
						)


					order_details.save()

					for order_item in cart_items:
						oi=OrderItem.objects.create(
							product = Product.objects.get(id=order_item.product.id),
							price = order_item.product.price,
							order = order_details,
							slot=order_item.slot,
							quantity=1,
							location = order_item.location,
							ride = order_item.ride
							)
						oi.save()
						order_item.delete()

						
					return redirect('order:thanks',order_details.id)
				

				except ObjectDoesNotExist:
					pass


			except stripe.error.CardError as e:
				return False,e

			
				

	return render (request, 'cart.html', dict(cart_items = cart_items, total = total , counter = counter,
											 data_key=data_key, stripe_total= stripe_total, description=description),)




def cart_remove (request,product_id,slot):
	if 'stripe_total' in request.session:
		del request.session['stripe_total']

	cart = Cart.objects.get(cart_id=_cart_id (request))
	product = get_object_or_404(Product, id=product_id)
	cart_item=CartItem.objects.filter(product=product,cart=cart,slot=slot)
	#if cart_item.quantity >1:
	#	cart_item.quantity-=1
	#	cart_item.save()
	#else:
	cart_item.delete()
	return redirect('cart:cart_detail')	
	#return redirect ("location:map")
	
def full_remove (request,product_id):
	cart = Cart.objects.get(cart_id=_cart_id (request))
	product = get_object_or_404(Product, id=product_id)
	cart_item=CartItem.objects.get(product=product,cart=cart)
	cart_item.delete()
	return redirect('cart:cart_detail')	






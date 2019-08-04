from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.contrib.auth.models import Group,User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from datetime import datetime as dt
from .scheduling import *
from order.models import Order,OrderItem
from cart.models import CartItem
from .mailgun import welcome_message
import requests


def index (request):
	
	currentMonth = dt.now().month
	
	x =   currentMonth 
	return HttpResponse (x)

#Category view

def allProdCat(request, c_slug=None):
	cart_items = CartItem.objects.all()
	for cart_item in cart_items:
		now = dt.now()
		duration=(now - cart_item.created)
		if duration.seconds > 1200:
			cart_item.delete()
	
	c_page = None
	Products = None
	if c_slug!=None:
		c_page= get_object_or_404 (Category,slug=c_slug)
		products= Product.objects.filter (category=c_page, available = True)

	else: 
		products = Product.objects.all().filter(available=True)

	return render (request, 'shop/category.html', {'category':c_page ,'products':products,'month_today':month_today,'day_today':day_today})



def ProdCatDetail (request,c_slug,product_slug,month,day,year=year_today):
	if 'stripe_total' in request.session:
		del request.session['stripe_total']
	orders = OrderItem.objects.filter(slot__startswith=year+"-"+month+"-"+str(day))
	strday = str(day)
	if day<10:
		strday = "0"+strday #quick fix
	
	carts = CartItem.objects.filter(slot__startswith=year+"-"+month+"-"+strday)
	dborders=[] # database orders 
	
	for o in orders:
		x= str(o.slot)
		dborders.append(x[11:13])

	for c in carts:
		x= str(c.slot)
		dborders.append(x[11:13])
	

	slots = {'14':'2pm',
	'15':'3pm' ,
	'16':'4pm',
	"17":'5pm',
	'18':'6pm',
	
	}

		

	monthname = month_name(month) #June

	month_days=monthdays(int(year),int(month))

	previous_month = str(int(month)-1)
	if len(previous_month)==1:
		previous_month="0"+previous_month
	nextmonth = str(int(month)+1)
	if len(nextmonth)==1:
		nextmonth="0"+nextmonth

	nextmonth_today = "0"+str(int(month_today)+1)

	tday = int(day_today)

	if (int(month) > int(month_today) and day in month_days) or (int(month)==int(month_today) and day>= int(day_today)):
		try:
			product=Product.objects.get(category__slug=c_slug,slug=product_slug)


		except Exception as e:
			raise e

	if request.method == 'POST':
		a=request.POST['slot']
		request.session['slot'] = year+  "-" + month+ "-"+str(day)+" "+ a+":00:00"
		
		return redirect ("cart:add_cart",product_id=product.id)
		
	return render(request,'shop/product.html',{'product':product,'monthname':monthname,'month_days':month_days, 'year':year,
		 										'month':month,'day':day,
		 										'tday':tday, 'month_today':month_today,'dborders':dborders,'slots':slots,
		 										"previous_month":previous_month, "nextmonth":nextmonth,
		 										"nextmonth_today":nextmonth_today})


def signupView (request):
	
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			a = form.cleaned_data
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			signup_user = User.objects.get(username=username,email=email)
			signup_user.profile.phone = form.cleaned_data.get('phone')
			signup_user.profile.pickup = form.cleaned_data.get('pickup')
			signup_user.save()
			customer_group = Group.objects.get (name='Customer')
			customer_group.user_set.add(signup_user)
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			welcome_message(email)

			
			
			
	else:
		form = SignUpForm()


	return  render (request, 'accounts/signup.html', {'form':form, })

def signinView (request):
	if request.method == 'POST':
		form = AuthenticationForm(data= request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password=password)
			if user is not None:
				login(request, user)
				return redirect('shop:allProdCat')
			else:
				return redirect ('signup')
	else:
		form = AuthenticationForm()
	return render (request,'accounts/signin.html',{'form':form})

def signoutView (request):
	logout(request)
	return redirect ('shop:allProdCat')

def profile (request):
	current_user = request.user
	phone =str(current_user.profile.phone)
	phone1= phone[0:3]
	phone2= phone[3:6]
	phone3= phone[6:]
	
	if request.method =='POST':
		print(request.POST)
		
		
		try:
			current_user.profile.phone = request.POST['phone1']+request.POST['phone2']+request.POST['phone3']
			current_user.save()
		except:
			pass
		try:
			current_user.profile.pickup = request.POST['pickup']
			current_user.save()
		except:
			pass
		return redirect('profile')
		
	return render (request,'accounts/profile.html',{'phone1':phone1,'phone2':phone2,'phone3':phone3})
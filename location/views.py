from django.shortcuts import render,redirect,get_object_or_404
from .models import locations
from operator import attrgetter
from math import sqrt
from enum import Enum
from pprint import pprint
import requests
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def map (request,itemid=None) :
	location_items = locations.objects.all()
	longitude="-115.19775"
	latitude="36.159545099999996"

	request.session['itemid'] = itemid


	if request.method == 'POST':
		if 'coord' in request.POST:
			a= (request.POST['coord'])
			i = a.split(':')
			longitude=i[1][0:10]
			latitude=i[2][0:9]
			
		else:
			a=request.POST['location']
			loc = locations.objects.get(id=a)
			request.session['location'] = loc.name
			if request.user.is_authenticated and itemid == None:
				current_user = request.user
				current_user.profile.location = loc.name
				current_user.save()
			return redirect ("cart:cart_detail")
	
		
		
	

	geolocation_URL = latitude+","+longitude
	place_id_URL=""
	for loc in location_items:
		place_id_URL+="place_id:"+loc.place_id+"|" #fetch from db

	

	r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+geolocation_URL+'&destinations='+place_id_URL+'&key=AIzaSyBXVueb1n7WXzPrhAttY3K6Qg2kQG3iMU4')
	j = r.json()
	k = j['rows'][0]['elements'][0]['distance']
	x=0  
	print(k)
	
	for loc in location_items:
		
		try:		
			a=float(j['rows'][0]['elements'][x]['distance']['text'][0:3])
			loc.distance=a
		except:
			pass
		x+=1

	sorted_list = sorted(location_items, key=attrgetter('distance'))
	
	return render(request,'location.html',{'sorted_list':sorted_list,'longitude':longitude})

# Create your views here.

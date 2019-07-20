from django.db import models
from shop.models import Product

class Cart (models.Model):
	cart_id = models.CharField(max_length = 250,blank=True)
	date_added = models.DateField(auto_now_add=True)
	class Meta:
		db_table = 'Cart'
		ordering = ['date_added']

	def __str__(self):
		return self.cart_id

class CartItem (models.Model):
	product= models.ForeignKey(Product, on_delete=models.CASCADE)
	cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
	active = models.BooleanField(default=True)
	slot=models.DateTimeField ( unique =True )
	created = models.DateTimeField(auto_now_add=True)
	location = models.CharField(max_length = 250,blank=True)
	ride = models.BooleanField(default=False)
	total = models.DecimalField(max_digits=10,decimal_places=2)
	class Meta:
		db_table= 'CartItem'

	def sub_total(self):
		return self.product.price 

	def __str__(self):
		return self.product

class Coupon (models.Model):
	code = models.CharField(max_length=10,unique = True,)
	discount = models.IntegerField()
	class Meta:
		db_table= 'Coupon'

	def __str__(self):
		return self.code
	def __int__(self):
		return self.discount


from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
	model = OrderItem
	fieldsets = [
	('Product',{'fields':['product'],}),
	('Quantity',{'fields':['quantity'],}),
	('Price',{'fields':['price'],}),
	('Slot',{'fields':['slot'],}),
	]

	readonly_fields = ['product','quantity','price','slot']
	can_delete = False
	max_num = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','billingName','emailAddress','created']
	list_display_links = ('id','billingName')
	search_fields = ['id','billingName','emailAddress']
	readonly_fields=['id','token','total','emailAddress','created',]

	fieldsets= [
	('Order Information', {'fields': ['id','token','created']}),
	('billing Information', {'fields':['billingName','billingAddress1','emailAddress']}),
	('Shipping information', {'fields':['shippingName']}),
	]
	inlines = [
		OrderItemAdmin
	]

	def has_delete_permission(self,request,obj=None):
		return False

	def has_add_permission (self,request):
		return False

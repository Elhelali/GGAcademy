from django.db import models
from shop.models import Product
# Create your models here.
class Order(models.Model):
    token = models.CharField(max_length=250, blank = True)
    total = models.DecimalField(max_digits=10,decimal_places=2,verbose_name= 'USD Order Total')
    emailAddress = models.EmailField(max_length = 250, blank= True, verbose_name='Email Address')
    created = models.DateTimeField (auto_now_add = True)
    billingName = models.CharField(max_length=250, blank= True)
    billingAddress1 = models.CharField(max_length=250,blank = True)
    billingCity = models.CharField(max_length=250, blank = True)
    billingPostcode = models.CharField(max_length=10 , blank = True)
    billingCountry= models.CharField(max_length=200, blank = True)
    shippingName= models.CharField(max_length=250, blank = True)
    shippingCity= models.CharField(max_length=250, blank = True)
    shippingPostcode= models.CharField(max_length=10, blank = True)
    shippingCountry = models.CharField (max_length=200, blank=True)
    description=models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__ (self):
        return str(self.id)

class OrderItem(models.Model):
    product= models.ForeignKey(Product,on_delete=None)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField (max_digits=10, decimal_places=2, verbose_name= 'USD Price')
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    slot = models.DateTimeField(null = True, unique = True)
    location = models.CharField(max_length = 250,default="Not Set")
    ride = models.BooleanField(default=False)
    class Meta :
        db_table = 'OrderItem'

    def sub_total (self):
            return self.quantity * self.price

    def __str__(self):
            return self.product
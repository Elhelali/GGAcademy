from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

class Category (models.Model):
	name = models.CharField(max_length=250,unique=True)
	slug = models.SlugField(max_length=250,unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category',blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	def get_url (self):
		return reverse ('shop:products_by_category',args=[self.slug])

	def __str__(self):
		return '{}'.format(self.name)

class Product(models.Model):
	name = models.CharField(max_length=250,unique=True)
	slug = models.CharField(max_length=250,unique=True)
	description = models.TextField(blank=True)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	image = models.ImageField(upload_to='product',blank=True)
	available=models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)

	class Meta:
			ordering=('name',)
			verbose_name='product'
			verbose_name_plural='products'
	def get_url(self):
		return reverse('shop:ProdCatDetail',args=[self.category.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=13, blank=False, )
    pickup = models.CharField(max_length=100, blank=True)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

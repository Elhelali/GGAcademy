from django.db import models

# Create your models here.
#class location(models.Model):
 #   user = models.ForeignKey(Order,on_delete = models.CASCADE)
  #  class Meta:
   #     db_table = 'Order'
    #    ordering = ['-created']

    #def __str__ (self):
     #   return str(self.id)

class locations(models.Model):
	name = models.CharField(max_length=250, default='none')
	address = models.CharField(max_length=250)
	longitude = models.FloatField ()
	latitude = models.FloatField ()
	distance = models.FloatField()
	place_id= models.CharField(max_length=250, default='none')

	class Meta:
		db_table = 'locations'
		ordering = ['longitude']

	def __str__ (self):
		return str(self.address)
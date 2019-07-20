from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=250, default='none')
    slug = models.SlugField(max_length=250,)
    pub_date = models.DateField(auto_now_add = True)



    class Meta:
	    db_table = 'Posts'
	    ordering = ['pub_date']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    def get_url (self):
        return reverse ('blog:post',args=[self.slug])
    def __str__ (self):
        return str(self.title)


class Topic (models.Model):
    title = models.CharField(max_length=250, default='none')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    number = models.IntegerField()
    text = models.CharField(max_length=5000,default = "article topic goes here")

    class Meta:
	    db_table = 'Topic'
	    ordering = ['post','number']

class Subtopic (models.Model):
    title = models.CharField(max_length=250, default='none')
    topic = models.ForeignKey(Topic,related_name='Subtopic', on_delete=models.CASCADE)
    number = models.IntegerField()
    text = models.CharField(max_length=5000,default = "article subtopic goes here")
    
    class Meta:
	    db_table = 'Subtopic'
	    ordering = ['topic','number']
from django.contrib import admin
from .models import Post,Topic,Subtopic
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display= ['title','pub_date']
	prepoulated_fields= {'slug':('title',)}
	list_per_page= 20
admin.site.register(Post,PostAdmin)

class TopicAdmin(admin.ModelAdmin):
	list_display= ['title','post','number','text']
	list_per_page= 20
admin.site.register(Topic,TopicAdmin)

class SubtopicAdmin(admin.ModelAdmin):
	list_display= ['title','topic','number','text']
	list_per_page= 20
admin.site.register(Subtopic,SubtopicAdmin)

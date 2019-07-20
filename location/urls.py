from django.urls import path
from . import views
app_name = 'location'


urlpatterns= [
path('',views.map, name='map'),
path('<itemid>',views.map,)]

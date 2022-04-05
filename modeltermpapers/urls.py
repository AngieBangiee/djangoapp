from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'modeltermpapers'

urlpatterns = [ 
    path('', views.home, name='home'), 
    #path('', views.prices, name='prices'),
    url(r'^(?P<name>\b[A-Za-z]\w+\b)/$', views.prices, name="prices"),
    
] 


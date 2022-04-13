from django.urls import path
from django.conf.urls import url
from . import views 

app_name = 'modeltermpapers'

urlpatterns = [ 
    path('', views.home, name='home'), 
    url('prices/', views.prices, name='prices'),
    url('about/', views.about, name='about'), 
    url('services/', views.services, name='services'),
    url('guarantees/', views.guarantees, name='guarantees'),
    url('custom-term-papers/', views.termpapers, name='termpapers'), 
    url('order/', views.order, name='order'),
] 
 
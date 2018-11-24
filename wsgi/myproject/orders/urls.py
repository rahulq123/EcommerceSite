from django.conf.urls import url
from . import views

# url takes to the views.order_create page

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
]

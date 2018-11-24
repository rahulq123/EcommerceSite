from django.conf.urls import url
from . import views


# the following url are linked with the views to direct user to the specific page when browsing the ecommerce site
# also it check the url with logcheckuser adn regcheckuser to verify the user data against the database
              
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^shop/$', views.product_list, name='product_list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    # Ajax: check if user exists on registration page
    url(r'^regcheckuser/$', views.regCheckUser, name='regCheckUser'),
    # Ajax: check if user exists on login page
    url(r'^logcheckuser/$', views.logCheckUser, name='logCheckUser'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]
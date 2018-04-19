from django.conf.urls import url,include
from superuser import views

urlpatterns = [
    url(r'^contactform/$',views.contactform ,name='contactform'),
    url(r'^superuserprofile/(?P<su_id>\w{0,50})$',views.superuserprofile, name= 'superuserprofile'),
]
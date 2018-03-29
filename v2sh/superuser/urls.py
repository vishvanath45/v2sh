from django.conf.urls import url,include
from superuser import views

urlpatterns = [
    url(r'^contactform/$',views.contactform ,name='contactform'),
    url(r'^superuserprofile/$',views.superuserprofile, name= 'superuserprofile'),
]
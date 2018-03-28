from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.home , name= 'home'),
    url(r'^aboutus/$', views.aboutus , name= 'aboutus'),
    url(r'^reportissue/$', views.reportissue , name= 'reportissue'),
    url(r'^authenticate/$',views.authenticate , name= 'authenticate'),
    url(r'^contactform/$',views.conactform ,name='contactform'),
]

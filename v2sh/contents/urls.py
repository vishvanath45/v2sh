from django.conf.urls import url,include
from contents import views

urlpatterns = [
    url(r'^aboutus/$', views.aboutus , name= 'aboutus'),
    url(r'^reportissue/$', views.reportissue , name= 'reportissue'),
    url(r'^feedbackform/$',views.feedbackform, name= 'feedbackform'),
    url(r'^ourmission/$',views.ourmission, name= 'ourmission'),
]

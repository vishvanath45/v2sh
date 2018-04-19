from django.conf.urls import url,include
from contents import views


urlpatterns = [
    url(r'^aboutus/$', views.aboutus , name= 'aboutus'),
    url(r'^reportissue/$', views.reportissue , name= 'reportissue'),
    url(r'^feedbackform/$',views.feedbackform, name= 'feedbackform'),
    url(r'^ourmission/$',views.ourmission, name= 'ourmission'),
    url(r'^byyear/(?P<beta>\w{0,50})$',views.byyear, name= 'byyear'),
    url(r'^byname/(?P<gamma>\w{0,50})$',views.byname, name= 'byname'),
    url(r'^bycompany/(?P<alpha>[^\n]+)$',views.bycompany,name = "bycompany"),
    url(r'^company/(?P<name>[^\n]+)$', views.company, name="company")
]

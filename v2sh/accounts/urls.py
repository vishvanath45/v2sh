from django.conf.urls import url,include
from accounts import views
urlpatterns = [
    url(r'^register/',views.signup ,name='signup'),
    url(r'^activate/(?P<key>.+)$', views.activation,name = 'activation'),
    url(r'^login/',views.login ,name='login'),
]

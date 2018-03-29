from django.conf.urls import url,include
from accounts import views

urlpatterns = [
    url(r'^authenticate/',views.authenticate ,name='authenticate'),
]
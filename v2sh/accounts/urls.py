from django.conf.urls import url,include
from accounts import views
urlpatterns = [
    url(r'^register/',views.signup ,name='signup'),
    url(r'^login/',views.login ,name='login'),
]

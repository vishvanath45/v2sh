from django.conf.urls import url,include
from accounts import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # url(r'^authenticate/',views.authenticate ,name='authenticate'),
    url(r'^register/',views.signup ,name='signup'),
    # url(r'^login/',views.login ,name='login'),
    # url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
"""v2sh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from contents import views
from superuser import views as sp
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^superuser/', include('superuser.urls')),
    url(r'^contents/', include('contents.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'' , sp.error , name = 'error'),
    # url(r'^dynamic_forms/$',include('dynamic_forms.urls', namespace='dynamic_forms')),
]

urlpatterns += staticfiles_urlpatterns()


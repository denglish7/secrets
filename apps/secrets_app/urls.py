from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logoff/$', views.logoff, name='logoff'),
    url(r'^new/$', views.logoff, name='logoff'),
]

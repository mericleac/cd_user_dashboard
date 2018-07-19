from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'process_login$', views.process_login),
    url(r'login$', views.login),
    url(r'process_register$', views.process_register),
    url(r'register$', views.register),
    url(r'$', views.index)
]
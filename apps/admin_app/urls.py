from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dashboard$', views.admin_dashboard),
    url(r'(?P<user_id>\d+)/process_edit$', views.process_edit),
    url(r'(?P<user_id>\d+)/edit$', views.admin_edit),
    url(r'process_add$', views.process_add),
    url(r'add$', views.add),
    url(r'(?P<user_id>\d+)/delete$', views.delete),
]
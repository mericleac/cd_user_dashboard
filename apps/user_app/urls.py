from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'/dashboard$', views.user_dashboard),
    url(r'(?P<user_id>\d+)/show$', views.show),
    url(r'(?P<user_id>\d+)/create_message$', views.create_message),
    url(r'(?P<user_id>\d+)/(?P<message_id>\d+)/create_comment', views.create_comment),
    url(r'process_edit$', views.process_edit),
    url(r'(?P<user_id>\d+)/edit$', views.edit),
    url(r'(?P<user_id>\d+)/(?P<message_id>\d+)/delete_message', views.delete_message),
    url(r'(?P<user_id>\d+)/(?P<comment_id>\d+)/delete_comment', views.delete_comment),
]
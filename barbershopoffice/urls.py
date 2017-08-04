from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_app, name='main_app'),
    url(r'orders/$', views.orders, name='orders'),
    url(r'dicts/$', views.dicts, name='dicts'),
    url(r'dicts/services/$', views.dict_services_list, name='dict_services_list'),
    url(r'dicts/clients/$', views.dict_clients_list, name='dict_clients_list'),
]
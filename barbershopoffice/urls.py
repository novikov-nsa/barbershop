from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_app, name='main_app'),
    url(r'orders/$', views.orders, name='orders'),
    url(r'orders/(?P<order_id>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'dicts/$', views.dicts, name='dicts'),
    url(r'dicts/services/$', views.dict_services_list, name='dict_services_list'),
    url(r'dicts/clients/$', views.dict_clients_list, name='dict_clients_list'),
    url(r'dicts/clients/(?P<client_id>[0-9]+)/$', views.dict_clients_detail, name='dict_clients_detail'),
]
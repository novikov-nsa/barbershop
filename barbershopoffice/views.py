from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import Http404

from .models import Orders, OrdersDetail, DictServices, DictClients

# Create your views here.
def main_app(request):
    latest_order = Orders.objects.order_by('-numberOrder')[:5]
    context = {'latest_order': latest_order}
    return render(request, 'main.html', context)

def dicts(request):
    return render(request, 'dicts/index.html')

def dict_services_list(request):
    latest_dicts_services = DictServices.objects.order_by('-codeService')[:5]
    context = {'latest_dicts_services': latest_dicts_services}
    return render(request, 'dicts/services.html', context)

def dict_clients_list(request):
    latest_dicts_clients = DictClients.objects.order_by('-codeClient')
    context = {'latest_dicts_clients': latest_dicts_clients}
    return render(request, 'dicts/clients.html', context)

def dict_clients_detail(request, client_id):
    try:
        client = DictClients.objects.get(pk=client_id)
    except DictClients.DoesNotExist:
        raise Http404("Запись справочника Клиенты не найдена")
    return render(request,'dicts/clients_detail.html', {'client': client})

def orders(request):
    latest_order = Orders.objects.order_by('-numberOrder')
    context = {'latest_order': latest_order}
    return render(request, 'orders.html', context)

def order_detail(request, order_id):
    try:
        order = Orders.objects.get(pk=order_id)
    except Orders.DoesNotExist:
        raise Http404("Запись заказа не найдена")
    return render(request, 'order_detail_edit.html', {'order': order})

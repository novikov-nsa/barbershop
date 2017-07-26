from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader

from .models import Orders, OrdersDetail, DictServices, DictClients

# Create your views here.

def orders(request):
    latest_order = Orders.objects.order_by('-numberOrder')[:5]
    context = {'latest_order': latest_order}
    return render(request, 'orders.html', context)

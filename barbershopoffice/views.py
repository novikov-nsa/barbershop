from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Orders, OrdersDetail, DictServices, DictClients

# Create your views here.

def orders(request):
    latest_order = Orders.objects.order_by('-numberOrder')[:5]
    output = ', '.join([q.numberOrder for q in latest_order])
    return HttpResponse(output)

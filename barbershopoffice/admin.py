from django.contrib import admin

# Register your models here.

from .models import DictServices, DictClients, Orders, OrdersDetail

admin.site.register(DictClients)
admin.site.register(DictServices)
admin.site.register(Orders)
admin.site.register(OrdersDetail)

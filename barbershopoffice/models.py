from django.db import models

# Create your models here.

class DictServices(models.Model):
    codeService = models.CharField(max_length=20)
    nameService = models.CharField(max_length=255)

class DictClients(models.Model):
    codeClient = models.CharField(max_length=20)
    nameClient = models.CharField(max_length=255)


class Orders(models.Model):
    """ Класс Orders - заказы клиентов

    numberOrder = номер заказа
    codeClient = код клиента
    nameClient = наименование клиента
    dateOrder = дата заказа
    codeOfService = код услуги

    """
    numberOrder = models.CharField(max_length=20)
    client = models.ForeignKey(DictClients, on_delete=models.CASCADE)
    dateOrder = models.DateField()


class OrdersDetail(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    service = models.ForeignKey(DictServices, on_delete=models.CASCADE)
    costOfService = models.DecimalField(max_digits=20, decimal_places=2)


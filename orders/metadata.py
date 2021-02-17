from django.db import models


class OrderStatuses(models.IntegerChoices):
    NEW = 0, 'Новый'
    READY = 1, 'Готов'
    DELIVERED = 2, 'Доставлен'
    CANCELED = 3, 'Отменен'
    __empty__ = '(Не известно)'

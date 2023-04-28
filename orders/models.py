from functools import lru_cache

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django_jsonform.models.fields import JSONField


@lru_cache
def order_content_schema() -> dict:
    schema = {
        "type": "array",
        "title": "Товары",
        "items": {
            "type": "object",
            "properties": {
                "product": {
                    "type": "string",
                    "title": "Наименование"
                },
                "quantity": {
                    "type": "number",
                    "title": "Количество"
                },
                "price": {
                    "type": "integer",
                    "title": "Цена"
                },
                "amount": {
                    "type": "integer",
                    "title": "Сумма"
                }
            }
        }
    }
    return schema


class OrderStatuses(models.IntegerChoices):
    NEW = 0, 'Распределение'
    READY = 1, 'Готов'
    DELIVERED = 2, 'Доставлен'
    CANCELED = 3, 'Отменен'
    __empty__ = '(Не известно)'


class OrderPartner(models.Model):
    # region Fields:...
    partner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Участник',
    )
    order = models.ForeignKey(
        'orders.Order',
        related_name='items',
        on_delete=models.CASCADE
    )
    debit = models.DecimalField(
        verbose_name='Внесено',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    credit = models.DecimalField(
        verbose_name='К внесению',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    # endregion

    class Meta:
        verbose_name = 'Участник заказа'
        verbose_name_plural = 'Участники заказа'
        unique_together = [('partner', 'order')]

    def __str__(self):
        title = f"{self.partner.first_name} {self.partner.last_name}"

        return title


class Order(models.Model):
    objects = models.Manager()

    # region Fields:...
    id = models.AutoField(
        verbose_name='Номер',
        primary_key=True
    )
    date = models.DateTimeField(
        verbose_name='Дата',
        default=timezone.now
    )
    created_at = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Изменено',
        auto_now=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Пометка удаления',
        default=False
    )
    status = models.IntegerField(
        verbose_name='Статус',
        choices=OrderStatuses.choices,
        default=0,
    )
    amount = models.DecimalField(
        verbose_name='Сумма',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    debit = models.DecimalField(
        verbose_name='Внесено',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    opening_balance = models.DecimalField(
        verbose_name='Начальный остаток',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    final_balance = models.DecimalField(
        verbose_name='Конечный остаток',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    partners = models.ManyToManyField(
        User,
        verbose_name='Участники',
        through=OrderPartner,
    )
    previous_order = models.OneToOneField(
        'Order',
        verbose_name='Предыдущий заказ',
        blank=True,
        null=True,
        default=objects.last,
        on_delete=models.SET_NULL,
    )
    content = JSONField(
        verbose_name='Содержание',
        help_text='Список товаров заказа',
        blank=True,
        default=list,
        schema=order_content_schema,
    )
    # endregion

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date']

    def __str__(self):
        date = self.date.strftime('%d.%m.%Y %H:%M:%S')
        result = f"Заказ №{self.id} от {date}"

        return result

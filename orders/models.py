from django.db import models
from django.utils import timezone

from orders.metadata import OrderStatuses
from django.contrib.auth.models import User


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
        db_table = 'order_partners'
        verbose_name = 'Участник заказа'
        verbose_name_plural = 'Участники заказа'
        unique_together = [('partner', 'order')]

    def __str__(self):
        title = f"{self.partner.first_name} {self.partner.last_name}"

        return title


class Order(models.Model):
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
        on_delete=models.SET_NULL,
    )
    content = models.TextField(
        verbose_name='Содержимое',
        blank=True,
        default="",
    )
    # endregion

    @property
    def representation(self):
        date = self.date.strftime('%d.%m.%Y %H:%M:%S')
        representation = f"Заказ №{self.id} от {date}"

        return representation

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date']

    def __str__(self):
        return self.representation

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == OrderStatuses.NEW and not self.is_deleted:
            self.calculate_partners()
            super().save(*args, **kwargs)

    def calculate_partners(self):
        prev_order = self.previous_order
        partners = OrderPartner.objects.filter(order=self)
        partner_count = partners.count()
        apportion_amount = self.amount
        debit_total = 0

        if partner_count == 0 and prev_order is not None:
            prev_partners = OrderPartner.objects.filter(order=prev_order)
            partner_count = prev_partners.count()
            partners_credit = apportion_amount / partner_count
            for partner in prev_partners:
                new_item = OrderPartner(
                    order=self,
                    partner=partner.partner,
                    credit=partners_credit
                )
                new_item.save()
        else:
            partners_credit = apportion_amount / partner_count
            for partner in partners:
                debit_total += partner.debit
                if partner.credit == 0:
                    partner.credit = partners_credit
                    partner.save()

        self.debit = debit_total
        self.final_balance = self.opening_balance + self.amount - self.debit

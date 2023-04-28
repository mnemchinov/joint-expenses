import logging
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from orders.models import Order, OrderStatuses
from orders.services import OrderService

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Order, dispatch_uid='signal_order_calculate')
def signal_order_calculate(**kwargs):
    logger.debug('Start "signal_order_calculate"')
    order = kwargs.get('instance', None)
    if order.status == OrderStatuses.NEW and not order.is_deleted:
        OrderService.calculate_order(order=order, **kwargs)

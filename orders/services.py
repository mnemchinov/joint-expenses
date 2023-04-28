from django.db import models, transaction
import logging

from orders.models import Order, OrderStatuses

logger = logging.getLogger(__name__)


class OrderService:
    model: models = Order

    @staticmethod
    def calculate_order(**kwargs):
        try:
            order: Order = kwargs.get('order')
            prev_order: Order = order.previous_order
            partners = order.partners.through.objects.all()
            partner_count = partners.count()
            opening_balance = order.opening_balance if not prev_order \
                else prev_order.final_balance
            credit = max(order.amount - opening_balance, 0)
            partners_debit_total = 0
            with transaction.atomic():
                if partner_count != 0:
                    one_partner_credit = credit / partner_count
                    for partner in partners:
                        partners_debit_total += partner.debit
                        if partner.credit == 0:
                            partner.credit = one_partner_credit
                            partner.save()
                debit = partners_debit_total
                order.debit = debit
                order.final_balance = debit - credit
                if order.debit >= order.amount:
                    order.status = OrderStatuses.READY
                order.save()
        except Exception as ex:
            logger.exception('Failed to save the order!', exc_info=ex)

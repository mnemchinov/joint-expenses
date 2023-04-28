from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = 'Документы'

    def ready(self):
        import orders.signals
        orders.signals.logger.debug('Load "orders.signals"')

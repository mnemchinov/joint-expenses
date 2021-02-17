from django.contrib import admin
from .models import *


class TabularOrderPartner(admin.TabularInline):
    extra = 0
    show_change_link = True
    model = Order.partners.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('representation', 'status', 'opening_balance',
                    'amount', 'final_balance')
    inlines = (TabularOrderPartner,)
    list_filter = ('date', 'is_deleted', 'status', 'partners')
    search_fields = ('content',)
    fieldsets = (
        ('Основное', {
            'fields': ('date', 'status', 'is_deleted',)
        }),
        ('Параметры заказа', {
            'fields': ('previous_order', 'opening_balance', 'amount', 'debit',
                       'final_balance'),
        }),
        ('Содержимое', {
            'fields': ('content',)
        }),
    )

    def get_changeform_initial_data(self, request):
        initial_data = {
            'previous_order': None,
            'opening_balance': 0,
        }
        previous_order = Order.objects.filter(
            status=OrderStatuses.DELIVERED,
            is_deleted=False
        ).first()

        if previous_order is not None:
            initial_data['previous_order'] = previous_order
            initial_data['opening_balance'] = previous_order.final_balance

        return initial_data




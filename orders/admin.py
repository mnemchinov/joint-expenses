from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class TabularOrderPartner(admin.TabularInline):
    extra = 0
    show_change_link = True
    model = Order.partners.through


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'status', 'opening_balance',
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




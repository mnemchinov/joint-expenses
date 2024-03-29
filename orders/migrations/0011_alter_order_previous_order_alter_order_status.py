# Generated by Django 4.2 on 2023-04-28 08:23

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='previous_order',
            field=models.OneToOneField(blank=True, default=django.db.models.query.QuerySet.last, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order', verbose_name='Предыдущий заказ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(None, '(Не известно)'), (0, 'Распределение'), (1, 'Готов'), (2, 'Доставлен'), (3, 'Отменен')], default=0, verbose_name='Статус'),
        ),
    ]

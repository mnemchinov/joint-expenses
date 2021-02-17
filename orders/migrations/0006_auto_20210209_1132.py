# Generated by Django 3.1.6 on 2021-02-09 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_prevent_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='prevent_order',
        ),
        migrations.AddField(
            model_name='order',
            name='previous_order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order', verbose_name='Предыдущий заказ'),
        ),
    ]
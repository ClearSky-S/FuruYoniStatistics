# Generated by Django 4.0.3 on 2022-08-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_god_totalgame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='god',
            name='ban_ratio',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='god',
            name='pick_ratio',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='god',
            name='win_ratio',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
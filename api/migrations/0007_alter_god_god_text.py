# Generated by Django 4.0.3 on 2022-08-26 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_god_id_card_god'),
    ]

    operations = [
        migrations.AlterField(
            model_name='god',
            name='god_text',
            field=models.TextField(max_length=500),
        ),
    ]

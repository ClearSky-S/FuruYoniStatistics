# Generated by Django 4.0.3 on 2022-08-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_name',
            field=models.CharField(max_length=50),
        ),
    ]

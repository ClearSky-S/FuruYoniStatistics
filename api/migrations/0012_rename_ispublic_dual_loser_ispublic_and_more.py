# Generated by Django 4.0.3 on 2022-08-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_dual_ispublic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dual',
            old_name='isPublic',
            new_name='loser_isPublic',
        ),
        migrations.AddField(
            model_name='dual',
            name='winner_isPublic',
            field=models.BooleanField(default=True),
        ),
    ]
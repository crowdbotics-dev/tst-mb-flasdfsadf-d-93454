# Generated by Django 2.2.28 on 2023-06-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_hi'),
    ]

    operations = [
        migrations.AddField(
            model_name='hello',
            name='dssdds',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.12 on 2022-02-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_date',
            field=models.DateField(),
        ),
    ]

# Generated by Django 3.2.12 on 2022-02-10 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
        ('payables', '0002_alter_payable_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payable',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.transaction'),
        ),
    ]

# Generated by Django 3.2.12 on 2022-02-09 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('requires_card_number', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('barcode', models.CharField(max_length=200, unique=True)),
                ('payment_date', models.DateTimeField()),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.paymentmethod')),
            ],
        ),
    ]

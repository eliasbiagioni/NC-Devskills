from operator import mod
from django.db import models

from transactions.models import Transaction

# Model for service types
class ServiceType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model for payables status
class PaymentStatus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model for payables
class Payable(models.Model):
    service_type        = models.ForeignKey(ServiceType, on_delete=models.PROTECT)
    service_description = models.CharField(max_length=200)
    expiration_date     = models.DateField()
    payment_state       = models.ForeignKey(PaymentStatus, on_delete=models.PROTECT)
    barcode             = models.CharField(max_length=200, unique=True)
    amount              = models.DecimalField(max_digits=6, decimal_places=2)
    payment             = models.OneToOneField(Transaction, on_delete=models.PROTECT, null=True)

    def set_payment(self, transaction):
        self.payment = transaction

    def set_paid(self):
        paid = PaymentStatus.objects.get(name='paid')
        self.payment_state = paid
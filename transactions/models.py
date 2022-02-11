from django.db import models

# Model for payment methods
class PaymentMethod(models.Model):
    name                    = models.CharField(max_length=200)
    requires_card_number    = models.BooleanField(default=False)
    
# Model for transaction
class Transaction(models.Model):
    payment_method  = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    card_number     = models.IntegerField(null=True)
    amount          = models.DecimalField(max_digits=6, decimal_places=2)
    barcode         = models.CharField(max_length=200, unique=True)
    payment_date    = models.DateField()
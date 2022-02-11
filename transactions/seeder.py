from transactions.models import PaymentMethod

# Payment method seeder
payment_methods = [
    {
        "name"                  : "debit_card",
        "requires_card_number"  : True
    },
    {
        "name"                  : "credit_card",
        "requires_card_number"  : True
    },
    {
        "name"                  : "cash",
        "requires_card_number"  : False
    }
]

for payment_method in payment_methods:
    PaymentMethod.objects.create(
        name=payment_method['name'],
        requires_card_number=payment_method['requires_card_number']
    )
from payables.models import ServiceType, PaymentStatus

# Service type seeder
service_types = [
    'Luz',
    'Gas',
    'Agua'
]

for service_type in service_types:
    ServiceType.objects.create(
        name=service_type
    )

# Payment status seeder
payment_statuses = [
    'pending',
    'cancelled',
    'paid'
]

for payment_status in payment_statuses:
    PaymentStatus.objects.create(
        name=payment_status
    )
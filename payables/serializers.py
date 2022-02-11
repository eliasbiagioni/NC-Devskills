from rest_framework import serializers

from .models import Payable

from transactions.serializers import TransactionSerializer

# Serializer for payables
class PayableSerializer(serializers.ModelSerializer):
    
    payment         = TransactionSerializer(many=False, read_only=True)

    class Meta:
        model               = Payable
        fields              = '__all__'
        read_only_fields    = [ 'id' ]

    
# Serializer to list not paid payables
class NotPaidPayableSerializer(serializers.ModelSerializer):
    service_type    = serializers.StringRelatedField(many=False)
    
    class Meta:
        model               = Payable
        fields              = [ 'id', 'expiration_date', 'amount', 'barcode', 'service_type' ]
        read_only_fields    = [ 'id', 'expiration_date', 'amount', 'barcode', 'service_type' ]

# Serializer for payables list without service type
class PayableWithoutServiceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model               = Payable
        fields              = [ 'id', 'expiration_date', 'amount', 'barcode' ]
        read_only_fields    = [ 'id', 'expiration_date', 'amount', 'barcode' ]
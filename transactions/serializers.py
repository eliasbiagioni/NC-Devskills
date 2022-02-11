from rest_framework import serializers

from .models import Transaction

#from payables.serializers import PayableSerializer

class TransactionSerializer(serializers.ModelSerializer):    

    class Meta:
        model               = Transaction
        fields              = '__all__'
        read_only_fields    = [ 'id' ]

    def validate(self, data):
        # Validate if card number is required
        if(data['payment_method'] and data['payment_method'].requires_card_number and (not 'card_number' in data or data['card_number'] == '')):
            raise serializers.ValidationError({
                        'card_number': ['Card number is required']
                        })
        return data

    def create(self, validated_data):
        if( not validated_data['payment_method'].requires_card_number and  'card_number' in validated_data and validated_data['card_number'] is not None ):
            validated_data['card_number'] = None
        # Create transaction
        transaction = super().create(validated_data)

        # Relates payable with its transaction and change payable state
        validated_data['payable'].set_payment(transaction)
        validated_data['payable'].set_paid()
        validated_data['payable'].save()
        return transaction

class SimpleTransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['id', 'payment_method', 'card_number', 'amount','barcode', 'payment_date' ]

class GroupedTransactionSerializer(serializers.Serializer):

    payment_date        = serializers.DateField(required=True)
    total_paid          = serializers.DecimalField(max_digits=6, decimal_places=2)
    transactions_count  = serializers.IntegerField(required=True)
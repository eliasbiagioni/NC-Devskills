from rest_framework import viewsets, filters

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, status

from .models import Transaction
from .serializers import TransactionSerializer, GroupedTransactionSerializer

from payables.models import Payable

from datetime import datetime

from django.db.models import Sum, Count

# FIlters for transactions list
class TransactionFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        # Filter by from date
        if(request.GET.get('from')):
            try:
                from_date = datetime.strptime(request.GET.get('from'), '%Y-%m-%d')
                queryset = queryset.filter(payment_date__gte=from_date.date()).distinct()
            except ValueError:
                pass
        # Filter by to date
        if(request.GET.get('to')):
            try:
                to_date = datetime.strptime(request.GET.get('to'), '%Y-%m-%d')
                queryset = queryset.filter(payment_date__lte=to_date.date()).distinct()
            except ValueError:
                pass
        # Group transactions by payment date and sum their amount
        grouped = (request.GET.get('grouped') and request.GET.get('grouped') == 'true')
        if( grouped ):
            queryset = queryset.values('payment_date').annotate(total_paid=Sum('amount'), transactions_count=Count('barcode'))
        return queryset

# View for transactions
class TransactionViewSet(viewsets.ModelViewSet):
    queryset            = Transaction.objects.all()
    serializer_class    = TransactionSerializer
    filter_backends     = [TransactionFilter]

    def list(self, request):
        grouped = (request.GET.get('grouped') and request.GET.get('grouped') == 'true')
        if( grouped ):
            self.serializer_class = GroupedTransactionSerializer
        filterBackend = self.filter_backends[0]()
        queryset = filterBackend.filter_queryset(request, self.queryset, self)
        return Response(self.serializer_class(queryset, many=True).data)


    def create(self, request, payable_pk=None):
        payable = get_object_or_404(Payable, pk=payable_pk)
        if( payable.payment ):
            raise serializers.ValidationError({
                'payable': [
                    "Payable already paid"
                ]
            })
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['payable'] = payable
            transaction = serializer.create(serializer.validated_data)
            return Response(
                self.serializer_class(transaction).data,
                status=status.HTTP_201_CREATED
            )
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Payable, PaymentStatus
from .serializers import *

class PayableFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        # Filter by not paid state
        not_paid = (request.GET.get('not_paid') and request.GET.get('not_paid') == 'true')
        if(not_paid):
            paid_state  = PaymentStatus.objects.get(name='paid')
            queryset    = queryset.exclude(payment_state=paid_state)

        if(request.GET.get('service_type')):
            queryset = queryset.filter(service_type=int(request.GET.get('service_type')))

        return queryset
        

class PayableViewSet(viewsets.ModelViewSet):
    queryset = Payable.objects.all()
    serializer_class = PayableSerializer
    filter_backends = [PayableFilter]

    def list(self, request):
        if(request.GET.get('not_paid') and request.GET.get('not_paid') == 'true'):
            self.serializer_class = NotPaidPayableSerializer
        if(request.GET.get('service_type')):
            self.serializer_class = PayableWithoutServiceTypeSerializer
        filterBackend = self.filter_backends[0]()
        queryset = filterBackend.filter_queryset(request, self.queryset, self)
        return Response(self.serializer_class(queryset, many=True).data)

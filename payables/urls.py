from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import PayableViewSet

from transactions.views import TransactionViewSet

router = DefaultRouter()
router.register(r'payables', PayableViewSet, basename='payable')

payables_transactions_routes = routers.NestedSimpleRouter(router, r'payables', lookup='payable')
payables_transactions_routes.register(r'transactions', TransactionViewSet, basename='payable-transactions')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(payables_transactions_routes.urls))
]

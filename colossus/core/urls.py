from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    HelloNexusView,
    CategoryViewSet,
    ProductViewSet,
    OrderViewSet,
    PaymentViewSet,
    CartViewSet,
    InventoryHistoryViewSet
)

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('payments', PaymentViewSet)
router.register('carts', CartViewSet)
router.register('inventory', InventoryHistoryViewSet)

urlpatterns = [
    path('hello/', HelloNexusView.as_view(), name='hello'),  # Normal API endpoint
    path('', include(router.urls)),  # All ViewSet routes
]

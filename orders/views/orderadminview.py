from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from orders.models import Order
from orders.serializers import OrderSerializer

class OrderAdminListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
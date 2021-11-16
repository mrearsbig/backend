from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from orders.models import Order
from orders.serializers import OrderSerializer

class OrderAdminRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

class OrderAdminListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
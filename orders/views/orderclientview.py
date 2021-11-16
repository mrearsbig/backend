from django.conf import settings

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from orders.models import Order
from orders.serializers import OrderSerializer

from rest_framework_simplejwt.backends import TokenBackend

class OrderClientListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user = self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION') [7:]
        algorithm = settings.SIMPLE_JWT['ALGORITHM']
        key = settings.SIMPLE_JWT['SIGNING_KEY']
        backend = TokenBackend(algorithm = algorithm, signing_key = key)
        payload = backend.decode(token = token, verify = True)

        if payload['user_id'] != kwargs['pk']:
            return Response({'message': 'user unauthorized'}, status = status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)
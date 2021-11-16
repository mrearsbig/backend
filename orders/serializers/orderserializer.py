from rest_framework.serializers import ModelSerializer

from orders.models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'date': instance.date,
            'shipping': instance.shipping,
            'total': instance.total,
            'client': {
                'username': instance.client.username
            }
        }
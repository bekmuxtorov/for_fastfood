from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import MealSerializer
from utils.determining_total_time import total_time


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    total_payment = serializers.SerializerMethodField()
    delivery_time = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'latitude', 'longitude',
                  'created_at', 'delivery_time', 'total_payment')

    def get_total_payment(self, obj: Order):
        obj.set_total_payment()
        return obj.total_payment

    def get_delivery_time(self, obj: Order):
        obj.set_delivery_time()
        return obj.delivery_time


class OrderListRetrieveSerializer(OrderSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'latitude', 'longitude',
                  'created_at', 'delivery_time', 'total_payment', "order_items")

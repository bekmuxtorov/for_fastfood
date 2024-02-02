from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import MealSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    total_payment = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'latitude', 'longitude',
                  'created_at', 'delivery_time', 'items', 'total_payment')

    def get_total_payment(self, obj):
        total_payment = sum([item.payment for item in obj.items.all()])
        obj.total_payment = total_payment
        obj.save()
        return total_payment

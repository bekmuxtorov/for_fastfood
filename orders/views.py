from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .import serializers
from .import models
from users.permissions import (
    IsAdmin,
    IsCustomer,
    IsWaiter
)


# Order Create api view
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAdmin | IsCustomer]


# Order List api view
class OrderListAPIView(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListRetrieveSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user',]
    search_fields = [
        'user__full_name',
        'user__phone_number', 'longitude', 'latitude'
    ]


# Order Detail api view
class OrderGenericAPIView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListRetrieveSerializer


# Order Update api view
class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAdmin | IsCustomer]


# Order Delete api view
class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAdmin | IsCustomer]


# Order Item


# OrderItem Create api view
class OrderItemCreateAPIView(generics.CreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    permission_classes = [IsAdmin | IsCustomer]


# OrderItem List api view
class OrderItemListAPIView(generics.ListAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['order', 'meal__name', ]
    search_fields = ['meal__name', 'count', 'payment']


# OrderItem Detail api view
class OrderItemGenericAPIView(generics.RetrieveAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


# OrderItem Update api view
class OrderItemUpdateAPIView(generics.UpdateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


# OrderItem Delete api view
class OrderItemDeleteAPIView(generics.DestroyAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer

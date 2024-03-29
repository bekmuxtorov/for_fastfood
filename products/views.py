from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .import serializers
from .import models
from users.permissions import (
    IsAdmin,
    IsCustomer,
    IsWaiter
)


# Meal Create api view
class MealCreateAPIView(generics.CreateAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer
    permission_classes = [IsWaiter | IsAdmin]


# Meal List api view


class MealListAPIView(generics.ListAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer
    permission_classes = [IsWaiter | IsAdmin | IsCustomer]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


# Meal Detail api view
class MealGenericAPIView(generics.RetrieveAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer
    permission_classes = [IsWaiter | IsAdmin | IsCustomer]


# Meal Update api view
class MealUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer
    permission_classes = [IsWaiter | IsAdmin]


# Meal Delete api view
class MealDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer
    permission_classes = [IsWaiter | IsAdmin]

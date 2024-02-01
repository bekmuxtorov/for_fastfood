from rest_framework import generics

from .import serializers
from .import models


# Meal Create api view
class MealCreateAPIView(generics.CreateAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer


# Meal List api view
class MealListAPIView(generics.ListAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer


# Meal Detail api view
class MealGenericAPIView(generics.RetrieveAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer


# Meal Update api view
class MealUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer


# Meal Delete api view
class MealDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer

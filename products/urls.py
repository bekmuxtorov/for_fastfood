from django.urls import path

from .import views


urlpatterns = [
    path('meals/', views.MealListAPIView.as_view()),
    path('meals/create/', views.MealCreateAPIView.as_view()),
    path('meals/<int:pk>/', views.MealGenericAPIView.as_view()),
    path('meals/<int:pk>/update/', views.MealUpdateAPIView.as_view()),
    path('meals/<int:pk>/delete/', views.MealDeleteAPIView.as_view()),
]

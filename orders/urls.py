from django.urls import path

from .import views


urlpatterns = [
    path('orders/', views.OrderListAPIView.as_view()),
    path('orders/create/', views.OrderCreateAPIView.as_view()),
    path('orders/<int:pk>/', views.OrderGenericAPIView.as_view()),
    path('orders/<int:pk>/update/', views.OrderUpdateAPIView.as_view()),
    path('orders/<int:pk>/delete/', views.OrderDeleteAPIView.as_view()),

    # Order Item
    path('order_items/', views.OrderItemListAPIView.as_view()),
    path('order_items/create/', views.OrderItemCreateAPIView.as_view()),
    path('order_items/<int:pk>/', views.OrderItemGenericAPIView.as_view()),
    path('order_items/<int:pk>/update/', views.OrderItemUpdateAPIView.as_view()),
    path('order_items/<int:pk>/delete/', views.OrderItemDeleteAPIView.as_view()),
]

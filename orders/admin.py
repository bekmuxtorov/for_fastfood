from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_user_full_name', 'latitude',
                    'longitude', 'created_at', 'delivery_time')

    search_fields = ('user__full_name',)

    def get_user_full_name(self, obj):
        return obj.user.full_name
    get_user_full_name.short_description = 'User full_name'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'count', 'payment', 'created_at')
    list_filter = ('meal',)
    search_fields = ('meal__name', 'order__user__full_name')

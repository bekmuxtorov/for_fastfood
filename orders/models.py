from django.db.models import Sum
from django.db import models
from users.models import User
from products.models import Meal
from utils.determining_total_time import total_time


class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Mijoz',
    )
    latitude = models.FloatField(
        verbose_name='Joylashuv latitude'
    )
    longitude = models.FloatField(
        verbose_name='Joylashuv longitude'
    )
    created_at = models.DateTimeField(
        verbose_name="Qo'shilgan vaqt",
        auto_now_add=True
    )
    delivery_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Tahminiy yetkazib berish vaqti"
    )
    total_payment = models.DecimalField(
        verbose_name="Umumiy to'lov(chek)",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return ' | '.join(["Order", str(self.id), self.user.phone_number])

    def set_total_payment(self):
        total_payment = sum([item.payment for item in self.order_items.all()])
        if not self.total_payment or self.total_payment != total_payment:
            self.total_payment = total_payment
            self.save()

        return self.total_payment

    def set_delivery_time(self):
        products_count = sum([item.count for item in self.order_items.all()])
        delivery_time = total_time(
            self.latitude, self.longitude, products_count)

        if not self.delivery_time:
            self.delivery_time = delivery_time
            self.save()

        return self.delivery_time


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        verbose_name="Buyurtma",
        related_name='order_items',
        null=True,
        blank=True
    )
    meal = models.ForeignKey(
        to=Meal,
        on_delete=models.CASCADE,
        verbose_name="Taom"
    )
    count = models.IntegerField(
        verbose_name="Soni"
    )
    created_at = models.DateTimeField(
        verbose_name="Qo'shilgan vaqt",
        auto_now_add=True
    )
    payment = models.DecimalField(
        verbose_name="Umumiy to'lov",
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.payment = self.calculate_payment()
        super().save(*args, **kwargs)

    def calculate_payment(self):
        return self.meal.cost * self.count

    def __str__(self):
        return ' | '.join([self.meal.name, str(self.count)])

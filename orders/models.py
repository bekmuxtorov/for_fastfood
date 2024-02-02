from django.db.models import Sum
from django.db import models
from users.models import User
from products.models import Meal


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
    items = models.ManyToManyField(
        "orders.OrderItem", related_name='orders', verbose_name="Items")
    total_payment = models.DecimalField(
        verbose_name="Umumiy to'lov(chek)",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return ' | '.join(["Order", str(self.id), self.user.phone_number])


class OrderItem(models.Model):
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

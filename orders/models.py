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
    meals = models.ManyToManyField(
        to=Meal,
        related_name="orders",
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

    def __str__(self):
        return ' | '.join(["Order", str(self.id), self.user.phone_number])

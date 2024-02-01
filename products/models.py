from django.db import models


class Meal(models.Model):
    name = models.CharField(
        verbose_name='Ovqat nomi',
        max_length=100
    )
    cost = models.DecimalField(
        verbose_name='Ovqat narxi(UZS):',
        max_digits=6,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

from .managers import UserManager

USER_ROLES = (
    ('admin', 'Adminstrator'),
    ('waiter', 'Ofitsiant'),
    ('customer', 'Mijoz')
)


class User(AbstractBaseUser, PermissionsMixin):
    role = models.CharField(
        choices=USER_ROLES,
        default='customer',
        max_length=88
    )
    phone_number = models.CharField(
        verbose_name="phone number",
        max_length=20,
        unique=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+998\d{9}$',
                message='Invalid phone number. Please enter in the format +998901234567'
            ),
        ]
    )
    full_name = models.CharField(
        verbose_name="Ism familiya",
        max_length=100,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name="is staff",
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name="Yaratilgan vaqt",
        auto_now_add=True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.phone_number

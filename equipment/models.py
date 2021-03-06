from django.db import models
from django.utils import timezone
from django.core import validators

from user.models import User
from django.conf import settings
# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)

    address = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.CharField(validators=[validators.RegexValidator("1[345678]\d{9}",message='Please Enter the right phone number!')],
                             max_length=20)
    description = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_equipments')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rented_equipments', null=True, blank=True)

    class Status(models.TextChoices):
        UNRELEASED = 'UNR'
        UNAPPROVED = 'UNA'
        AVAILABLE = 'AVA'
        RENTED = 'REN'
        RETURNED = 'RET'

    status = models.CharField(max_length=3, choices=Status.choices, default=Status.UNRELEASED)

    is_released = models.BooleanField(default=False)

    # foreign key related name:
    #   release_applications
    #   rent_applications

    # if it is rented
    # current_tenant: rent_applications.get(applying=True).hirer
    # lease_term_end: rent_applications.get(applying=True).lease_term_end
    # user_comments: rent_applications.get(applying=True).user_comments

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        app_label = 'equipment'


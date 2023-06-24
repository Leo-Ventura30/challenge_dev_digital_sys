from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Customers
import random


@receiver(pre_save, sender=Customers)
def customers_signal(sender, instance, **kwargs):
    instance.score = random.randint(0, 999)

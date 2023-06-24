from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Customers
from .tasks import approve_proposal

import random


@receiver(pre_save, sender=Customers)
def customers_signal(sender, instance, **kwargs):
    if instance.status == 'em_analise' and instance.score == 0:
        instance.score = 800


@receiver(post_save, sender=Customers)
def customers_signal(sender, instance, **kwargs):
    if instance.status == 'em_analise':
        approve_proposal.apply_async((instance.id,), countdown=10)

from datetime import datetime
import random

from django.db import models
from django.utils.translation import ugettext_lazy as _


def _subscription_code(length=20):
    choices = '23456789abcdefghjkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
    return ''.join(random.choice(choices) for i in range(length))


class SubscriptionManager(models.Manager):
    def subscribers(self):
        return self.filter(is_active=True)


class Subscription(models.Model):
    is_active = models.BooleanField(_('is active'), default=False)
    created = models.DateTimeField(_('created'))
    last_updated = models.DateTimeField(_('last updated'))

    code = models.CharField(_('code'), max_length=40, default=_subscription_code,
        unique=True)

    confirmed_on = models.DateTimeField(_('confirmed on'), blank=True, null=True)
    unsubscribed_on = models.DateTimeField(_('unsubscribed on'), blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['-created']
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()

        self.is_active = (self.confirmed_on and not self.unsubscribed_on)
        self.last_updated = datetime.now()

        super(Subscription, self).save(*args, **kwargs)

    @models.permalink
    def confirmation_url(self):
        return ('yesimeanit_subscription_confirm', (), {'code': self.code})

    @models.permalink
    def unsubscription_url(self):
        return ('yesimeanit_subscription_unsubscribe', (), {'code': self.code})

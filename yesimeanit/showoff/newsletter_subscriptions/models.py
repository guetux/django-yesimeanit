from django.db import models
from django.utils.translation import ugettext_lazy as _

from yesimeanit.models import Subscription


class NewsletterSubscription(Subscription):
    SALUTATION_CHOICES = (
        ('f', _('Mrs.')),
        ('m', _('Mr.')),
        ('?', _('Unspecified')),
        )

    salutation = models.CharField(_('salutation'), max_length=1,
        choices=SALUTATION_CHOICES, blank=True)
    email = models.EmailField(_('email'))
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = _('newsletter subscription')
        verbose_name_plural = _('newsletter subscriptions')

    def __unicode__(self):
        return self.email
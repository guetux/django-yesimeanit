from datetime import datetime

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from yesimeanit.models import Subscription, SubscriptionManager


class NewsletterSubscriptionManager(SubscriptionManager):
    def create_subscription(self, email, **kwargs):
        confirmed = kwargs.pop('confirmed', False)

        try:
            object = self.get(email=email)
        except self.model.DoesNotExist:
            object = self.model(email=email)

        for k, v in kwargs.items():
            setattr(object, k, v)

        if confirmed:
            object.confirmed_on = datetime.now()
        else:
            object.send_subscription_mail()

        object.save()
        return object


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

    objects = NewsletterSubscriptionManager()

    def __unicode__(self):
        return self.email

    def send_subscription_mail(self):
        lines = render_to_string('newsletter_subscriptions/subscription_mail.txt', {
            'site': Site.objects.get_current(),
            'object': self,
            }).splitlines()

        send_mail(lines[0], u'\n'.join(lines[2:]), settings.DEFAULT_FROM_EMAIL,
            [self.email], fail_silently=False)

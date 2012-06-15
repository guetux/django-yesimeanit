from django.conf.urls import patterns, include, url

from yesimeanit.views import (ConfirmationView, UnsubscriptionView)
from .views import (SubscribeView, UnsubscribeView)
from .models import NewsletterSubscription


urlpatterns = patterns('',
    url(r'^$', SubscribeView.as_view(),
        name='newsletter_subscriptions_newslettersubscription_subscribe'),
    url(r'^unsubscribe/$', UnsubscribeView.as_view(),
        name='newsletter_subscriptions_newslettersubscription_unsubscribe'),

    url(r'^subscribe/(?P<code>\w+)/$', ConfirmationView.as_view(
        model=NewsletterSubscription,
        ), name='newsletter_subscriptions_newslettersubscription_confirm'),
    url(r'^unsubscribe/(?P<code>\w+)/$', UnsubscriptionView.as_view(
        model=NewsletterSubscription,
        ), name='newsletter_subscriptions_newslettersubscription_unsubscribe'),
)

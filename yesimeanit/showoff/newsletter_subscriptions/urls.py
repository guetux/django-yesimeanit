from django.conf.urls.defaults import patterns, include, url

from yesimeanit.views import (ConfirmationView, UnsubscriptionView)
from .views import (SubscriptionView,)
from .models import NewsletterSubscription


urlpatterns = patterns('',
    url(r'^$', SubscriptionView.as_view(),
        name='newsletter_subscriptions_newslettersubscription_subscribe'),
    url(r'^subscribe/(?P<code>\w+)/$', ConfirmationView.as_view(
        model=NewsletterSubscription,
        ), name='newsletter_subscriptions_newslettersubscription_confirm'),
    url(r'^subscribe/(?P<code>\w+)/$', UnsubscriptionView.as_view(
        model=NewsletterSubscription,
        ), name='newsletter_subscriptions_newslettersubscription_unsubscribe'),
)

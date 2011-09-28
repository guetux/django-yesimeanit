from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from .forms import (SubscribtionForm, UnsubscriptionForm)
from .models import NewsletterSubscription


class SubscriptionView(generic.CreateView):
    form_class = SubscribtionForm
    model = NewsletterSubscription
    subscribed_message = _('Subscription request successful. You have been sent a mail with a confirmation link.')

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            'Newsletter subscription',
            '''
Confirm the subscription here: %s
Unsubscribe here: %s
''' % (self.object.confirmation_url(), self.object.unsubscription_url()),
            settings.DEFAULT_FROM_EMAIL,
            [self.object.email],
            fail_silently=False)

        self.template_name_suffix = '_result'
        return self.render_to_response(self.get_context_data(
            object=self.object,
            subscribed=True,
            message=self.subscribed_message))


class UnsubscriptionView(generic.FormView):
    form_class = UnsubscriptionForm
    model = NewsletterSubscription
    template_name = 'newsletter_subscriptions/newslettersubscription_form.html'
    unsubscribed_message = _('The subscription has been successfully cancelled.')

    def form_valid(self, form):
        for object in NewsletterSubscription.objects.active().filter(email=form.cleaned_data['email']):
            object.unsubscribed_on = datetime.now()
            object.save()

        self.template_name = 'newsletter_subscriptions/newslettersubscription_result.html'
        return self.render_to_response(self.get_context_data(
            object=form.cleaned_data['email'], # TODO ugly, but the template only uses object... :-)
            unsubscribed=True,
            message=self.unsubscribed_message))

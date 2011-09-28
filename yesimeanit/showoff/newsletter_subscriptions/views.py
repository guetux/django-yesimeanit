from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from .forms import NewsletterSubscriptionForm
from .models import NewsletterSubscription


class SubscriptionView(generic.CreateView):
    form_class = NewsletterSubscriptionForm
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
            message=self.subscribed_message))

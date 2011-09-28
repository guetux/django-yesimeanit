from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView


class YesIMeanItView(DetailView):
    slug_field = 'code'
    slug_url_kwarg = 'code'


class ConfirmationView(YesIMeanItView):
    already_confirmed_message = _('This subscription has already been confirmed.')

    def get_context_data(self, **kwargs):
        if self.object.confirmed_on:
            kwargs['already_confirmed'] = True
            kwargs['error'] = self.already_confirmed_message
        else:
            self.object.confirmed_on = datetime.now()
            self.object.save()

        return super(ConfirmationView, self).get_context_data(**kwargs)


class UnsubscriptionView(YesIMeanItView):
    already_unsubscribed_message = _('This subscription has already been deactivated.')
    not_active_yet_message = _('This subscription cannot be deactivated, it isn\'t activated yet.')

    def get_context_data(self, **kwargs):
        if self.confirmed_on:
            if self.object.unsubscribed_on:
                kwargs['already_unsubscribed'] = True
                kwargs['error'] = self.already_unsubscribed_message
            else:
                self.object.unsubscribed_on = datetime.now()
                self.object.save()
        else:
            kwargs['not_active_yet'] = True
            kwargs['error'] = self.not_active_yet_message

        return super(ConfirmationView, self).get_context_data(**kwargs)

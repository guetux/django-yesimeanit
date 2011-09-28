from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from django.views import generic


class YesIMeanItView(generic.DetailView):
    slug_field = 'code'
    slug_url_kwarg = 'code'
    template_name_suffix = '_result'


class ConfirmationView(YesIMeanItView):
    already_confirmed_message = _('This subscription has already been confirmed.')
    confirmed_message = _('The subscription has been successfully confirmed.')

    def get_context_data(self, **kwargs):
        if self.object.confirmed_on:
            kwargs['already_confirmed'] = True
            kwargs['message'] = self.already_confirmed_message
        else:
            kwargs['confirmed'] = True
            kwargs['message'] = self.confirmed_message
            self.object.confirmed_on = datetime.now()
            self.object.save()

        return super(ConfirmationView, self).get_context_data(**kwargs)


class UnsubscriptionView(YesIMeanItView):
    already_unsubscribed_message = _('This subscription has already been deactivated.')
    not_active_yet_message = _('This subscription cannot be deactivated, it isn\'t activated yet.')
    unsubscribed_message = _('The subscription has been successfully cancelled.')

    def get_context_data(self, **kwargs):
        if self.object.confirmed_on:
            if self.object.unsubscribed_on:
                kwargs['already_unsubscribed'] = True
                kwargs['message'] = self.already_unsubscribed_message
            else:
                kwargs['unsubscribed'] = True
                kwargs['message'] = self.unsubscribed_message
                self.object.unsubscribed_on = datetime.now()
                self.object.save()
        else:
            kwargs['not_active_yet'] = True
            kwargs['message'] = self.not_active_yet_message

        return super(UnsubscriptionView, self).get_context_data(**kwargs)

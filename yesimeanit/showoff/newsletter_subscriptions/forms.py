from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import NewsletterSubscription


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ('salutation', 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and NewsletterSubscription.objects.active().filter(email=email).count():
            raise forms.ValidationError(_('This e-mail address already has an active subscription.'))
        return email


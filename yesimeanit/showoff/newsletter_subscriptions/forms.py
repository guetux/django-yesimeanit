from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import NewsletterSubscription


class SubscribtionForm(forms.ModelForm):
    salutation = forms.ChoiceField(choices=NewsletterSubscription.SALUTATION_CHOICES,
        required=False, label=_('salutation'), widget=forms.RadioSelect)

    class Meta:
        model = NewsletterSubscription
        fields = ('salutation', 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and NewsletterSubscription.objects.active().filter(email=email).count():
            raise forms.ValidationError(_('This e-mail address already has an active subscription.'))
        return email


class UnsubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ('email',)

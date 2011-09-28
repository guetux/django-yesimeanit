from django.contrib import admin

from .models import NewsletterSubscription


admin.site.register(NewsletterSubscription,
    list_display=('email', 'is_active', 'confirmed_on', 'unsubscribed_on'),
    list_filter=('is_active',),
    )

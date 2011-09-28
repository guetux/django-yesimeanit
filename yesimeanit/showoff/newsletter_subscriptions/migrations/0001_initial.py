# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'NewsletterSubscription'
        db.create_table('newsletter_subscriptions_newslettersubscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('code', self.gf('django.db.models.fields.CharField')(default='pb2E3QZXBn5Ft3Kv339N', unique=True, max_length=40)),
            ('confirmed_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('unsubscribed_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('salutation', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('newsletter_subscriptions', ['NewsletterSubscription'])

    def backwards(self, orm):
        
        # Deleting model 'NewsletterSubscription'
        db.delete_table('newsletter_subscriptions_newslettersubscription')

    models = {
        'newsletter_subscriptions.newslettersubscription': {
            'Meta': {'ordering': "['-created']", 'object_name': 'NewsletterSubscription'},
            'code': ('django.db.models.fields.CharField', [], {'default': "'eVCNx8FbnBAcoY84pmvB'", 'unique': 'True', 'max_length': '40'}),
            'confirmed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'unsubscribed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['newsletter_subscriptions']

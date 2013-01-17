# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Wall'
        db.create_table('social_wall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('privacy', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('social', ['Wall'])

        # Adding model 'UserHistory'
        db.create_table('social_userhistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.User'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('cigarette', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cigarette.Cigarette'])),
        ))
        db.send_create_signal('social', ['UserHistory'])


    def backwards(self, orm):
        # Deleting model 'Wall'
        db.delete_table('social_wall')

        # Deleting model 'UserHistory'
        db.delete_table('social_userhistory')


    models = {
        'cigarette.cigarette': {
            'Meta': {'object_name': 'Cigarette'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'profiles.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'privacy': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'social.userhistory': {
            'Meta': {'object_name': 'UserHistory'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'cigarette': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cigarette.Cigarette']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.User']"})
        },
        'social.wall': {
            'Meta': {'object_name': 'Wall'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'privacy': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.User']"})
        }
    }

    complete_apps = ['social']
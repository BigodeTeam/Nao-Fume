# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Friend', fields ['user', 'fb_id']
        db.create_unique('profiles_friend', ['user_id', 'fb_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Friend', fields ['user', 'fb_id']
        db.delete_unique('profiles_friend', ['user_id', 'fb_id'])


    models = {
        'profiles.friend': {
            'Meta': {'unique_together': "(('user', 'fb_id'),)", 'object_name': 'Friend'},
            'fb_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.User']"})
        },
        'profiles.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '1'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['profiles']
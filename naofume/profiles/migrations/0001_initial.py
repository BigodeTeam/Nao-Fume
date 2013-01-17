# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('profiles_user', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('picture', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('meta', self.gf('django.db.models.fields.DateField')()),
            ('privacy', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('username', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal('profiles', ['User'])

        # Adding model 'Friend'
        db.create_table('profiles_friend', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.User'])),
            ('fb_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('picture', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal('profiles', ['Friend'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('profiles_user')

        # Deleting model 'Friend'
        db.delete_table('profiles_friend')


    models = {
        'profiles.friend': {
            'Meta': {'object_name': 'Friend'},
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
            'meta': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'privacy': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['profiles']
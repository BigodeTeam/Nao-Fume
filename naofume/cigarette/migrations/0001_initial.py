# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cigarette'
        db.create_table('cigarette_cigarette', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('cigarette', ['Cigarette'])

        # Adding model 'HistoryCigarette'
        db.create_table('cigarette_historycigarette', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cigarette', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cigarette.Cigarette'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('amount', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('cigarette', ['HistoryCigarette'])


    def backwards(self, orm):
        # Deleting model 'Cigarette'
        db.delete_table('cigarette_cigarette')

        # Deleting model 'HistoryCigarette'
        db.delete_table('cigarette_historycigarette')


    models = {
        'cigarette.cigarette': {
            'Meta': {'object_name': 'Cigarette'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'cigarette.historycigarette': {
            'Meta': {'object_name': 'HistoryCigarette'},
            'amount': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'cigarette': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cigarette.Cigarette']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['cigarette']
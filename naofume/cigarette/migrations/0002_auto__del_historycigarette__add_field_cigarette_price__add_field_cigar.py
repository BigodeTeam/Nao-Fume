# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'HistoryCigarette'
        db.delete_table('cigarette_historycigarette')

        # Adding field 'Cigarette.price'
        db.add_column('cigarette_cigarette', 'price',
                      self.gf('django.db.models.fields.FloatField')(default=5.0),
                      keep_default=False)

        # Adding field 'Cigarette.amount'
        db.add_column('cigarette_cigarette', 'amount',
                      self.gf('django.db.models.fields.IntegerField')(default=20, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'HistoryCigarette'
        db.create_table('cigarette_historycigarette', (
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('cigarette', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cigarette.Cigarette'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('cigarette', ['HistoryCigarette'])

        # Deleting field 'Cigarette.price'
        db.delete_column('cigarette_cigarette', 'price')

        # Deleting field 'Cigarette.amount'
        db.delete_column('cigarette_cigarette', 'amount')


    models = {
        'cigarette.cigarette': {
            'Meta': {'object_name': 'Cigarette'},
            'amount': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['cigarette']
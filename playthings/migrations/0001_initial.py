# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('playthings_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('playthings', ['Country'])

        # Adding model 'City'
        db.create_table('playthings_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playthings.Country'])),
        ))
        db.send_create_signal('playthings', ['City'])

        # Adding model 'Hood'
        db.create_table('playthings_hood', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playthings.City'])),
        ))
        db.send_create_signal('playthings', ['Hood'])

        # Adding model 'Plaything'
        db.create_table('playthings_plaything', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=12)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=12)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('neighbourhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playthings.Hood'])),
        ))
        db.send_create_signal('playthings', ['Plaything'])


    def backwards(self, orm):
        
        # Deleting model 'Country'
        db.delete_table('playthings_country')

        # Deleting model 'City'
        db.delete_table('playthings_city')

        # Deleting model 'Hood'
        db.delete_table('playthings_hood')

        # Deleting model 'Plaything'
        db.delete_table('playthings_plaything')


    models = {
        'playthings.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'playthings.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'playthings.hood': {
            'Meta': {'ordering': "['name']", 'object_name': 'Hood'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'playthings.plaything': {
            'Meta': {'ordering': "['neighbourhood', 'type']", 'object_name': 'Plaything'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '12'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '12'}),
            'neighbourhood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Hood']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['playthings']

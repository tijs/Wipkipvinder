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

        # Adding model 'Category'
        db.create_table('playthings_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('playthings', ['Category'])

        # Adding model 'Type'
        db.create_table('playthings_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playthings.Category'], null=True)),
        ))
        db.send_create_signal('playthings', ['Type'])

        # Adding model 'Plaything'
        db.create_table('playthings_plaything', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playthings.Type'])),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=12)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=12)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('neighbourhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playthings.Hood'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playthings.City'], null=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 6, 5, 15, 7, 58, 131791), auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('playthings', ['Plaything'])

        # Adding unique constraint on 'Plaything', fields ['reference', 'city']
        db.create_unique('playthings_plaything', ['reference', 'city_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Plaything', fields ['reference', 'city']
        db.delete_unique('playthings_plaything', ['reference', 'city_id'])

        # Deleting model 'Country'
        db.delete_table('playthings_country')

        # Deleting model 'City'
        db.delete_table('playthings_city')

        # Deleting model 'Hood'
        db.delete_table('playthings_hood')

        # Deleting model 'Category'
        db.delete_table('playthings_category')

        # Deleting model 'Type'
        db.delete_table('playthings_type')

        # Deleting model 'Plaything'
        db.delete_table('playthings_plaything')


    models = {
        'playthings.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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
            'Meta': {'ordering': "['neighbourhood', 'type']", 'unique_together': "(('reference', 'city'),)", 'object_name': 'Plaything'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.City']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 5, 15, 7, 58, 131791)', 'auto_now_add': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '12'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '12'}),
            'neighbourhood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Hood']"}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Type']"})
        },
        'playthings.type': {
            'Meta': {'ordering': "['name']", 'object_name': 'Type'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Category']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['playthings']

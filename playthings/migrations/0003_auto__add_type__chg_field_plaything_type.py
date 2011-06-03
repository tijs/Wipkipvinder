# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Type'
        db.create_table('playthings_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('playthings', ['Type'])

        # Renaming column for 'Plaything.type' to match new field type.
        db.rename_column('playthings_plaything', 'type', 'type_id')
        # Changing field 'Plaything.type'
        db.alter_column('playthings_plaything', 'type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playthings.Type']))

        # Adding index on 'Plaything', fields ['type']
        db.create_index('playthings_plaything', ['type_id'])


    def backwards(self, orm):
        
        # Removing index on 'Plaything', fields ['type']
        db.delete_index('playthings_plaything', ['type_id'])

        # Deleting model 'Type'
        db.delete_table('playthings_type')

        # Renaming column for 'Plaything.type' to match new field type.
        db.rename_column('playthings_plaything', 'type_id', 'type')
        # Changing field 'Plaything.type'
        db.alter_column('playthings_plaything', 'type', self.gf('django.db.models.fields.CharField')(max_length=100))


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
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 3, 14, 18, 8, 350645)', 'auto_now_add': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '12'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '12'}),
            'neighbourhood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Hood']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Type']"})
        },
        'playthings.type': {
            'Meta': {'ordering': "['name']", 'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['playthings']

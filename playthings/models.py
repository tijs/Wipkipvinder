from datetime import datetime
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = 'countries'
        ordering = ['name']

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey("Country")

    class Meta:
        verbose_name_plural = 'cities'
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Hood(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey("City")

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("Category", null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Plaything(models.Model):
    type = models.ForeignKey("Type")
    reference = models.CharField(max_length=20, null=True)
    lat = models.DecimalField(max_digits=16, decimal_places=12)
    lng = models.DecimalField(max_digits=16, decimal_places=12)
    address = models.TextField(blank=True, null=True)
    neighbourhood = models.ForeignKey("Hood")
    city = models.ForeignKey("City", null=True)
    last_updated = models.DateTimeField(auto_now_add=True, editable=False, default=datetime.now())

    class Meta:
        unique_together = ('reference', 'city')
        ordering = ['neighbourhood', 'type']

    def __unicode__(self):
        return "%s, %s" % (self.reference, self.type.name)

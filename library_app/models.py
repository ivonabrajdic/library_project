# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()

    class Meta:
        ordering = ('first_name',)
        
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    isbn = models.CharField(max_length=13)
    year_published = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    class Meta:
        ordering = ('title',)

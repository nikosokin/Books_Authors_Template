# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-24 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_authors_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(related_name='book', to='books_authors_app.Authors'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce', '0003_product_page_field_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ean',
            field=models.CharField(blank=True, help_text='European Article Number', max_length=255, null=True, unique=True, verbose_name='EAN'),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, help_text='Stock Keeping Unit', max_length=255, null=True, unique=True, verbose_name='SKU'),
        ),
    ]

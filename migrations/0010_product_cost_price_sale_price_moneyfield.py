# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 10:32
from __future__ import unicode_literals

from django.db import migrations
import wagtailcommerce.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce', '0009_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost_price',
            field=wagtailcommerce.fields.MoneyField(blank=True, decimal_places=2, default=None, help_text='Cost of the product.', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=wagtailcommerce.fields.MoneyField(blank=True, decimal_places=2, default=None, help_text='Base price to compute the customer price. Sometimes called the catalog price.', max_digits=10, null=True),
        ),
    ]
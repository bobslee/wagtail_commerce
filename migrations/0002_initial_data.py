# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 20:12
from __future__ import unicode_literals

from django import VERSION as DJANGO_VERSION
from django.db import migrations

from ..models import CommercePage, ProductIndexPage
from wagtail.wagtailcore.models import Page, Site

def initial_data(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')

    root_page = Page.objects.get(slug='root')
    
    commerce_page = CommercePage(
        title="Commerce",
        body="This is the main Commerce Page. Ensure it's moved under a Site Root Page."
    )

    root_page.add_child(instance=commerce_page)

    product_index_page = ProductIndexPage(
        title="Products",
    )

    commerce_page.add_child(instance=product_index_page)

def remove_initial_data(apps, schema_editor):
    """This function does nothing. The below code is commented out together
    with an explanation of why we don't need to bother reversing any of the
    initial data"""
    pass
    # This does not need to be deleted, Django takes care of it.
    # page_content_type = ContentType.objects.get(
    #     model='page',
    #     app_label='wagtailcore',
    # )

    # Page objects: Do nothing, the table will be deleted when reversing 0001

    # Do not reverse Site creation since other models might depend on it

    # Remove auth groups -- is this safe? External objects might depend
    # on these groups... seems unsafe.
    # Group.objects.filter(
    #     name__in=('Moderators', 'Editors')
    # ).delete()
    #
    # Likewise, we're leaving all GroupPagePermission unchanged as users may
    # have been assigned such permissions and its harmless to leave them.

class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce', '0001_initial')
    ]

    operations = [
        migrations.RunPython(initial_data, remove_initial_data),
    ]

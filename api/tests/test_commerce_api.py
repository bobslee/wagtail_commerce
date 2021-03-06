from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ...tests import test_commerce

class CommerceAPITestCase(APITestCase, test_commerce.CommerceTestCase):
    def setUp(self):
        super(CommerceAPITestCase, self).setUp()
        self.url_product_search_filters = reverse('product-search-filters')
        self.url_product_search_query = reverse('product-search-query')

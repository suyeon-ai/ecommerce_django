# from unittest import skip

from django.test import Client, RequestFactory, TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from .models import Category, Product
from django.test import Client
from django.urls import reverse

from .views import all_products

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.test_data = Category.objects.create(name='TOUR MERCH', slug='tour-merch')
    
    # Category class testing
    def test_category_model_entry(self):
        data = self.test_data
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'TOUR MERCH')  
    

class TestProductsModel(TestCase):
    
    def setUp(self):
        Category.objects.create(id=4, name='TOUR MERCH', slug='tour-merch')
        User.objects.create(id=2, username='test1')
        self.test_data = Product.objects.create(product_name='4 cuts photo', price='10000', description='testing',
                                                product_image='None', detail_image='None', slug='4-cuts-photo', in_stock=1, is_active=1,
                                                category_id=4, created_by_id=2)
    
    # Product class testing
    def test_product_model_entry(self):
        data = self.test_data
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), '4 cuts photo')   

    
# @skip('the reason of skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViewResponses(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        Category.objects.create(id=4, name='TOUR MERCH', slug='tour-merch')
        User.objects.create(id=2, username='test1')
        Product.objects.create(product_name='4 cuts photo', price='10000', description='testing',
                               product_image='None', detail_image='None', slug='4-cuts-photo', in_stock=1, is_active=1,
                               category_id=4, created_by_id=2)
        
    def test_url_allowed_hosts(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_product_detail_url(self):
        response = self.client.get(reverse('store:product_detail', args=['4-cuts-photo']))
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_function(self):
        request = self.factory.get('item/butter')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
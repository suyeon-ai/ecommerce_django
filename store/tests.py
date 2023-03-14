from django.test import TestCase
from django.contrib.auth.models import User

from .models import Category, Product


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

    

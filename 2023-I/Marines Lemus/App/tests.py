from django.test import TestCase
from .models import Clients, Products

# Create your tests here.

class ClientsTestCase(TestCase):
    def setUp(sefl):
        Clients.objects.create(name='prueba', email='prueba@correo.com')
    
    def test_cliente_existe(self):
        client = Clients.objects.get(name="prueba")
        self.assertEqual(client.email, "prueba@correo.com")
        self.assertIsNotNone(client.date_joined)

class ProductsTestCase(TestCase):
    def setUp(sefl):
        Products.objects.create(name='prueba', price=00000, sku= 'SKU000000')
    
    def test_producto_existe(self):
        product = Products.objects.get(name="prueba")
        self.assertEqual(product.price, 00000)
        self.assertEqual(product.sku, "SKU000000")
        self.assertIsNotNone(product.image)
    
    def test_producto_imagen(self):
        product = Products.objects.get(name="prueba")
        self.assertEqual(product.image.url, "/media/default_image.jpg")

    def test_producto_unico_sku(self):
        with self.assertRaises(Exception):
            Products.objects.create(name="prueba dos", price=00000, sku="SKU000000")




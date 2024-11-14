from django.test import Client, TestCase



class TestDistributedFinance(TestCase):
    def setUp(self):
        self.client = Client(headers=None)
    
    def test_post(self):
        data = {
            "income": 50000, 
            "purpose": "накопление", 
            "hobby": ["спорт", "игры"], 
            "family": "женат",  
            "number_children": 2, 
            "flat_or_house": "квартира"
        }
        response = self.client.post(
            "/distribution_finances/",
            data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)
    # использовать Mock
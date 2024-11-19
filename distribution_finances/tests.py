from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import DistributionFinances
from django.contrib.auth.models import User
from json import dumps



class TestDistributionFinances(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="unit_test", password="password")
        self.factory = APIRequestFactory()
    
    def test_post(self):
        data = {
            "income": 50000, 
            "purpose": "накопление", 
            "hobby": ["спорт", "игры"], 
            "family": "женат",  
            "number_children": 2, 
            "flat_or_house": "квартира"
        }
        request = self.factory.post(
            "distribution_finances/",
            dumps(data),          
            content_type='application/json'
        )
        request.user = self.user
        # request.data = data
        view = DistributionFinances.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 201)

# переписать тесты
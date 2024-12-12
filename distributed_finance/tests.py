from django.test import TestCase
from unittest.mock import patch, MagicMock
from rest_framework.test import APIRequestFactory
from .views import DistributedFinance
from django.contrib.auth.models import User



class TestDistributedFinance(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="unit_test", password="password")
        self.factory = APIRequestFactory()

    @patch('distributed_finance.views.FinancesData')
    @patch('distributed_finance.views.UserData')
    def test_get_finances_success(
        self, mock_userdata_client, mock_financesdata_client
    ):
        user_data = MagicMock()
        mock_userdata_client.return_value = user_data
        user_data.__getitem__.return_value = user_data    
        user_data.get_data.return_value = {
            "_id": "unit_test",
            "income": 50000, 
            "purpose": "накопление", 
            "hobby": ["спорт", "игры"], 
            "family": "женат",  
            "number_children": 2, 
            "flat_or_house": "квартира"
        }

        finances_data = MagicMock()
        mock_financesdata_client.return_value = finances_data
        finances_data.__getitem__.return_value = finances_data
        finances_data.get_data.return_value = {
            "_id": "unit_test",
            "продукты питания": 10000,
            "дом или квартира": 10000,
            "транспорт": 5000,
            "семья": 10000,
            "спорт": 3000,
            "игры": 2000,
            "прочие расходы": 5000,
            "остаток": 5000
        }

        request = self.factory.get('/distributed_finance/')
        request.user = self.user
        view = DistributedFinance.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 302)
        
from django.urls import path, include
from .views import DistributedFinance


urlpatterns = [
    path('', DistributedFinance.as_view())
]

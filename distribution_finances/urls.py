from django.urls import path, include
from .views import DistributionFinances



urlpatterns = [
    path('', DistributionFinances.as_view()),

]

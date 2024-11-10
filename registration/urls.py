from django.urls import path, include
from .views import CreateUser

urlpatterns = [
    path('', CreateUser.as_view()),

]

from django.urls import path, include



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('registration/', include('registration.urls')),
]

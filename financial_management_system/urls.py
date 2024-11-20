from django.urls import path, include



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('registration/', include('registration.urls')),
    path('api/v1/distribution_finances/', include('distribution_finances.urls')),
    path('api/v1/distributed_finance/', include('distributed_finance.urls')),
]

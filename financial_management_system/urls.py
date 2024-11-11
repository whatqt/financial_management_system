from django.urls import path, include



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('registration/', include('registration.urls')),
    path('distribution_finances/', include('distribution_finances.urls')),

    
]

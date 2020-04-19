from django.urls import path, include


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-registration/', include('rest_auth.registration.urls'))
]

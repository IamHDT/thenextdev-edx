from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

app_name = 'jwt_auth_api'

urlpatterns = [
    url(r'^jwt_auth/refresh/', refresh_jwt_token, name='jwt_auth_api'),
    url(r'^jwt_auth/verify/', verify_jwt_token, name='jwt_auth_api'),
    url(r'^jwt_auth/token/', obtain_jwt_token, name='jwt_auth_api'),
]

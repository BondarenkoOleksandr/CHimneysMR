<<<<<<< HEAD
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
=======
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token, obtain_jwt_token

from accounts.api.views import GoogleLoginApi

app_name = 'accounts_api'

urlpatterns = [
    path('login/google/', GoogleLoginApi.as_view(), name='google-login'),
    path('login/facebook/', GoogleLoginApi.as_view(), name='facebook-login'),
    path('token-refresh/', refresh_jwt_token),  # REFRESH JET TOKEN
    path('token-verify/', verify_jwt_token),  # VERIFY JET TOKEN
    path('token-auth/', obtain_jwt_token),  # OBTAIN JET TOKEN
>>>>>>> 1ed7da5f399e20a2b7473c81dc9d369b2b27de94
]
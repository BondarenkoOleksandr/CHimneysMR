from django.urls import path

from accounts.api.views import GoogleLoginApi, UserMeApi

app_name = 'accounts_api'

urlpatterns = [
    path('login/google/', GoogleLoginApi.as_view(), name='google-login'),
    path('login/facebook/', GoogleLoginApi.as_view(), name='facebook-login'),
    path('me/', UserMeApi.as_view(), name='me')
]
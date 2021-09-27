from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
]
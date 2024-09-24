from django.urls import path
from .views import register, login, protected_route, generate_api_key, list_api_keys, deactivate_api_key
from .passwordless_views import send_login_token, verify_login_token

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('protected/', protected_route, name='protected'),
    path('api-key/generate/', generate_api_key, name='generate_api_key'),
    path('api-key/list/', list_api_keys, name='list_api_keys'),
    path('api-key/deactivate/', deactivate_api_key, name='deactivate_api_key'),
    path('passwordless/send-token/', send_login_token, name='send_login_token'),
    path('passwordless/verify-token/', verify_login_token, name='verify_login_token'),
]

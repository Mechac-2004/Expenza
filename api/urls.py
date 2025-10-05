from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views.transaction import TransactionListCreateView, TransactionRetrieveUpdateDestroyView
from .views.auth import (
    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    ChangePasswordView
)

urlpatterns = [
    # Authentification
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('auth/profile/', UserProfileView.as_view(), name='user-profile'),
    path('auth/user/', UserProfileView.as_view(), name='current-user'),  # Alias pour compatibilité frontend
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
    
    # Transactions
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<uuid:id>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail'),
]
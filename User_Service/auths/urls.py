from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

from auths.views import (
    UserLoginView,
    UserRegistrationView, 
)

urlpatterns = [

    # Authorization actions
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),

    # Token actions
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
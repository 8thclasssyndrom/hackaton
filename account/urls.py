from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import (SignUpView, SuccessfulSignUpView, AccountActivationView, SignInView,
                           ChangePasswordView, ForgotPasswordView, ForgotPasswordCompleteView)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-up/success/', SuccessfulSignUpView.as_view(), name='success-sign_up'),
    path('activate/<str:code>/', AccountActivationView.as_view(), name='activate'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot_password/complete', ForgotPasswordCompleteView.as_view(), name='forgot-password-complete'),
]
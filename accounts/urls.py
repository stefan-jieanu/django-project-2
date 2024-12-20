from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import SubmittableLoginView, SubmittablePasswordChangeView, SignUpView

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'password-change/', SubmittablePasswordChangeView.as_view(),
        name='password_change'
    ),
    path('sign-up/', SignUpView.as_view(), name='sign_up')
]
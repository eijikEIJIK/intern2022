from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignUpView, WorkerSignUpView, CompanySignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/worker/', WorkerSignUpView.as_view(), name='worker_signup'),
    path('signup/company/', CompanySignUpView.as_view(), name='company_signup'),


    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

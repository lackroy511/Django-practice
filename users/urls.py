from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterUser, activate_account, ActivationSuccess, ActivationFailed


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html',
         extra_context={'is_active_enter': 'active'}), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('activate/<str:uidb64>/', activate_account, name='activate_account'),
    
    path('success', ActivationSuccess.as_view(), name='activation_success'),
    path('failed', ActivationFailed.as_view(), name='activation_failed')
    

]

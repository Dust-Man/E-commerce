from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import EmailLoginForm  

urlpatterns = [
    # Registro
    path('signup/', views.signup, name='signup'),
    
    # Perfil
    path('profile/', views.profile, name='profile'),
    
    # Login y logout 
    path('login/', 
         auth_views.LoginView.as_view(
             template_name='accounts/login.html',
             authentication_form=EmailLoginForm  
         ), 
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Reset de contraseña
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
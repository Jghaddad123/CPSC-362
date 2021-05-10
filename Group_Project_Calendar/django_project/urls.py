
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #empty path maches with the empty url in the cal_home to make the homepage
    path('', include('cal_home.urls')),
    path('', include('calen.urls')),
    #user app urls
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

 
    path('password-reset/',
          auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
          name='password_reset'),
    path('password-reset/done/',
          auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
          name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
          name='password_reset_confirm'),
    path('password-reset-complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
          name='password_reset_complete'),
]

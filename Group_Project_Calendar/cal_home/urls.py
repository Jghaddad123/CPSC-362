from django.urls import path
from cal_home import views

urlpatterns = [
    path('', views.landing, name ='cal_landing'),
    path('home/', views.home, name ='cal_home'),
    path('test/', views.test, name ='cal_test'),
]

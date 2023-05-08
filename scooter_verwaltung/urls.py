from django.contrib import admin
from django.urls import path
from scooter_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start, name='start'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.lougout_view, name='logout'),
    path('register-u/', views.register_view_user, name='register_user'),
    path('register-c/', views.register_view_company, name='register_company'),
    path('setup-mode/', views.mode_setup, name='setup-mode'),
    path('operative-mode/', views.mode_operative, name='operative-mode'),
    path('settings/', views.settings, name='settings'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

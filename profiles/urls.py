from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard' ),
    path('pages/login', views.dashboard, name='login' ),
    path('pages/logout', views.dashboard, name='logout' ),
    path('pages/signup', views.dashboard, name='signup' ),
    
]
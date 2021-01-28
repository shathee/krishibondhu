from django.urls import path

from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.home_view, name='home' ),
    path('home', views.home_view ),
    path('about', views.about_view, name='about' ),
    path('signup', views.signup_view, name="signup"),
    # path('signup', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.Logout, name="logout"),
    # path('dashboard/', views.dashboard, name="dashboard"),
    path('contact', views.contact_view, name='contact' ),

    path('api/home/', views.home_api_view ),
    path('api/about/', views.about_api_view ),
]
from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard' ),
    path('dashboard/questions', views.questions, name='questions' ),
    path('dashboard/questions/ask', views.ask_questions, name='ask_questions' ),
    path('profile', views.update_profile, name='profile' ),
    path('pages/login', views.dashboard, name='login' ),
    path('pages/logout', views.dashboard, name='logout' ),
    path('pages/signup', views.dashboard, name='signup' ),
    
]
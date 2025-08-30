from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'api'

urlpatterns = [
    path('save_character/', views.save_character, name='save_character'),
    path('get_characters/', views.get_characters, name='get_characters'),
    path('get_character/', views.get_character, name='get_character')
]
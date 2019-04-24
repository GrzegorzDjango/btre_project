from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # slash musi być na końcu inaczej ciemna dupa
    path('about/', views.about, name='about'),
]

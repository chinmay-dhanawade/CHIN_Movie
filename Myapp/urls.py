from django.urls import path
from . import views

app_name = 'Myapp' 

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('create/', views.movie_create, name='movie_create'),
    path('update/<str:pk>/', views.movie_update, name='movie_update'),
    path('delete/<str:pk>/', views.movie_delete, name='movie_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('add_review/<str:pk>/', views.add_review, name='add_review'),
]
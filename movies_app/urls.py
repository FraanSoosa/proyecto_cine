from django.urls import path, include
from movies_app import views

urlpatterns = [
    path('', views.get_all_movies, name='Home'),
    path('rooms', views.get_all_rooms, name='Rooms'),
    path('promotions', views.get_all_promotions, name='Promotions'),
    path('schedule', views.get_all_schedule, name='Schedule'),
    path('add-movie', views.post_movie, name='ADDMOVIE'),
    path('add-rooms', views.post_sala, name='ADDROOM'),
    path('add-schedule', views.post_schedule, name='ADDSCHEDULE'),
    path('add-promociones', views.post_promociones, name='ADDPROMOCIONES'),
    path('search', views.search, name='Search'),
]  
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('review/', views.review, name='review'),
    path('review/<int:get_id>', views.review, name='review'),
    path('knowledge/', views.knowledge, name='knowledge'),
    path('weekly/', views.weekly_recommend, name='weekly'),
    path('about/', views.about, name='about'),
    path('terms-of-service/', views.tos, name='terms-of-service'),
    path('tos/', views.tos, name='terms-of-service'),
    path('privacy-policy/', views.privacy, name='privacy-policy'),
    path('privacy/', views.privacy, name='privacy-policy'),
    path('pp/', views.privacy, name='privacy-policy'),
    path('cast/', views.cast, name='cast'),
    path('cast/<int:get_id>', views.cast, name='cast'),
    path('review/cast/<int:get_id>', views.cast, name='cast'),
    path('filter/<int:genre_var>', views.filter_page, name='filter'),
    path('filter/review/<int:get_id>', views.review, name='review'),
    path('weekly/review/<int:get_id>', views.review, name='review')
]

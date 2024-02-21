from django.urls import path
from . import views

# app_name = 'books_app'
urlpatterns = [
    path('',views.list_view, name='books'),
    path('add_book', views.add_books_views, name='add_book'),
    path('update_book/<str:slug>/',views.update_view, name='update_book'),
    path('del_book/<str:slug>/',views.delete_view,name='del_book')
]

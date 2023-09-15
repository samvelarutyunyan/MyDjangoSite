from django.contrib.auth import login
from django.urls import path

from .views import *

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  # int pk- id нашего поста
    path('about/', AboutPageView.as_view(), name='about'),  # информация о том как открывается наша страничка
    path('', Bloglist.as_view(), name='index'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('pozn/', PoznavatelniyCategory.as_view(), name='pozn'),
    path('len/', LeniviyCategory.as_view(), name='len'),
    path('superlen/', ChtotLenCategory.as_view(), name='superlen'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logount/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('user_profile/<int:ak>', UserProfile.as_view(), name='user_profile'),
    path('add_page/', addpage, name='add_page')

]

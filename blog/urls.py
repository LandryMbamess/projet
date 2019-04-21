from django.urls import path,include
from . import views
from . import forms
from .models import Article
from django.views.generic import ListView
import django_comments.urls
from django.contrib.auth import views as auth_views

app_name = 'blog'
urlpatterns = [
	path('', views.blog.as_view(), name = 'blog'),
	path('listing/', views.listing, name = 'listing'),
	path('<int:pk>/detail/', views.detailArticle.as_view(), name ='detailArticle'),
	path('editArt/<int:pk>/', views.editArticle.as_view(), name ='editArticle'),
	path('newArticle/', views.newArticle, name ='newArticle'),
	path('<int:pk>/newCom/', views.newCom, name ='newCom'),
	path('<int:pk>/del/', views.delArt.as_view(), name='delete'),
	path('inscription/', views.inscription.as_view(), name = 'inscription'),
	path('login/', auth_views.login, {'template_name':'blog/login.html'}, name = 'login'),
	path('logout/', auth_views.logout, {'next_page':'/'}, name='logout'),
	path('editCat/', views.ajoutCat.as_view(), name='ajoutCat'),

]
from articles import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name= 'home'),
    path('article/<int:article_id>', views.get_article, name= 'get_article'),
    path('article/new/', views.create_post, name= 'create_post'),
    path('registration', views.registred, name= 'regPage'),
    path('logIn', views.logIn, name= 'logIn'),
    path('logOut', views.logOut, name= 'logOut'),
]

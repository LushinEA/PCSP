from articles import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name= 'home'),
    path('article/<int:article_id>', views.get_article, name= 'get_article')
]

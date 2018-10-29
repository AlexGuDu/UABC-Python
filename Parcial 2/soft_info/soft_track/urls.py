from django.urls import include, path
from . import views

app_name = 'soft_track'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('newsw/', views.newsw, name='newsw'),
    path('newdept/', views.newdept, name='newdept'),

]

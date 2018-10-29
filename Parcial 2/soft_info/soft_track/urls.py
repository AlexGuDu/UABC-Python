from django.urls import include, path
from . import views

app_name = 'soft_track'

urlpatterns = [
    path('', views.index, name='index'),
    path('softwarebydept/<str:name>/', views.index_filter, name='index_filter'),
    path('details/<int:id>/', views.details, name='details'),
    path('newsw/', views.newsw, name='newsw'),
    path('newdept/', views.newdept, name='newdept'),

]

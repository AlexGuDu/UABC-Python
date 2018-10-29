from django.urls import include, path
from . import views

app_name = 'sci_papers'

urlpatterns = [
    path('', views.index, name='index'),
    path('cat01/', views.cat01, name='cat01'),
    path('cat02/', views.cat02, name='cat02'),
    path('cat03/', views.cat03, name='cat03'),
    path('cat04/', views.cat04, name='cat04'),
    path('cat05/', views.cat05, name='cat05'),
    path('details/<int:id>/', views.details, name='details'),
    path('create/', views.create, name='create'),
]

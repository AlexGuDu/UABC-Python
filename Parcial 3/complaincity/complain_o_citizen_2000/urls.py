from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='indexroot'),
    path('index/', views.index, name='index'),
    path('type_complaint/', views.type_complaint, name='type_complaint'),
]

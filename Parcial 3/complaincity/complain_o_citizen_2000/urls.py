from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='indexroot'),
    path('index/', views.index, name='index'),
    path('type_complaint/<int:id>', views.type_complaint, name='type_complaint'),
    path('bigcomplaint/<int:id>', views.bigcomplaint, name='bigcomplaint'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('login/', views.login, name='login'),
    path('register_f/', views.register_f, name="register_f"),
    path('login_f/', views.login_f, name="login_f"),
    path('logout/', views.logout, name="logout"),
]

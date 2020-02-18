from django.urls import path, include
from . import views


urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', views.inicio, name='inicio'),
    path('user/login/', views.login_user, name='login'),
]






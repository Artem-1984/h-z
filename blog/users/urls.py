from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout/', views.login_out, name='logout'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog.as_view()),
    path('<int:pk>/', views.PostBlog.as_view()),
    path('rev/<int:pk>/',views.AddComment.as_view(), name='comment')

]
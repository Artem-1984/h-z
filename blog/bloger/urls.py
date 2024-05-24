from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog.as_view()),
    path('<int:pk>/', views.PostBlog.as_view(), name = 'blog'),
    path('rev/<int:pk>/',views.AddComment.as_view(), name='comment'),
    path('cm/',views.AddComments.as_view(), name='cm'),
    path('a/',views.Ser.as_view(), name='a'),
    path('/',views.Ser.as_view(), name='a'),
    path('com/<int:pk>/',views.Red.as_view(), name='red'),
    path('com/<int:pk>/rep',views.Rep.as_view(), name='rep'),
    path('com/<int:pk>/del',views.Del.as_view(), name='del')


]
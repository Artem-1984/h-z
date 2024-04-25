from django.urls import path
from . import views

urlpatterns = [

    path('Главная', views.first, name ='first'),
    path('Руководство', views.City_leagers ,name=''),
    path('Контакты', views.Contact,name='Contact'),
    path('Факты', views.Facts,name='Facts'),
    path('История', views.History,name='History'),
    path('Новости', views.City_news,name='City_news'),
    path('История/Фото', views.History_fotos,name='History_fotos'),
    path('История/Люди', views.History_people,name='History_people'),
]

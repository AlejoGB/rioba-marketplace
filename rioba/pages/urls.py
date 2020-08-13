from django.urls import path
from . import views


urlpatterns = [
    path('', views.index.as_view() , name='index'),
    path('nosotros/', views.nosotros.as_view() , name='nosotros'),

]
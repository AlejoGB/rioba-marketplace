from django.urls import path
from . import views


urlpatterns = [
    path('emprens/', views.emprens.as_view() , name='emprens'),
#    path('emprens/<id>', views.emprens.as_view() , name='empren'),

]
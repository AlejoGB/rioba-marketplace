from django.urls import path
from . import views


urlpatterns = [
    path('', views.emprensListView.as_view() , name='emprens'),
    path('<pk>', views.emprensDetailView.as_view() , name='detail'),
#   path('emprens/<id>', views.emprens.as_view() , name='empren'),

]
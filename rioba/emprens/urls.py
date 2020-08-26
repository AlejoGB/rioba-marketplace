from django.urls import path
from emprens.views import ( emprensBarrioView,
                            emprensListView,
                            emprensDetailView,
                            emprensSlugView,

)


urlpatterns = [
    path('', emprensListView.as_view() , name='emprens'),
  #  path('<pk>', emprensDetailView.as_view() , name='detail'),
    path('<slug>', emprensSlugView.as_view() , name='detail'),
    path('barrio', emprensBarrioView.as_view() , name='barrio')

#    path('<pk>', views.emprensDetailView , name='detail'),
#   path('emprens/<id>', views.emprens.as_view() , name='empren'),

]
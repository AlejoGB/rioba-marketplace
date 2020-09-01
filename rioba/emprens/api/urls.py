from .views import EmprendimientoCRUDView , EmprendimientoListView
from django.urls import path


urlpatterns = [
    path('<slug>/', EmprendimientoCRUDView.as_view(), name='empren-crud' ),
    path('', EmprendimientoListView.as_view(), name='empren-list' )
]
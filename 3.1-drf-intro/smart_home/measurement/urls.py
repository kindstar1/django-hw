from django.urls import path
from .views import SensorViewSet, SensorView, CreateMesView


urlpatterns = [
    path('sensors/', SensorViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('measurements/', CreateMesView.as_view()), 
]

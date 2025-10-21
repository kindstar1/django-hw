# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import viewsets
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

class SensorViewSet(viewsets.ModelViewSet):
   
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Добавить измерение. Указываются ID датчика и температура.
class CreateMesView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

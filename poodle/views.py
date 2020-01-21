from .models import Poodle
from .serializers import PoodleSerializer
from rest_framework import generics

class PoodleList(generics.ListCreateAPIView):
    #templates/models
    queryset = Poodle.objects.all()
    serializer_class = PoodleSerializer

class PoodleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poodle.objects.all()
    serializer_class = PoodleSerializer
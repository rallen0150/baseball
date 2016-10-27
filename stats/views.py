from django.shortcuts import render
from stats.models import Master, Batting, Fielding, Pitching
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from stats.serializers import MasterSerializer, BattingSerializer, FieldingSerializer, PitchingSerializer

class MasterListCreateAPIView(ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class MasterDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class BattingListCreateAPIView(ListCreateAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer

class BattingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer

class FieldingListCreateAPIView(ListCreateAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer

class FieldingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer

class PitchingListCreateAPIView(ListCreateAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer

class PitchingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer

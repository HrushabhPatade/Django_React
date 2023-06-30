from django.shortcuts import render
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from api.models import Students

# Create your views here.

class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


from django.shortcuts import render
from post.serializers import FormSerializer
from rest_framework.generics import ListCreateAPIView
from post.models import Form

class FormList(ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

# Create your views here.

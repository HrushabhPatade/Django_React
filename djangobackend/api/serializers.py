from rest_framework import serializers
from api.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'stuname', 'email']
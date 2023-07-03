from rest_framework import serializers
from post.models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields= ['id', 'name', 'email', 'message']
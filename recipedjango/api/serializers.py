#specify the model you want to serialize here
from rest_framework import serializers
from .models import base

class baseSerializer(serializers.ModelSerializer):
    class Meta:
        model = base
        fields = '__all__'
        
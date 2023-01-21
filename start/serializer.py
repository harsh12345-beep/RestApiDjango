from dataclasses import fields
from .models import details

from rest_framework import serializers

class detailsserializer(serializers.ModelSerializer):
    class Meta:
        model = details
        fields = "__all__"
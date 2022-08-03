from rest_framework import serializers
from .models import *


class JustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"

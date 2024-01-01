from rest_framework import serializers
from .models import Tool, Tag


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

    tags = serializers.StringRelatedField(
        many=True
    )



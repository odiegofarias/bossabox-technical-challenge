from rest_framework import serializers
from .models import Tool, Tag


class ToolSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(
        many=True
    )
    
    class Meta:
        model = Tool
        fields = ('id', 'title', 'link', 'description', 'tags')





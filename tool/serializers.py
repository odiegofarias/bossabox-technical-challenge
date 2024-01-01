from rest_framework import serializers
from .models import Tool, Tag


class ToolSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    
    class Meta:
        model = Tool
        fields = ('id', 'title', 'link', 'description', 'tags')





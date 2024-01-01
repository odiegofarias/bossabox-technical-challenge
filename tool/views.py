from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Tool, Tag
from .serializers import ToolSerializer



@api_view(['GET', 'POST'])
def get_tools(request):
    if request.method == "POST":
        serializer = ToolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tool = serializer.save()
        
        for tag_name in request.data.get('tags'):
            try:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                tool.tags.add(tag)
            except Tag.DoesNotExist:
                raise NotFound()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == "GET":
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)

        return Response(serializer.data)




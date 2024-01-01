from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tool, Tag
from .serializers import ToolSerializer



@api_view(['GET'])
def get_tools(request):
    tools = Tool.objects.all()
    serializer = ToolSerializer(tools, many=True)

    return Response(serializer.data)

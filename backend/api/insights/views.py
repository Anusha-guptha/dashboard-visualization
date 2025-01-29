from django.shortcuts import render

# insights/views.py

from rest_framework import generics
from rest_framework.response import Response  
from rest_framework import status
from .models import Insight
from .serializers import InsightSerializer

class InsightList(generics.ListCreateAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=[request.data], many=True)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


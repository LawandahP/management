from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from landlord.models import Landlord


class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = '__all__'


class LandlordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        landlords = Landlord.objects.all()
        serializer = LandlordSerializer(landlords, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LandlordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LandlordDetailView(APIView):
    def get_object(self, pk):
        try:
            return Landlord.objects.get(pk=pk)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        landlord = self.get_object(pk)
        serializer = LandlordSerializer(landlord)
        return Response(serializer.data)

    def put(self, request, pk):
        landlord = self.get_object(pk)
        serializer = LandlordSerializer(landlord, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        landlord = self.get_object(pk=pk)
        landlord.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

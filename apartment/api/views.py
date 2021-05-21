from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from apartment.models import Apartment


class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

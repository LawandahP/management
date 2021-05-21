from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from unit.models import Unit


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]

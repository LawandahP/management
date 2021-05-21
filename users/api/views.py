
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'is_tenant']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 3}}

    def create(self, validated_data):
        is_tenant = validated_data.pop('is_tenant')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_tenant = is_tenant
        user.save()
        return user
        # return get_user_model().objects.create_user(**validated_data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
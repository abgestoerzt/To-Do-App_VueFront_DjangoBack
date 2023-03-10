from .models import ToDo
from rest_framework import serializers


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'name', 'deadline', 'done']

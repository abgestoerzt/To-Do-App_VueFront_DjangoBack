from django.shortcuts import render
from to_do_list.models import ToDo
from rest_framework import viewsets
from to_do_list.serializers import ToDoSerializer

# Create your views here.


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

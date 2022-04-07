import requests
from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Service, Plan, Recharge
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .serializers import ServiceSerializer, PlanSerializer, RechargeSerializer
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
   

class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class RechargeViewSet(viewsets.ModelViewSet):
    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer
    

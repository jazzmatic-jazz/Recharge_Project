from rest_framework import serializers
from .models import Service, Plan, Recharge

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name','services']


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Plan
        fields = ['url','service','amount','int_data','description']
    
class RechargeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Recharge
        fields = ['url','username','mobile','service','plan']
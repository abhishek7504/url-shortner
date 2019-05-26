from . models import FellaURL
from rest_framework import serializers


class FellaURLSerializer(serializers.Serializer):
    url = serializers.CharField(
            label='URL', 
           
        
            )

  
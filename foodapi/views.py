from django.shortcuts import render
from rest_framework.views import APIView
from foodapi.models import Food
from rest_framework.response import Response
from foodapi.serrializers import FoodSerializers
from rest_framework import status


# Create your views here.

# Create your views here.

# list, create, detail, update, delete

# localhost:8000/restaurant/dishes/

class FoodView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Food.objects.all()
        serializers = FoodSerializers(qs, many=True)
        return Response(data=serializers.data)

    def post(self, request, *args, **kwargs):
        seralizer = FoodSerializers(data=request.data)
        if seralizer.is_valid():
            Food.objects.create(**seralizer.validated_data)
            return Response(data=seralizer.data)
        else:
            return Response(data=seralizer.errors)

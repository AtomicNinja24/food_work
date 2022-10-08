from rest_framework import serializers
from foodapi.models import Food


class FoodSerializers(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    genre = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()

    def validate(self, data):
        cost = data.get("price")
        if cost<0:
            raise serializers.ValidationError("Invalid Price!")
        return data

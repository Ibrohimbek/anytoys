from rest_framework import serializers

from core.models import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = (
            'name',
            'description',
            'photo',
            'type',
            'owner_name',
            'owner_phone_number',
        )

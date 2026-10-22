from rest_framework import serializers

from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            "url",
            "id",
            "name",
            "species",
            "breed",
            "birth_date",
            "age_label",
            "description",
            "photo",
            "status",
            "intake_date",
        ]

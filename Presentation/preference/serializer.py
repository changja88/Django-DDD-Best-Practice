from rest_framework import serializers

from Context.preference.domain.preference_entity import PreferenceEntity


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceEntity
        fields = ["id", "content"]


class PreferenceWithTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceEntity
        fields = ["content", "type"]

from rest_framework import serializers

from Context.address.domain.address_level1_entity import AddressLevel1Entity
from Context.address.domain.address_level2_aggregate import AddressLevel2Aggregate


class AddressLevel1EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressLevel1Entity
        fields = ["id", "name"]


class AddressLevel2AggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressLevel2Aggregate
        fields = ["id", "name"]

from rest_framework import serializers

from Context.friend_code.domain.freind_code_aggregate import FriendCodeAggregate


class FriendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendCodeAggregate
        fields = ["code"]

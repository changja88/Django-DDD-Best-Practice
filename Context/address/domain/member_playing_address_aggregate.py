from django.db import models
from django_extensions.db.models import TimeStampedModel

from Context.address.domain.address_level1_entity import AddressLevel1Entity
from Context.address.domain.address_level2_aggregate import AddressLevel2Aggregate
from Context.member.domain.member_entity import MemberEntity


class MemberPlayingAddressAggregate(TimeStampedModel):
    member = models.ForeignKey(
        MemberEntity,
        on_delete=models.CASCADE,
        related_name="playing_address",
        db_index=True,
    )
    level1_address = models.ForeignKey(
        AddressLevel1Entity, on_delete=models.CASCADE, related_name="playing_level1_address"
    )
    level2_address = models.ForeignKey(
        AddressLevel2Aggregate, on_delete=models.CASCADE, related_name="playing_level2_address"
    )

    class Meta:
        db_table = "member_playing_address"
        verbose_name = "[member_playing_address] 사용자 활동 지역"
        verbose_name_plural = "[member_playing_address] 사용자 활동 지역"
        index_together = ("level1_address", "level2_address")

    def __str__(self) -> str:
        return f"[id: {self.id}] [level1_address: {self.level1_address}] [level2_address: {self.level2_address}]"

from django.db import models
from django_extensions.db.models import TimeStampedModel

from Context.address.domain.address_level2_aggregate import AddressLevel2Aggregate
from Context.member.domain.member_entity import MemberEntity


class MemberLivingAggregate(TimeStampedModel):
    member = models.ForeignKey(MemberEntity, on_delete=models.CASCADE, related_name="living_address", db_index=True)
    level1_address = models.ForeignKey(
        AddressLevel2Aggregate, on_delete=models.CASCADE, related_name="living_level1_address"
    )
    level2_address = models.ForeignKey(
        AddressLevel2Aggregate, on_delete=models.CASCADE, related_name="living_level2_address"
    )

    class Meta:
        db_table = "member_ling_address"
        verbose_name = "[member_ling_address] 사용자 계정"
        verbose_name_plural = "[member_ling_address] 사용자 계정"
        index_together = ("level1_address", "level2_address")

    def __str__(self) -> str:
        return f"[id: {self.id}] [level1_address: {self.level1_address}] [level2_address: {self.level2_address}]"

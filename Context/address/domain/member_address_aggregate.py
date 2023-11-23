from django.db import models
from django_extensions.db.models import TimeStampedModel

from Context.address.domain.address_level1_entity import AddressLevel1Entity
from Context.address.domain.address_level2_aggregate import AddressLevel2Aggregate
from Context.member.domain.member_entity import MemberEntity


class MemberAddressAggregate(TimeStampedModel):
    member = models.OneToOneField(MemberEntity, on_delete=models.CASCADE, related_name="member_address", db_index=True)
    living_address_level1 = models.ForeignKey(
        AddressLevel1Entity,
        related_name="member_living_address_lv1",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    living_address_level2 = models.ForeignKey(
        AddressLevel2Aggregate,
        related_name="member_living_address_lv2",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    playing_address_level1 = models.ForeignKey(
        AddressLevel1Entity,
        related_name="member_playing_address_lv1",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    playing_address_level2 = models.ForeignKey(
        AddressLevel2Aggregate,
        related_name="member_playing_address_lv2",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = "member_address"
        verbose_name = "[member_address] 멤버의 주소(거주지/활동지)"
        verbose_name_plural = "[member_address] 멤버의 주소(거주지/활동지)"

    def __str__(self) -> str:
        return (
            f"[id: {self.id}] "
            f"[living_address: {self.living_address_level1} {self.living_address_level2}]"
            f"[playing_address: {self.playing_address_level1} {self.playing_address_level2}]"
        )

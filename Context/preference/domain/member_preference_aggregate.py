from django.db import models

from Context.member.domain.member_entity import MemberEntity
from Context.preference.domain.preference_entity import PreferenceEntity


class MemberPreferenceAggregate(models.Model):
    member = models.ForeignKey(MemberEntity, on_delete=models.CASCADE, related_name="preference", db_index=True)
    preference = models.ForeignKey(PreferenceEntity, on_delete=models.CASCADE, related_name="member_preference")
    type = models.CharField("기호", max_length=32, choices=PreferenceEntity.PreferenceType, blank=False, null=False)

    class Meta:
        db_table = "member_preference"
        verbose_name = "[member_preference] 멤버 기호"
        verbose_name_plural = "[member_preference] 멤버 기호"

    def __str__(self) -> str:
        return f"[id: {self.id}] [member: {self.member.nickname}] [type: {self.type}]"

import uuid

from django.db import models

from Context.member.domain.member_entity import MemberEntity


class FriendCodeAggregate(models.Model):
    member = models.OneToOneField(
        MemberEntity, on_delete=models.CASCADE, related_name="member_friend_code", db_index=True
    )
    code = models.CharField("친구초대 코드", max_length=8, unique=True, null=False, blank=False)

    class Meta:
        db_table = "friend_code"
        verbose_name = "[friend_code] 멤버 친구초대 코드"
        verbose_name_plural = "[friend_code] 멤버 친구초대 코드"

    def __str__(self) -> str:
        return f"[id: {self.id}] [member: {self.member.nickname}] [code: {self.code}]"

    @classmethod
    def generate_friend_code(cls) -> str:
        return str(uuid.uuid4())[:5]

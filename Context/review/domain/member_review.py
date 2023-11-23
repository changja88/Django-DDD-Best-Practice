import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from djchoices import ChoiceItem, DjangoChoices

from Context.member.domain.member_entity import MemberEntity
from Context.review.enum import ReviewStatus, ReviewType


def get_s3_file_path(instance: TimeStampedModel, filename: str) -> str:
    path: str = f"file/{instance.member_id}/" f"{instance.type}_{str(uuid.uuid4())[:5]}"
    return path


class MemberReviewAggregate(TimeStampedModel):
    class ReviewType(DjangoChoices):
        face = ChoiceItem(ReviewType.face.value, "얼굴")
        body = ChoiceItem(ReviewType.body.value, "체형")
        income = ChoiceItem(ReviewType.income.value, "소득")
        car = ChoiceItem(ReviewType.car.value, "차")
        house = ChoiceItem(ReviewType.house.value, "집")
        asset = ChoiceItem(ReviewType.asset.value, "자산")
        compony = ChoiceItem(ReviewType.compony.value, "직장")
        education = ChoiceItem(ReviewType.education.value, "교육")

    class ReviewStatus(DjangoChoices):
        approved = ChoiceItem(ReviewStatus.approved.value, "인증 완료")
        rejected = ChoiceItem(ReviewStatus.rejected.value, "인증 불가")
        under_review = ChoiceItem(ReviewStatus.under_review.value, "심사 중")

    file = models.ImageField(upload_to=get_s3_file_path, blank=False, null=False)
    member = models.ForeignKey(MemberEntity, on_delete=models.DO_NOTHING, related_name="member_storage", db_index=True)
    type = models.CharField("심사 타입", max_length=16, choices=ReviewType.choices, blank=False, null=False)
    status = models.CharField("심사 상태", max_length=16, choices=ReviewStatus.choices, blank=False, null=False)

    class Meta:
        db_table = "member_review"
        verbose_name = "[member_review] 멤버 심사 심사"
        verbose_name_plural = "[member_review] 멤버 심사"

    def __str__(self) -> str:
        return f"[id: {self.id}] [member: {self.member.nickname}] [type: {self.type}] [file: {self.file.url}]"

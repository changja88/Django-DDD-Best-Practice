from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel
from djchoices import ChoiceItem, DjangoChoices

from Context.member.enum import Gender, MemberStatus


class MemberEntity(TimeStampedModel, AbstractBaseUser):
    """
    휴대폰 본인 인증후 받을 수 있는 정보 + '마지막 접근 시간' 만 담고 있음
    """

    class GenderChoices(DjangoChoices):
        female = ChoiceItem(Gender.female, "여자")
        male = ChoiceItem(Gender.male, "남자")

    class StatusChoices(DjangoChoices):
        registered = ChoiceItem(MemberStatus.registered, "가입만 완료")
        under_review = ChoiceItem(MemberStatus.under_review, "심사중")
        recommend_off = ChoiceItem(MemberStatus.recommend_off, "추천제외 상태")
        active = ChoiceItem(MemberStatus.active, "모든 심사 완료")
        inactive = ChoiceItem(MemberStatus.inactive, "탈퇴 상태")

    name = models.CharField("본명", max_length=32, blank=False, null=False)
    gender = models.CharField("성별", max_length=4, choices=GenderChoices.choices, blank=False, null=False)
    nickname = models.CharField(
        "닉네임",
        validators=[UnicodeUsernameValidator()],
        max_length=30,
        blank=False,
        null=False,
        unique=True,
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
    )
    birth_year = models.PositiveIntegerField(
        "출생 연도",
        validators=[MinValueValidator(1800), MaxValueValidator(2200)],
        blank=False,
        null=False,
    )
    status = models.CharField(
        "성별",
        choices=StatusChoices.choices,
        max_length=32,
        blank=False,
        null=False,
    )
    last_access = models.DateTimeField("마지막 접근 시간", default=timezone.now)
    is_staff = models.BooleanField("스태프 여부", default=False)
    is_superuser = models.BooleanField("슈퍼유저 여부", default=False)

    password = None
    last_login = None
    email = None

    USERNAME_FIELD = "nickname"
    REQUIRED_FIELDS = ["name", "gender", "birth_year", "status"]

    class Meta:
        db_table = "member"
        verbose_name = "[member] 사용자 계정"
        verbose_name_plural = "[member] 사용자 계정"
        index_together = ("gender", "birth_year", "status")

    def __str__(self) -> str:
        return f"[id: {self.id}] [name: {self.name}] [nickname: {self.nickname}] [status: {self.status}]"

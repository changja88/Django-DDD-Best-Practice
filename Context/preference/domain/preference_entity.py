from django.db import models
from djchoices import ChoiceItem, DjangoChoices

from Context.preference.enum import PreferenceType


class PreferenceEntity(models.Model):
    class PreferenceType(DjangoChoices):
        MBTI = ChoiceItem(PreferenceType.MBTI, PreferenceType.MBTI)
        keyword = ChoiceItem(PreferenceType.keyword, PreferenceType.keyword)
        growth = ChoiceItem(PreferenceType.growth, PreferenceType.growth)
        habit = ChoiceItem(PreferenceType.habit, PreferenceType.habit)
        date_style = ChoiceItem(PreferenceType.date_style, PreferenceType.date_style)

    content = models.CharField("내용", max_length=32, blank=False, null=False)
    type = models.CharField("기호", max_length=32, choices=PreferenceType, blank=False, null=False)
    order = models.PositiveIntegerField("노출 순위", blank=False, null=True)

    class Meta:
        db_table = "preference"
        verbose_name = "[preference] 기호"
        verbose_name_plural = "[preference] 기호"

    def __str__(self) -> str:
        return f"[id: {self.id}] [type: {self.type}] [content: {self.content}]"

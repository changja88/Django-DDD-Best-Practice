from typing import List

from Context.preference.domain.member_preference_aggregate import (
    MemberPreferenceAggregate,
)
from Context.preference.domain.preference_entity import PreferenceEntity
from Context.preference.enum import PreferenceType


class PreferenceQueryRepo:
    def get_preference_list_by(self, preference_type: PreferenceType) -> List[PreferenceEntity]:
        preference_list: List[PreferenceEntity] = (
            PreferenceEntity.objects.filter(type=preference_type.value).all().order_by("order")
        )
        return preference_list

    def get_all_member_preference_list_by(self, member_id: int) -> List[PreferenceEntity]:
        preference_list: List[PreferenceEntity] = PreferenceEntity.objects.filter(
            id__in=MemberPreferenceAggregate.objects.filter(member_id=member_id).values_list("preference_id", flat=True)
        )
        return preference_list

    def get_member_preference_list_by(self, member_id: int, preference_type: PreferenceType) -> List[PreferenceEntity]:
        preference_list: List[PreferenceEntity] = PreferenceEntity.objects.filter(
            id__in=MemberPreferenceAggregate.objects.filter(member_id=member_id, type=preference_type).values_list(
                "preference_id", flat=True
            )
        )
        return preference_list

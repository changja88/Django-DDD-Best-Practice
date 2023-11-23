from Context.preference.domain.member_preference_aggregate import (
    MemberPreferenceAggregate,
)
from Context.preference.domain.preference_entity import PreferenceEntity


class PreferenceCmdRepo:
    def register_member_preference(self, member_id: int, preference_id: int) -> None:
        preference_type = PreferenceEntity.objects.get(id=preference_id).type
        MemberPreferenceAggregate.objects.get_or_create(
            member_id=member_id,
            preference_id=preference_id,
            type=preference_type,
            defaults={"member_id": member_id, "preference_id": preference_id, "type": preference_type},
        )

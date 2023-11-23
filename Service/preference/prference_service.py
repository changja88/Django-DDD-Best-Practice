from typing import List

from Context.preference.domain.preference_entity import PreferenceEntity
from Context.preference.enum import PreferenceType
from Context.preference.repository.preference_cmd_repo import PreferenceCmdRepo
from Context.preference.repository.preference_query_repo import PreferenceQueryRepo


class PreferenceService:
    preference_query_repo: PreferenceQueryRepo = PreferenceQueryRepo()
    preference_cmd_repo: PreferenceCmdRepo = PreferenceCmdRepo()

    @classmethod
    def get_preference_list_by(cls, preferece_type: PreferenceType) -> List[PreferenceEntity]:
        perference_list: List[PreferenceEntity] = cls.preference_query_repo.get_preference_list_by(
            preference_type=preferece_type
        )
        return perference_list

    @classmethod
    def get_all_member_preference_list_by(cls, member_id: int) -> List[PreferenceEntity]:
        perference_list: List[PreferenceEntity] = cls.preference_query_repo.get_all_member_preference_list_by(member_id)
        return perference_list

    @classmethod
    def register_member_preference_by(cls, preference_id: int, member_id: int) -> None:
        cls.preference_cmd_repo.register_member_preference(member_id=member_id, preference_id=preference_id)

    @classmethod
    def get_member_preference_list_by(cls, member_id: int, preference_type: PreferenceType) -> List[PreferenceEntity]:
        perference_list: List[PreferenceEntity] = cls.preference_query_repo.get_member_preference_list_by(
            member_id=member_id, preference_type=preference_type
        )
        return perference_list

from typing import Optional

from Context.friend_code.domain.freind_code_aggregate import FriendCodeAggregate
from Context.friend_code.repository.friend_code_cmd_repo import FriendCodeCmdRepo
from Context.friend_code.repository.friend_code_query_repo import FriendCodeQueryRepo


class FriendCodeService:
    friend_code_query_repo: FriendCodeQueryRepo = FriendCodeQueryRepo()
    friend_code_cmd_repo: FriendCodeCmdRepo = FriendCodeCmdRepo()

    @classmethod
    def get_or_create_friend_cody_by(cls, member_id: int) -> Optional[FriendCodeAggregate]:
        if friend_code := cls._get_already_generated_friend_code_by(member_id):
            return friend_code
        cls._create_friend_cody_by(member_id=member_id)
        if friend_code := cls._get_already_generated_friend_code_by(member_id=member_id):
            return friend_code
        return None

    @classmethod
    def _get_already_generated_friend_code_by(cls, member_id: int) -> Optional[FriendCodeAggregate]:
        return cls.friend_code_query_repo.find_friend_code_by(member_id=member_id)

    @classmethod
    def _create_friend_cody_by(cls, member_id: int) -> None:
        cls.friend_code_cmd_repo.create_friend_code_by(member_id)

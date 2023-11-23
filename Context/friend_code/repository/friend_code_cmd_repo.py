import uuid

from Context.friend_code.domain.freind_code_aggregate import FriendCodeAggregate


class FriendCodeCmdRepo:
    def create_friend_code_by(self, member_id: int) -> None:
        FriendCodeAggregate.objects.create(member_id=member_id, code=str(uuid.uuid4())[:5])

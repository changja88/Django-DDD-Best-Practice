from typing import Optional

from Context.friend_code.domain.freind_code_aggregate import FriendCodeAggregate


class FriendCodeQueryRepo:
    def find_friend_code_by(
        self, *, member_id: Optional[int] = None, code: Optional[str] = None
    ) -> Optional[FriendCodeAggregate]:
        if member_id:
            fried_code_aggregate: FriendCodeAggregate = FriendCodeAggregate.objects.filter(member_id=member_id).first()
            return fried_code_aggregate
        elif code:
            fried_code_aggregate = FriendCodeAggregate.objects.filter(code=code).first()
            return fried_code_aggregate

        return None

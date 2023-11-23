from typing import List

from Context.review.domain.member_review import MemberReviewAggregate
from Context.review.enum import ReviewType


class ReviewQueryRepo:
    @classmethod
    def get_reviews_by(cls, member_id: int, review_type: ReviewType) -> List[MemberReviewAggregate]:
        member_reviews: List[MemberReviewAggregate] = MemberReviewAggregate.objects.filter(
            member_id=member_id, type=review_type.value
        )

        return member_reviews

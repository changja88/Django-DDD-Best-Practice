from typing import List

from Context.review.domain.member_review import MemberReviewAggregate
from Context.review.enum import ReviewType
from Context.review.repository.review_cmd_repo import (
    ChangeReviewStatusCmd,
    ReviewCmdRepo,
    StartReviewCommand,
)
from Context.review.repository.review_query_repo import ReviewQueryRepo


class ReviewService:
    review_cmd_repo: ReviewCmdRepo = ReviewCmdRepo()
    review_query_repo: ReviewQueryRepo = ReviewQueryRepo()

    @classmethod
    def start_review_by(cls, start_review_commend: StartReviewCommand) -> None:
        review: StartReviewCommand = StartReviewCommand(
            member_id=start_review_commend.member_id,
            review_type=start_review_commend.review_type,
            file=start_review_commend.file,
        )
        cls.review_cmd_repo.upload_review(review)

    @classmethod
    def get_reviews_by(cls, member_id: int, review_type: ReviewType) -> List[MemberReviewAggregate]:
        review_list: List[MemberReviewAggregate] = cls.review_query_repo.get_reviews_by(
            member_id=member_id, review_type=review_type
        )
        return review_list

    @classmethod
    def change_review_status_by(cls, change_review_status_cmd: ChangeReviewStatusCmd) -> None:
        cls.review_cmd_repo.change_review_status_by(change_review_status_cmd)

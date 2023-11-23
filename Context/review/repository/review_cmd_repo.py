from dataclasses import dataclass

from django.core.files import File

from Context.review.domain.member_review import MemberReviewAggregate
from Context.review.enum import ReviewStatus, ReviewType


@dataclass
class StartReviewCommand:
    member_id: int
    review_type: ReviewType
    file: File


@dataclass
class ChangeReviewStatusCmd:
    review_id: int
    status: ReviewStatus


class ReviewCmdRepo:
    def upload_review(self, review: StartReviewCommand) -> None:
        MemberReviewAggregate.objects.create(
            file=review.file,
            member_id=review.member_id,
            type=review.review_type.value,
            status=ReviewStatus.under_review.name,
        )

    def change_review_status_by(self, change_review_status_cmd: ChangeReviewStatusCmd) -> None:
        review: MemberReviewAggregate = MemberReviewAggregate.objects.get(id=change_review_status_cmd.review_id)
        review.status = change_review_status_cmd.status.value
        review.save()

from typing import List

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from Context.review.domain.member_review import MemberReviewAggregate
from Context.review.enum import ReviewStatus, ReviewType
from Presentation.review.serializer import ReviewSerializer
from Service.review.review_service import (
    ChangeReviewStatusCmd,
    ReviewService,
    StartReviewCommand,
)


class UploadFileTypeException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "400_BAD_REQUEST"
    default_detail = "type을 확인해주세요"


class ReviewStatusException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "400_BAD_REQUEST"
    default_detail = "review type을 확인해주세요"


class ReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        def get_review_type() -> ReviewType:
            try:
                return ReviewType(request.POST.get("type"))
            except ValueError:
                raise UploadFileTypeException()

        def create_start_review_commeand() -> StartReviewCommand:
            return StartReviewCommand(
                member_id=request.user.id, review_type=review_type, file=request.FILES.get("file")
            )

        review_type: ReviewType = get_review_type()
        ReviewService.start_review_by(start_review_commend=create_start_review_commeand())
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        def get_review_type() -> ReviewType:
            try:
                return ReviewType(request.GET.get("type"))
            except ValueError:
                raise UploadFileTypeException()

        review_list: List[MemberReviewAggregate] = ReviewService.get_reviews_by(
            member_id=request.user.id, review_type=get_review_type()
        )
        return Response(
            data=ReviewSerializer(review_list, many=True).data,
            status=status.HTTP_200_OK,
        )


class ReviewStatusView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request: Request) -> Response:
        def crate_change_review_status_cmd() -> ChangeReviewStatusCmd:
            try:
                change_review_status_cmd: ChangeReviewStatusCmd = ChangeReviewStatusCmd(
                    request.POST.get("review_id"), ReviewStatus(request.data.get("status"))
                )
            except ValueError:
                raise ReviewStatusException()
            else:
                return change_review_status_cmd

        ReviewService.change_review_status_by(crate_change_review_status_cmd())
        return Response(status=status.HTTP_200_OK)

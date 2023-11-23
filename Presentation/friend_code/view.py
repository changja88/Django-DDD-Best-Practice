from typing import Type

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from Presentation.friend_code.serializer import FriendCodeSerializer
from Service.freind_code.friend_code_service import FriendCodeService


class FriendCodeRegisterErrorExcepiton(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = "HTTP_500_INTERNAL_SERVER_ERROR"
    default_detail = "친구 초대 코드 생성 에러 발생"


class FriendCodeView(APIView):
    permission_classes = [IsAuthenticated]
    friend_code_context: Type[FriendCodeService] = FriendCodeService

    def get(self, reqeust: Request) -> Response:
        if friend_code := self.friend_code_context.get_or_create_friend_cody_by(member_id=reqeust.user.id):
            return Response(
                data={"friend-code": FriendCodeSerializer(friend_code).data},
                status=status.HTTP_200_OK,
            )
        else:
            raise FriendCodeRegisterErrorExcepiton()

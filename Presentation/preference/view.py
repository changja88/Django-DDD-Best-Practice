from typing import List, Type

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from Context.preference.domain.preference_entity import PreferenceEntity
from Context.preference.enum import PreferenceType
from Presentation.preference.serializer import (
    PreferenceSerializer,
    PreferenceWithTypeSerializer,
)
from Service.preference.prference_service import PreferenceService


class PreferenceBadRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "type을 확인해주세요"
    default_code = "HTTP_400_BAD_REQUEST"


def get_preference_or_raise(incoming_str: str) -> PreferenceType:
    try:
        preference_type: PreferenceType = PreferenceType(incoming_str)
    except ValueError:
        raise PreferenceBadRequestException()
    else:
        return preference_type


class PreferenceLookupView(APIView):
    preference_service: Type[PreferenceService] = PreferenceService

    def get(self, request: Request) -> Response:
        preference: List[PreferenceEntity] = self.preference_service.get_preference_list_by(
            get_preference_or_raise(request.GET.get("type"))
        )

        return Response(
            data=PreferenceSerializer(preference, many=True).data,
            status=status.HTTP_200_OK,
        )


class MemberPreferenceView(APIView):
    preference_service: Type[PreferenceService] = PreferenceService

    def get(self, request: Request) -> Response:
        def get_all_member_preference() -> List[PreferenceEntity]:
            preference_list: List[PreferenceEntity] = self.preference_service.get_all_member_preference_list_by(
                request.user.id
            )
            return preference_list

        def get_member_preference_by(preference_type: PreferenceType) -> List[PreferenceEntity]:
            preference_list: List[PreferenceEntity] = self.preference_service.get_member_preference_list_by(
                member_id=request.user.id, preference_type=preference_type
            )
            return preference_list

        if tye_str := request.GET.get("type"):
            member_preference_list: List[PreferenceEntity] = get_member_preference_by(tye_str)
        else:
            member_preference_list = get_all_member_preference()

        return Response(
            data=PreferenceWithTypeSerializer(member_preference_list, many=True).data,
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request) -> Response:
        self.preference_service.register_member_preference_by(
            member_id=request.user.id, preference_id=request.POST.get("preference_id")
        )
        return Response(status=status.HTTP_201_CREATED)

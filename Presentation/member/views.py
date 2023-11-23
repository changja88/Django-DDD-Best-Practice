import json
from typing import Type

from django.http import HttpResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from Service.address.member_address_register_service import MemberAddressRegisterCmd
from Service.member.member_register_service import (
    MemberRegisterCmd,
    MemberRegisterService,
)


class MemberRegisterView(APIView):
    member_register_service: Type[MemberRegisterService] = MemberRegisterService

    def post(self, request: Request) -> HttpResponse:
        # 1> 클라이언트로부터 인증 결과를 받는다
        # 2> 포트원에게 인증정보를 확인하고 사용자 정보를 받아 온다
        member_register_cmd: MemberRegisterCmd = self._create_member_register_cmd(request)
        member_address_register_cmd: MemberAddressRegisterCmd = self._create_member_address_register_cmd(request)

        member_id, token = self.member_register_service.register_member_by(
            member_register_cmd=member_register_cmd,
            member_address_register_cmd=member_address_register_cmd,
        )

        return HttpResponse(
            json.dumps({"member_id": member_id, "token": token}),
            status=status.HTTP_201_CREATED,
            content_type="application/json",
        )

    def _create_member_address_register_cmd(self, request: Request) -> MemberAddressRegisterCmd:
        member_address_register_request = MemberAddressRegisterCmd(
            living_address_level1_id=request.POST.get("living_address_level1_id"),
            living_address_level2_id=request.POST.get("living_address_level2_id"),
            playing_address_level1_id=request.POST.get("playing_address_level1_id"),
            playing_address_level2_id=request.POST.get("playing_address_level2_id"),
        )
        return member_address_register_request

    def _create_member_register_cmd(self, request: Request) -> MemberRegisterCmd:
        member_register_request: MemberRegisterCmd = MemberRegisterCmd(
            name=request.POST.get("name"),
            birth_year=request.POST.get("birth_year"),
            gender=request.POST.get("gender"),
            nickname=request.POST.get("nickname"),
        )
        return member_register_request

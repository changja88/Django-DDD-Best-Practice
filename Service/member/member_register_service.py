from typing import Tuple, Type

from django.db import transaction

from Context.member.repository.member_cmd_repo import MemberCmdRepo, MemberRegisterCmd
from Service.address.member_address_register_service import (
    MemberAddressRegisterCmd,
    MemberAddressService,
)
from Service.token.token_service import TokenService


class MemberRegisterService:
    member_cmd_repo: MemberCmdRepo = MemberCmdRepo()
    member_address_service: Type[MemberAddressService] = MemberAddressService
    token_context: Type[TokenService] = TokenService

    @classmethod
    @transaction.atomic
    def register_member_by(
        cls,
        member_register_cmd: MemberRegisterCmd,
        member_address_register_cmd: MemberAddressRegisterCmd,
    ) -> Tuple[int, str]:
        member_id: int = cls.member_cmd_repo.create_member_by(member_register_cmd)
        member_token: str = cls.token_context.generate_token_for(member_id=member_id)
        print(member_token)
        cls.member_address_service.register_member_address_by(member_id, member_address_register_cmd)
        return member_id, member_token

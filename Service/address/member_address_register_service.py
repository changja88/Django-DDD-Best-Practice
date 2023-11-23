from Context.address.repository.member_address_cmd_repo import (
    MemberAddressCmdRepo,
    MemberAddressRegisterCmd,
)


class MemberAddressService:
    member_address_cmd_repo: MemberAddressCmdRepo = MemberAddressCmdRepo()

    @classmethod
    def register_member_address_by(cls, member_id: int, member_address_register_cmd: MemberAddressRegisterCmd) -> None:
        cls.member_address_cmd_repo.register_member_address_by(member_id, member_address_register_cmd)

from dataclasses import dataclass

from Context.address.domain.member_address_aggregate import MemberAddressAggregate


@dataclass(frozen=True)
class MemberAddressRegisterCmd:
    living_address_level1_id: int
    living_address_level2_id: int
    playing_address_level1_id: int
    playing_address_level2_id: int


class MemberAddressCmdRepo:
    def register_member_address_by(self, member_id: int, member_address_register_cmd: MemberAddressRegisterCmd) -> None:
        MemberAddressAggregate.objects.create(
            member_id=member_id,
            living_address_level1_id=member_address_register_cmd.living_address_level1_id,
            living_address_level2_id=member_address_register_cmd.living_address_level2_id,
            playing_address_level1_id=member_address_register_cmd.playing_address_level1_id,
            playing_address_level2_id=member_address_register_cmd.playing_address_level2_id,
        )

from dataclasses import dataclass

from Context.member.domain.member_entity import MemberEntity
from Context.member.enum import MemberStatus


@dataclass(frozen=True)
class MemberRegisterCmd:
    name: str
    birth_year: int
    nickname: str
    gender: str


class MemberCmdRepo:
    @classmethod
    def create_member_by(cls, member_register_cmd: MemberRegisterCmd) -> int:
        member: MemberEntity = MemberEntity.objects.create(
            name=member_register_cmd.name,
            nickname=member_register_cmd.nickname,
            gender=member_register_cmd.gender,
            birth_year=member_register_cmd.birth_year,
            status=MemberStatus.registered,
        )
        member_id: int = member.id
        return member_id

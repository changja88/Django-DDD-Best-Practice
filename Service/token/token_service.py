from Context.token.repository.token_cmd_repo import TokenCmdRepo


class TokenService:
    token_cmd_repo: TokenCmdRepo = TokenCmdRepo()

    @classmethod
    def generate_token_for(cls, member_id: int) -> str:
        return cls.token_cmd_repo.generate_token_for(member_id=member_id)

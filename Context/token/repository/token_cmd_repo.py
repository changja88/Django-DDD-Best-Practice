from rest_framework.authtoken.models import Token


class TokenCmdRepo:
    @classmethod
    def generate_token_for(cls, member_id: int) -> str:
        token: Token = Token.objects.create(user_id=member_id)
        key: str = token.key
        return key

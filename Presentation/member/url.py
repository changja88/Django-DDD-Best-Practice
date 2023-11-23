from django.urls import path

from Presentation.member.views import MemberRegisterView

urlpatterns = [
    path("register", MemberRegisterView.as_view()),
    # path("check-nickname", MemberNicknameCheckView.as_view()),
]

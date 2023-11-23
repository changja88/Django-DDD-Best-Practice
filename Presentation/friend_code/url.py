from django.urls import path

from Presentation.friend_code.view import FriendCodeView

urlpatterns = [
    path("", FriendCodeView.as_view()),
]

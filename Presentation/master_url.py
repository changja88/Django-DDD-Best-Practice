from django.urls import include, path

urlpatterns = [
    path("member/", include("Presentation.member.url")),
    path("address/", include("Presentation.address.url")),
    path("preference/", include("Presentation.preference.url")),
    path("friend-code/", include("Presentation.friend_code.url")),
    path("review", include("Presentation.review.url")),
]

from django.urls import path

from Presentation.preference.view import MemberPreferenceView, PreferenceLookupView

##### begin with /preference/ ######

urlpatterns = [
    path("", PreferenceLookupView.as_view()),
    path("member", MemberPreferenceView.as_view()),
]

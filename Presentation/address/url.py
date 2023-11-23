from django.urls import path

from Presentation.address.view import AddressLookupView

##### begin with /address/ ######

urlpatterns = [
    path("lookup", AddressLookupView.as_view()),
]

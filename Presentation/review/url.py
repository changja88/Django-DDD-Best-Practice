from django.urls import path

from Presentation.review.view import ReviewStatusView, ReviewView

urlpatterns = [
    path("", ReviewView.as_view()),
    path("/status", ReviewStatusView.as_view()),
]

from enum import Enum


class ReviewType(Enum):
    face = "face"
    body = "body"
    income = "income"
    car = "car"
    house = "house"
    asset = "asset"
    compony = "compony"
    education = "education"


class ReviewStatus(Enum):
    approved = "approved"
    rejected = "rejected"
    under_review = "under_review"

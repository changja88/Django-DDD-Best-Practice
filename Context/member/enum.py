from enum import Enum


class MemberStatus(Enum):
    registered = "registered"
    under_review = "under_review"
    recommend_off = "recommend_off"
    active = "active"
    inactive = "inactive"


class Gender(Enum):
    female = "F"
    male = "M"

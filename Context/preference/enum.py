from dataclasses import dataclass
from enum import Enum


@dataclass(unsafe_hash=True)
class PreferenceType(Enum):
    MBTI = "MBTI"
    keyword = "keyword"
    growth = "growth"
    habit = "habit"
    date_style = "date_style"
    smoking = "smoking"
    drinking = "drinking"
    religion = "religion"

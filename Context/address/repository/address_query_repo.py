from dataclasses import dataclass
from typing import List, Optional

from Context.address.domain.address_level1_entity import AddressLevel1Entity
from Context.address.domain.address_level2_aggregate import AddressLevel2Aggregate


@dataclass(frozen=True)
class AddressLookupRequest:
    level: int
    level1_id: Optional[int]


class AddressQueryRepo:
    @classmethod
    def get_level1_address_list(cls) -> List[AddressLevel1Entity]:
        address_list: List[AddressLevel1Entity] = AddressLevel1Entity.objects.order_by("order").all()
        return address_list

    @classmethod
    def get_level2_address_by_level1_id(cls, level1_id: int) -> List[AddressLevel2Aggregate]:
        address_list: List[AddressLevel2Aggregate] = (
            AddressLevel2Aggregate.objects.filter(level1_id=level1_id).all().order_by("order")
        )
        return address_list

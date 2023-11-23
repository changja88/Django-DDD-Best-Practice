from typing import List

from Context.address.domain.address_level1_entity import AddressLevel1Entity
from Context.address.domain.address_level2_aggregate import AddressLevel2Aggregate
from Context.address.repository.address_query_repo import AddressQueryRepo


class AddressLookupService:
    address_lookup_repo: AddressQueryRepo = AddressQueryRepo()

    @classmethod
    def get_level1_address(cls) -> List[AddressLevel1Entity]:
        return cls.address_lookup_repo.get_level1_address_list()

    @classmethod
    def get_level2_address_by(cls, level1_address_id: int) -> List[AddressLevel2Aggregate]:
        return cls.address_lookup_repo.get_level2_address_by_level1_id(level1_id=level1_address_id)

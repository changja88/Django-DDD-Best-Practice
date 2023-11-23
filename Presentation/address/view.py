from typing import List

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from Context.address.domain.address_level1_entity import AddressLevel1Entity
from Context.address.domain.address_level2_aggregate import AddressLevel2Aggregate
from Presentation.address.serializer import (
    AddressLevel1EntitySerializer,
    AddressLevel2AggregateSerializer,
)
from Service.address.address_lookup_service import AddressLookupService


class AddressLookupBadRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "입력 정보를 확인해주세요"
    default_code = "Invalid input"


class AddressLookupView(APIView):
    address_lookup_service: type[AddressLookupService] = AddressLookupService

    def get(self, request: Request) -> Response:
        if level1_address_id := request.GET.get("level1_id"):
            return self.get_level2_address_data_by(level1_address_id)
        else:
            return self.get_level1_address_data()

    def get_level1_address_data(self) -> Response:
        address_list: List[AddressLevel1Entity] = self.address_lookup_service.get_level1_address()
        return Response(
            data={"address": AddressLevel1EntitySerializer(address_list, many=True).data},
            status=status.HTTP_200_OK,
        )

    def get_level2_address_data_by(self, level1_address_id: int) -> Response:
        address_list: List[AddressLevel2Aggregate] = self.address_lookup_service.get_level2_address_by(
            level1_address_id
        )
        return Response(
            data={"address": AddressLevel2AggregateSerializer(address_list, many=True).data},
            status=status.HTTP_200_OK,
        )

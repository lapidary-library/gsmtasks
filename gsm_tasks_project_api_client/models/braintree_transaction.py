import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BraintreeTransaction")


@attr.s(auto_attribs=True)
class BraintreeTransaction:
    """
    Attributes:
        id (str):
        url (str):
        invoice (str):
        customer (str):
        amount (str):
        timestamp (datetime.datetime):
        response (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        type (Union[Unset, str]):
        status (Union[Unset, str]):
        currency (Union[Unset, str]):
    """

    id: str
    url: str
    invoice: str
    customer: str
    amount: str
    timestamp: datetime.datetime
    response: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    type: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        invoice = self.invoice
        customer = self.customer
        amount = self.amount
        timestamp = self.timestamp.isoformat()

        response = self.response
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        type = self.type
        status = self.status
        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "invoice": invoice,
                "customer": customer,
                "amount": amount,
                "timestamp": timestamp,
                "response": response,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        invoice = d.pop("invoice")

        customer = d.pop("customer")

        amount = d.pop("amount")

        timestamp = isoparse(d.pop("timestamp"))

        response = d.pop("response")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        type = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        currency = d.pop("currency", UNSET)

        braintree_transaction = cls(
            id=id,
            url=url,
            invoice=invoice,
            customer=customer,
            amount=amount,
            timestamp=timestamp,
            response=response,
            created_at=created_at,
            updated_at=updated_at,
            type=type,
            status=status,
            currency=currency,
        )

        braintree_transaction.additional_properties = d
        return braintree_transaction

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

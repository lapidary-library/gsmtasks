import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.stripe_payment_state_enum import StripePaymentStateEnum
from ..models.stripe_state_enum import StripeStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="StripePayment")


@attr.s(auto_attribs=True)
class StripePayment:
    """
    Attributes:
        id (str):
        url (str):
        billable_account (str):
        amount (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        invoice (Optional[str]):
        state (Union[Unset, StripePaymentStateEnum]):
        stripe_id (Union[Unset, None, str]):
        stripe_state (Union[None, StripeStateEnum, Unset]):
        currency (Union[Unset, str]):
        timestamp (Union[Unset, None, datetime.datetime]):
        response (Union[Unset, None, str]):
    """

    id: str
    url: str
    billable_account: str
    amount: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    invoice: Optional[str]
    state: Union[Unset, StripePaymentStateEnum] = UNSET
    stripe_id: Union[Unset, None, str] = UNSET
    stripe_state: Union[None, StripeStateEnum, Unset] = UNSET
    currency: Union[Unset, str] = UNSET
    timestamp: Union[Unset, None, datetime.datetime] = UNSET
    response: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        billable_account = self.billable_account
        amount = self.amount
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        invoice = self.invoice
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        stripe_id = self.stripe_id
        stripe_state: Union[None, Unset, str]
        if isinstance(self.stripe_state, Unset):
            stripe_state = UNSET
        elif self.stripe_state is None:
            stripe_state = None

        elif isinstance(self.stripe_state, StripeStateEnum):
            stripe_state = UNSET
            if not isinstance(self.stripe_state, Unset):
                stripe_state = self.stripe_state.value

        else:
            stripe_state = self.stripe_state

        currency = self.currency
        timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat() if self.timestamp else None

        response = self.response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "billable_account": billable_account,
                "amount": amount,
                "created_at": created_at,
                "updated_at": updated_at,
                "invoice": invoice,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if stripe_id is not UNSET:
            field_dict["stripe_id"] = stripe_id
        if stripe_state is not UNSET:
            field_dict["stripe_state"] = stripe_state
        if currency is not UNSET:
            field_dict["currency"] = currency
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        billable_account = d.pop("billable_account")

        amount = d.pop("amount")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        invoice = d.pop("invoice")

        _state = d.pop("state", UNSET)
        state: Union[Unset, StripePaymentStateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StripePaymentStateEnum(_state)

        stripe_id = d.pop("stripe_id", UNSET)

        def _parse_stripe_state(data: object) -> Union[None, StripeStateEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _stripe_state_type_0 = data
                stripe_state_type_0: Union[Unset, StripeStateEnum]
                if isinstance(_stripe_state_type_0, Unset):
                    stripe_state_type_0 = UNSET
                else:
                    stripe_state_type_0 = StripeStateEnum(_stripe_state_type_0)

                return stripe_state_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, StripeStateEnum, Unset], data)

        stripe_state = _parse_stripe_state(d.pop("stripe_state", UNSET))

        currency = d.pop("currency", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, None, datetime.datetime]
        if _timestamp is None:
            timestamp = None
        elif isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        response = d.pop("response", UNSET)

        stripe_payment = cls(
            id=id,
            url=url,
            billable_account=billable_account,
            amount=amount,
            created_at=created_at,
            updated_at=updated_at,
            invoice=invoice,
            state=state,
            stripe_id=stripe_id,
            stripe_state=stripe_state,
            currency=currency,
            timestamp=timestamp,
            response=response,
        )

        stripe_payment.additional_properties = d
        return stripe_payment

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

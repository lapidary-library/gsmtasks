import datetime
import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.invoice_account import InvoiceAccount
from ..models.invoice_billing_method_enum import InvoiceBillingMethodEnum
from ..models.invoice_item import InvoiceItem
from ..models.invoice_state_enum import InvoiceStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Invoice")


@attr.s(auto_attribs=True)
class Invoice:
    """
    Attributes:
        id (str):
        url (str):
        account (InvoiceAccount):
        billing_method (InvoiceBillingMethodEnum):
        state (InvoiceStateEnum):
        period (List[datetime.date]): Indicates what period the price was calculated for
        total_no_vat (str):
        total_vat (str):
        total_with_vat (str):
        currency (str):
        vat (bool):
        paid_at (datetime.datetime):
        items (List[InvoiceItem]):
        pricing (str):
        confirmed_by (str):
        confirmed_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        due_date (Union[Unset, None, datetime.date]):
    """

    id: str
    url: str
    account: InvoiceAccount
    billing_method: InvoiceBillingMethodEnum
    state: InvoiceStateEnum
    period: List[datetime.date]
    total_no_vat: str
    total_vat: str
    total_with_vat: str
    currency: str
    vat: bool
    paid_at: datetime.datetime
    items: List[InvoiceItem]
    pricing: str
    confirmed_by: str
    confirmed_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    due_date: Union[Unset, None, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account.to_dict()

        billing_method = self.billing_method.value

        state = self.state.value

        period = []
        for period_item_data in self.period:
            period_item = period_item_data.isoformat()
            period.append(period_item)

        total_no_vat = self.total_no_vat
        total_vat = self.total_vat
        total_with_vat = self.total_with_vat
        currency = self.currency
        vat = self.vat
        paid_at = self.paid_at.isoformat()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        pricing = self.pricing
        confirmed_by = self.confirmed_by
        confirmed_at = self.confirmed_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        due_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat() if self.due_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "billing_method": billing_method,
                "state": state,
                "period": period,
                "total_no_vat": total_no_vat,
                "total_vat": total_vat,
                "total_with_vat": total_with_vat,
                "currency": currency,
                "vat": vat,
                "paid_at": paid_at,
                "items": items,
                "pricing": pricing,
                "confirmed_by": confirmed_by,
                "confirmed_at": confirmed_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = (None, json.dumps(self.account.to_dict()).encode(), "application/json")

        billing_method = (None, str(self.billing_method.value).encode(), "text/plain")

        state = (None, str(self.state.value).encode(), "text/plain")

        _temp_period = []
        for period_item_data in self.period:
            period_item = period_item_data.isoformat()
            _temp_period.append(period_item)
        period = (None, json.dumps(_temp_period).encode(), "application/json")

        total_no_vat = (
            self.total_no_vat
            if isinstance(self.total_no_vat, Unset)
            else (None, str(self.total_no_vat).encode(), "text/plain")
        )
        total_vat = (
            self.total_vat if isinstance(self.total_vat, Unset) else (None, str(self.total_vat).encode(), "text/plain")
        )
        total_with_vat = (
            self.total_with_vat
            if isinstance(self.total_with_vat, Unset)
            else (None, str(self.total_with_vat).encode(), "text/plain")
        )
        currency = (
            self.currency if isinstance(self.currency, Unset) else (None, str(self.currency).encode(), "text/plain")
        )
        vat = self.vat if isinstance(self.vat, Unset) else (None, str(self.vat).encode(), "text/plain")
        paid_at = self.paid_at.isoformat().encode()

        _temp_items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            _temp_items.append(items_item)
        items = (None, json.dumps(_temp_items).encode(), "application/json")

        pricing = self.pricing if isinstance(self.pricing, Unset) else (None, str(self.pricing).encode(), "text/plain")
        confirmed_by = (
            self.confirmed_by
            if isinstance(self.confirmed_by, Unset)
            else (None, str(self.confirmed_by).encode(), "text/plain")
        )
        confirmed_at = self.confirmed_at.isoformat().encode()

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        due_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat().encode() if self.due_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "billing_method": billing_method,
                "state": state,
                "period": period,
                "total_no_vat": total_no_vat,
                "total_vat": total_vat,
                "total_with_vat": total_with_vat,
                "currency": currency,
                "vat": vat,
                "paid_at": paid_at,
                "items": items,
                "pricing": pricing,
                "confirmed_by": confirmed_by,
                "confirmed_at": confirmed_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = InvoiceAccount.from_dict(d.pop("account"))

        billing_method = InvoiceBillingMethodEnum(d.pop("billing_method"))

        state = InvoiceStateEnum(d.pop("state"))

        period = []
        _period = d.pop("period")
        for period_item_data in _period:
            period_item = isoparse(period_item_data).date()

            period.append(period_item)

        total_no_vat = d.pop("total_no_vat")

        total_vat = d.pop("total_vat")

        total_with_vat = d.pop("total_with_vat")

        currency = d.pop("currency")

        vat = d.pop("vat")

        paid_at = isoparse(d.pop("paid_at"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = InvoiceItem.from_dict(items_item_data)

            items.append(items_item)

        pricing = d.pop("pricing")

        confirmed_by = d.pop("confirmed_by")

        confirmed_at = isoparse(d.pop("confirmed_at"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, None, datetime.date]
        if _due_date is None:
            due_date = None
        elif isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        invoice = cls(
            id=id,
            url=url,
            account=account,
            billing_method=billing_method,
            state=state,
            period=period,
            total_no_vat=total_no_vat,
            total_vat=total_vat,
            total_with_vat=total_with_vat,
            currency=currency,
            vat=vat,
            paid_at=paid_at,
            items=items,
            pricing=pricing,
            confirmed_by=confirmed_by,
            confirmed_at=confirmed_at,
            created_at=created_at,
            updated_at=updated_at,
            due_date=due_date,
        )

        invoice.additional_properties = d
        return invoice

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

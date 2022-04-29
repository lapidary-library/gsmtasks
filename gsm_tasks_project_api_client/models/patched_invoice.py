import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.invoice_account import InvoiceAccount
from ..models.invoice_billing_method_enum import InvoiceBillingMethodEnum
from ..models.invoice_item import InvoiceItem
from ..models.invoice_state_enum import InvoiceStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedInvoice")


@attr.s(auto_attribs=True)
class PatchedInvoice:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, InvoiceAccount]):
        billing_method (Union[Unset, InvoiceBillingMethodEnum]):
        state (Union[Unset, InvoiceStateEnum]):
        period (Union[Unset, List[datetime.date]]): Indicates what period the price was calculated for
        total_no_vat (Union[Unset, str]):
        total_vat (Union[Unset, str]):
        total_with_vat (Union[Unset, str]):
        currency (Union[Unset, str]):
        vat (Union[Unset, bool]):
        due_date (Union[Unset, None, datetime.date]):
        paid_at (Union[Unset, datetime.datetime]):
        items (Union[Unset, List[InvoiceItem]]):
        pricing (Union[Unset, str]):
        confirmed_by (Union[Unset, str]):
        confirmed_at (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, InvoiceAccount] = UNSET
    billing_method: Union[Unset, InvoiceBillingMethodEnum] = UNSET
    state: Union[Unset, InvoiceStateEnum] = UNSET
    period: Union[Unset, List[datetime.date]] = UNSET
    total_no_vat: Union[Unset, str] = UNSET
    total_vat: Union[Unset, str] = UNSET
    total_with_vat: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    vat: Union[Unset, bool] = UNSET
    due_date: Union[Unset, None, datetime.date] = UNSET
    paid_at: Union[Unset, datetime.datetime] = UNSET
    items: Union[Unset, List[InvoiceItem]] = UNSET
    pricing: Union[Unset, str] = UNSET
    confirmed_by: Union[Unset, str] = UNSET
    confirmed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        billing_method: Union[Unset, str] = UNSET
        if not isinstance(self.billing_method, Unset):
            billing_method = self.billing_method.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        period: Union[Unset, List[str]] = UNSET
        if not isinstance(self.period, Unset):
            period = []
            for period_item_data in self.period:
                period_item = period_item_data.isoformat()
                period.append(period_item)

        total_no_vat = self.total_no_vat
        total_vat = self.total_vat
        total_with_vat = self.total_with_vat
        currency = self.currency
        vat = self.vat
        due_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat() if self.due_date else None

        paid_at: Union[Unset, str] = UNSET
        if not isinstance(self.paid_at, Unset):
            paid_at = self.paid_at.isoformat()

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        pricing = self.pricing
        confirmed_by = self.confirmed_by
        confirmed_at: Union[Unset, str] = UNSET
        if not isinstance(self.confirmed_at, Unset):
            confirmed_at = self.confirmed_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if billing_method is not UNSET:
            field_dict["billing_method"] = billing_method
        if state is not UNSET:
            field_dict["state"] = state
        if period is not UNSET:
            field_dict["period"] = period
        if total_no_vat is not UNSET:
            field_dict["total_no_vat"] = total_no_vat
        if total_vat is not UNSET:
            field_dict["total_vat"] = total_vat
        if total_with_vat is not UNSET:
            field_dict["total_with_vat"] = total_with_vat
        if currency is not UNSET:
            field_dict["currency"] = currency
        if vat is not UNSET:
            field_dict["vat"] = vat
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if items is not UNSET:
            field_dict["items"] = items
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if confirmed_by is not UNSET:
            field_dict["confirmed_by"] = confirmed_by
        if confirmed_at is not UNSET:
            field_dict["confirmed_at"] = confirmed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.account, Unset):
            account = (None, json.dumps(self.account.to_dict()).encode(), "application/json")

        billing_method: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.billing_method, Unset):
            billing_method = (None, str(self.billing_method.value).encode(), "text/plain")

        state: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.state, Unset):
            state = (None, str(self.state.value).encode(), "text/plain")

        period: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.period, Unset):
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
        due_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat().encode() if self.due_date else None

        paid_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.paid_at, Unset):
            paid_at = self.paid_at.isoformat().encode()

        items: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.items, Unset):
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
        confirmed_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.confirmed_at, Unset):
            confirmed_at = self.confirmed_at.isoformat().encode()

        created_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if billing_method is not UNSET:
            field_dict["billing_method"] = billing_method
        if state is not UNSET:
            field_dict["state"] = state
        if period is not UNSET:
            field_dict["period"] = period
        if total_no_vat is not UNSET:
            field_dict["total_no_vat"] = total_no_vat
        if total_vat is not UNSET:
            field_dict["total_vat"] = total_vat
        if total_with_vat is not UNSET:
            field_dict["total_with_vat"] = total_with_vat
        if currency is not UNSET:
            field_dict["currency"] = currency
        if vat is not UNSET:
            field_dict["vat"] = vat
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if items is not UNSET:
            field_dict["items"] = items
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if confirmed_by is not UNSET:
            field_dict["confirmed_by"] = confirmed_by
        if confirmed_at is not UNSET:
            field_dict["confirmed_at"] = confirmed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        _account = d.pop("account", UNSET)
        account: Union[Unset, InvoiceAccount]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = InvoiceAccount.from_dict(_account)

        _billing_method = d.pop("billing_method", UNSET)
        billing_method: Union[Unset, InvoiceBillingMethodEnum]
        if isinstance(_billing_method, Unset):
            billing_method = UNSET
        else:
            billing_method = InvoiceBillingMethodEnum(_billing_method)

        _state = d.pop("state", UNSET)
        state: Union[Unset, InvoiceStateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = InvoiceStateEnum(_state)

        period = []
        _period = d.pop("period", UNSET)
        for period_item_data in _period or []:
            period_item = isoparse(period_item_data).date()

            period.append(period_item)

        total_no_vat = d.pop("total_no_vat", UNSET)

        total_vat = d.pop("total_vat", UNSET)

        total_with_vat = d.pop("total_with_vat", UNSET)

        currency = d.pop("currency", UNSET)

        vat = d.pop("vat", UNSET)

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, None, datetime.date]
        if _due_date is None:
            due_date = None
        elif isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        _paid_at = d.pop("paid_at", UNSET)
        paid_at: Union[Unset, datetime.datetime]
        if isinstance(_paid_at, Unset):
            paid_at = UNSET
        else:
            paid_at = isoparse(_paid_at)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = InvoiceItem.from_dict(items_item_data)

            items.append(items_item)

        pricing = d.pop("pricing", UNSET)

        confirmed_by = d.pop("confirmed_by", UNSET)

        _confirmed_at = d.pop("confirmed_at", UNSET)
        confirmed_at: Union[Unset, datetime.datetime]
        if isinstance(_confirmed_at, Unset):
            confirmed_at = UNSET
        else:
            confirmed_at = isoparse(_confirmed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        patched_invoice = cls(
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
            due_date=due_date,
            paid_at=paid_at,
            items=items,
            pricing=pricing,
            confirmed_by=confirmed_by,
            confirmed_at=confirmed_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_invoice.additional_properties = d
        return patched_invoice

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

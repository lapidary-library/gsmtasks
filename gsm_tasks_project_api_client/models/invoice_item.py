import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceItem")


@attr.s(auto_attribs=True)
class InvoiceItem:
    """
    Attributes:
        id (str):
        invoice (str):
        name (str):
        unit_price (str):
        quantity (str):
        total (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        unit (Union[Unset, str]):
    """

    id: str
    invoice: str
    name: str
    unit_price: str
    quantity: str
    total: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        invoice = self.invoice
        name = self.name
        unit_price = self.unit_price
        quantity = self.quantity
        total = self.total
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "invoice": invoice,
                "name": name,
                "unit_price": unit_price,
                "quantity": quantity,
                "total": total,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        invoice = d.pop("invoice")

        name = d.pop("name")

        unit_price = d.pop("unit_price")

        quantity = d.pop("quantity")

        total = d.pop("total")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        unit = d.pop("unit", UNSET)

        invoice_item = cls(
            id=id,
            invoice=invoice,
            name=name,
            unit_price=unit_price,
            quantity=quantity,
            total=total,
            created_at=created_at,
            updated_at=updated_at,
            unit=unit,
        )

        invoice_item.additional_properties = d
        return invoice_item

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

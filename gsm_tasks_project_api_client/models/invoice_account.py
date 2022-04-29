from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceAccount")


@attr.s(auto_attribs=True)
class InvoiceAccount:
    """
    Attributes:
        id (str):
        slug (str):
        name (str):
        registry_code (Union[Unset, str]):
        vatin (Union[Unset, str]):
        billing_reference (Union[Unset, str]):
        billing_email (Union[Unset, str]):
        billing_vat (Union[Unset, bool]):
    """

    id: str
    slug: str
    name: str
    registry_code: Union[Unset, str] = UNSET
    vatin: Union[Unset, str] = UNSET
    billing_reference: Union[Unset, str] = UNSET
    billing_email: Union[Unset, str] = UNSET
    billing_vat: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        slug = self.slug
        name = self.name
        registry_code = self.registry_code
        vatin = self.vatin
        billing_reference = self.billing_reference
        billing_email = self.billing_email
        billing_vat = self.billing_vat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
            }
        )
        if registry_code is not UNSET:
            field_dict["registry_code"] = registry_code
        if vatin is not UNSET:
            field_dict["vatin"] = vatin
        if billing_reference is not UNSET:
            field_dict["billing_reference"] = billing_reference
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email
        if billing_vat is not UNSET:
            field_dict["billing_vat"] = billing_vat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        slug = d.pop("slug")

        name = d.pop("name")

        registry_code = d.pop("registry_code", UNSET)

        vatin = d.pop("vatin", UNSET)

        billing_reference = d.pop("billing_reference", UNSET)

        billing_email = d.pop("billing_email", UNSET)

        billing_vat = d.pop("billing_vat", UNSET)

        invoice_account = cls(
            id=id,
            slug=slug,
            name=name,
            registry_code=registry_code,
            vatin=vatin,
            billing_reference=billing_reference,
            billing_email=billing_email,
            billing_vat=billing_vat,
        )

        invoice_account.additional_properties = d
        return invoice_account

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

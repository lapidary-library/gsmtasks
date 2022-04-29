import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedBraintreeCustomer")


@attr.s(auto_attribs=True)
class PatchedBraintreeCustomer:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        braintree_id (Union[Unset, None, str]):
        account (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        company (Union[Unset, str]):
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        website (Union[Unset, str]):
        vat (Union[Unset, str]):
        payment_method_nonce (Union[Unset, None, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    braintree_id: Union[Unset, None, str] = UNSET
    account: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    vat: Union[Unset, str] = UNSET
    payment_method_nonce: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        braintree_id = self.braintree_id
        account = self.account
        first_name = self.first_name
        last_name = self.last_name
        company = self.company
        email = self.email
        phone = self.phone
        website = self.website
        vat = self.vat
        payment_method_nonce = self.payment_method_nonce
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
        if braintree_id is not UNSET:
            field_dict["braintree_id"] = braintree_id
        if account is not UNSET:
            field_dict["account"] = account
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if website is not UNSET:
            field_dict["website"] = website
        if vat is not UNSET:
            field_dict["vat"] = vat
        if payment_method_nonce is not UNSET:
            field_dict["payment_method_nonce"] = payment_method_nonce
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        braintree_id = (
            self.braintree_id
            if isinstance(self.braintree_id, Unset)
            else (None, str(self.braintree_id).encode(), "text/plain")
        )
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        first_name = (
            self.first_name
            if isinstance(self.first_name, Unset)
            else (None, str(self.first_name).encode(), "text/plain")
        )
        last_name = (
            self.last_name if isinstance(self.last_name, Unset) else (None, str(self.last_name).encode(), "text/plain")
        )
        company = self.company if isinstance(self.company, Unset) else (None, str(self.company).encode(), "text/plain")
        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")
        phone = self.phone if isinstance(self.phone, Unset) else (None, str(self.phone).encode(), "text/plain")
        website = self.website if isinstance(self.website, Unset) else (None, str(self.website).encode(), "text/plain")
        vat = self.vat if isinstance(self.vat, Unset) else (None, str(self.vat).encode(), "text/plain")
        payment_method_nonce = (
            self.payment_method_nonce
            if isinstance(self.payment_method_nonce, Unset)
            else (None, str(self.payment_method_nonce).encode(), "text/plain")
        )
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
        if braintree_id is not UNSET:
            field_dict["braintree_id"] = braintree_id
        if account is not UNSET:
            field_dict["account"] = account
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if website is not UNSET:
            field_dict["website"] = website
        if vat is not UNSET:
            field_dict["vat"] = vat
        if payment_method_nonce is not UNSET:
            field_dict["payment_method_nonce"] = payment_method_nonce
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

        braintree_id = d.pop("braintree_id", UNSET)

        account = d.pop("account", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        company = d.pop("company", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        website = d.pop("website", UNSET)

        vat = d.pop("vat", UNSET)

        payment_method_nonce = d.pop("payment_method_nonce", UNSET)

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

        patched_braintree_customer = cls(
            id=id,
            url=url,
            braintree_id=braintree_id,
            account=account,
            first_name=first_name,
            last_name=last_name,
            company=company,
            email=email,
            phone=phone,
            website=website,
            vat=vat,
            payment_method_nonce=payment_method_nonce,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_braintree_customer.additional_properties = d
        return patched_braintree_customer

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

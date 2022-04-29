from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountStripePaymentMethodAttach")


@attr.s(auto_attribs=True)
class AccountStripePaymentMethodAttach:
    """
    Attributes:
        stripe_payment_method_id (str): Reflects current default payment method. For reference only.
        stripe_customer_id (Union[Unset, str]):
        set_default (Union[Unset, bool]):  Default: True.
    """

    stripe_payment_method_id: str
    stripe_customer_id: Union[Unset, str] = UNSET
    set_default: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stripe_payment_method_id = self.stripe_payment_method_id
        stripe_customer_id = self.stripe_customer_id
        set_default = self.set_default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stripe_payment_method_id": stripe_payment_method_id,
            }
        )
        if stripe_customer_id is not UNSET:
            field_dict["stripe_customer_id"] = stripe_customer_id
        if set_default is not UNSET:
            field_dict["set_default"] = set_default

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        stripe_payment_method_id = (
            self.stripe_payment_method_id
            if isinstance(self.stripe_payment_method_id, Unset)
            else (None, str(self.stripe_payment_method_id).encode(), "text/plain")
        )
        stripe_customer_id = (
            self.stripe_customer_id
            if isinstance(self.stripe_customer_id, Unset)
            else (None, str(self.stripe_customer_id).encode(), "text/plain")
        )
        set_default = (
            self.set_default
            if isinstance(self.set_default, Unset)
            else (None, str(self.set_default).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "stripe_payment_method_id": stripe_payment_method_id,
            }
        )
        if stripe_customer_id is not UNSET:
            field_dict["stripe_customer_id"] = stripe_customer_id
        if set_default is not UNSET:
            field_dict["set_default"] = set_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stripe_payment_method_id = d.pop("stripe_payment_method_id")

        stripe_customer_id = d.pop("stripe_customer_id", UNSET)

        set_default = d.pop("set_default", UNSET)

        account_stripe_payment_method_attach = cls(
            stripe_payment_method_id=stripe_payment_method_id,
            stripe_customer_id=stripe_customer_id,
            set_default=set_default,
        )

        account_stripe_payment_method_attach.additional_properties = d
        return account_stripe_payment_method_attach

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

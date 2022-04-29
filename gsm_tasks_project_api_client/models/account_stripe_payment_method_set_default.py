from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import Unset

T = TypeVar("T", bound="AccountStripePaymentMethodSetDefault")


@attr.s(auto_attribs=True)
class AccountStripePaymentMethodSetDefault:
    """
    Attributes:
        stripe_payment_method_id (str): Reflects current default payment method. For reference only.
    """

    stripe_payment_method_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stripe_payment_method_id = self.stripe_payment_method_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stripe_payment_method_id": stripe_payment_method_id,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        stripe_payment_method_id = (
            self.stripe_payment_method_id
            if isinstance(self.stripe_payment_method_id, Unset)
            else (None, str(self.stripe_payment_method_id).encode(), "text/plain")
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stripe_payment_method_id = d.pop("stripe_payment_method_id")

        account_stripe_payment_method_set_default = cls(
            stripe_payment_method_id=stripe_payment_method_id,
        )

        account_stripe_payment_method_set_default.additional_properties = d
        return account_stripe_payment_method_set_default

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

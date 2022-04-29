from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountStripeSetupIntentsGet")


@attr.s(auto_attribs=True)
class AccountStripeSetupIntentsGet:
    """
    Attributes:
        payment_method_id (Union[Unset, None, str]):
    """

    payment_method_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_method_id = self.payment_method_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_method_id is not UNSET:
            field_dict["payment_method_id"] = payment_method_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        payment_method_id = d.pop("payment_method_id", UNSET)

        account_stripe_setup_intents_get = cls(
            payment_method_id=payment_method_id,
        )

        account_stripe_setup_intents_get.additional_properties = d
        return account_stripe_setup_intents_get

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

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AccountStripeSetupAttemptGet")


@attr.s(auto_attribs=True)
class AccountStripeSetupAttemptGet:
    """
    Attributes:
        setup_attempt_id (str):
    """

    setup_attempt_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        setup_attempt_id = self.setup_attempt_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "setup_attempt_id": setup_attempt_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        setup_attempt_id = d.pop("setup_attempt_id")

        account_stripe_setup_attempt_get = cls(
            setup_attempt_id=setup_attempt_id,
        )

        account_stripe_setup_attempt_get.additional_properties = d
        return account_stripe_setup_attempt_get

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

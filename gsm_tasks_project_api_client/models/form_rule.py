import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.form_rule_rules import FormRuleRules
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormRule")


@attr.s(auto_attribs=True)
class FormRule:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        name (str):
        edit_url (str):
        rules (FormRuleRules):
        is_active (Union[Unset, bool]):
        view_url (Union[Unset, None, str]):
        pdf_url (Union[Unset, None, str]):
    """

    id: str
    url: str
    account: str
    name: str
    edit_url: str
    rules: FormRuleRules
    is_active: Union[Unset, bool] = UNSET
    view_url: Union[Unset, None, str] = UNSET
    pdf_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        name = self.name
        edit_url = self.edit_url
        rules = self.rules.to_dict()

        is_active = self.is_active
        view_url = self.view_url
        pdf_url = self.pdf_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "name": name,
                "edit_url": edit_url,
                "rules": rules,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if view_url is not UNSET:
            field_dict["view_url"] = view_url
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        edit_url = (
            self.edit_url if isinstance(self.edit_url, Unset) else (None, str(self.edit_url).encode(), "text/plain")
        )
        rules = (None, json.dumps(self.rules.to_dict()).encode(), "application/json")

        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )
        view_url = (
            self.view_url if isinstance(self.view_url, Unset) else (None, str(self.view_url).encode(), "text/plain")
        )
        pdf_url = self.pdf_url if isinstance(self.pdf_url, Unset) else (None, str(self.pdf_url).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "name": name,
                "edit_url": edit_url,
                "rules": rules,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if view_url is not UNSET:
            field_dict["view_url"] = view_url
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        name = d.pop("name")

        edit_url = d.pop("edit_url")

        rules = FormRuleRules.from_dict(d.pop("rules"))

        is_active = d.pop("is_active", UNSET)

        view_url = d.pop("view_url", UNSET)

        pdf_url = d.pop("pdf_url", UNSET)

        form_rule = cls(
            id=id,
            url=url,
            account=account,
            name=name,
            edit_url=edit_url,
            rules=rules,
            is_active=is_active,
            view_url=view_url,
            pdf_url=pdf_url,
        )

        form_rule.additional_properties = d
        return form_rule

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

import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.patched_form_rule_rules import PatchedFormRuleRules
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedFormRule")


@attr.s(auto_attribs=True)
class PatchedFormRule:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        name (Union[Unset, str]):
        edit_url (Union[Unset, str]):
        view_url (Union[Unset, None, str]):
        pdf_url (Union[Unset, None, str]):
        rules (Union[Unset, PatchedFormRuleRules]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    edit_url: Union[Unset, str] = UNSET
    view_url: Union[Unset, None, str] = UNSET
    pdf_url: Union[Unset, None, str] = UNSET
    rules: Union[Unset, PatchedFormRuleRules] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        is_active = self.is_active
        name = self.name
        edit_url = self.edit_url
        view_url = self.view_url
        pdf_url = self.pdf_url
        rules: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if name is not UNSET:
            field_dict["name"] = name
        if edit_url is not UNSET:
            field_dict["edit_url"] = edit_url
        if view_url is not UNSET:
            field_dict["view_url"] = view_url
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        edit_url = (
            self.edit_url if isinstance(self.edit_url, Unset) else (None, str(self.edit_url).encode(), "text/plain")
        )
        view_url = (
            self.view_url if isinstance(self.view_url, Unset) else (None, str(self.view_url).encode(), "text/plain")
        )
        pdf_url = self.pdf_url if isinstance(self.pdf_url, Unset) else (None, str(self.pdf_url).encode(), "text/plain")
        rules: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = (None, json.dumps(self.rules.to_dict()).encode(), "application/json")

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
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if name is not UNSET:
            field_dict["name"] = name
        if edit_url is not UNSET:
            field_dict["edit_url"] = edit_url
        if view_url is not UNSET:
            field_dict["view_url"] = view_url
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        account = d.pop("account", UNSET)

        is_active = d.pop("is_active", UNSET)

        name = d.pop("name", UNSET)

        edit_url = d.pop("edit_url", UNSET)

        view_url = d.pop("view_url", UNSET)

        pdf_url = d.pop("pdf_url", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: Union[Unset, PatchedFormRuleRules]
        if isinstance(_rules, Unset):
            rules = UNSET
        else:
            rules = PatchedFormRuleRules.from_dict(_rules)

        patched_form_rule = cls(
            id=id,
            url=url,
            account=account,
            is_active=is_active,
            name=name,
            edit_url=edit_url,
            view_url=view_url,
            pdf_url=pdf_url,
            rules=rules,
        )

        patched_form_rule.additional_properties = d
        return patched_form_rule

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.assignee_proximity_enum import AssigneeProximityEnum
from ..models.category_enum import CategoryEnum
from ..models.legacy_nested_contact import LegacyNestedContact
from ..models.legacy_task_duration import LegacyTaskDuration
from ..models.legacy_task_forms import LegacyTaskForms
from ..models.legacy_task_metafields import LegacyTaskMetafields
from ..models.nested_address import NestedAddress
from ..models.state_ef_4_enum import StateEf4Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="LegacyTask")


@attr.s(auto_attribs=True)
class LegacyTask:
    """
    Attributes:
        url (str):
        account (str):
        order_reference (str):
        orderer_name (str):
        address (NestedAddress):
        state (StateEf4Enum):
        completed_at (datetime.datetime):
        cancelled_at (datetime.datetime):
        assignee_proximity (AssigneeProximityEnum):
        created_by (str):
        issues (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        events (str):
        documents (str):
        signatures (str):
        actions (str):
        counts (str):
        id (Union[Unset, None, str]):
        order (Union[Unset, None, str]):
        route (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        category (Union[Unset, CategoryEnum]):
        orderer (Union[Unset, None, str]):
        receiver (Union[Unset, None, str]):
        contact (Union[Unset, LegacyNestedContact]): Support depreciated fields phone and email

            write to new fields phones[0] and emails[0]
        description (Union[Unset, str]):
        reference (Union[Unset, str]):
        complete_after (Union[Unset, None, datetime.datetime]):
        complete_before (Union[Unset, None, datetime.datetime]):
        scheduled_time (Union[Unset, None, datetime.datetime]):
        assignee (Union[Unset, None, str]):
        auto_assign (Union[Unset, bool]):
        position (Union[Unset, None, datetime.datetime]):
        priority (Union[Unset, int]):
        duration (Union[Unset, None, LegacyTaskDuration]):
        size (Union[Unset, None, List[int]]):
        is_full_load (Union[Unset, bool]):
        metafields (Union[Unset, LegacyTaskMetafields]):
        forms (Union[Unset, LegacyTaskForms]):
    """

    url: str
    account: str
    order_reference: str
    orderer_name: str
    address: NestedAddress
    state: StateEf4Enum
    completed_at: datetime.datetime
    cancelled_at: datetime.datetime
    assignee_proximity: AssigneeProximityEnum
    created_by: str
    issues: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    events: str
    documents: str
    signatures: str
    actions: str
    counts: str
    id: Union[Unset, None, str] = UNSET
    order: Union[Unset, None, str] = UNSET
    route: Union[Unset, None, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    category: Union[Unset, CategoryEnum] = UNSET
    orderer: Union[Unset, None, str] = UNSET
    receiver: Union[Unset, None, str] = UNSET
    contact: Union[Unset, LegacyNestedContact] = UNSET
    description: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    complete_after: Union[Unset, None, datetime.datetime] = UNSET
    complete_before: Union[Unset, None, datetime.datetime] = UNSET
    scheduled_time: Union[Unset, None, datetime.datetime] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    auto_assign: Union[Unset, bool] = UNSET
    position: Union[Unset, None, datetime.datetime] = UNSET
    priority: Union[Unset, int] = UNSET
    duration: Union[Unset, None, LegacyTaskDuration] = UNSET
    size: Union[Unset, None, List[int]] = UNSET
    is_full_load: Union[Unset, bool] = UNSET
    metafields: Union[Unset, LegacyTaskMetafields] = UNSET
    forms: Union[Unset, LegacyTaskForms] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        account = self.account
        order_reference = self.order_reference
        orderer_name = self.orderer_name
        address = self.address.to_dict()

        state = self.state.value

        completed_at = self.completed_at.isoformat()

        cancelled_at = self.cancelled_at.isoformat()

        assignee_proximity = self.assignee_proximity.value

        created_by = self.created_by
        issues = self.issues
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        events = self.events
        documents = self.documents
        signatures = self.signatures
        actions = self.actions
        counts = self.counts
        id = self.id
        order = self.order
        route = self.route
        external_id = self.external_id
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        orderer = self.orderer
        receiver = self.receiver
        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        description = self.description
        reference = self.reference
        complete_after: Union[Unset, None, str] = UNSET
        if not isinstance(self.complete_after, Unset):
            complete_after = self.complete_after.isoformat() if self.complete_after else None

        complete_before: Union[Unset, None, str] = UNSET
        if not isinstance(self.complete_before, Unset):
            complete_before = self.complete_before.isoformat() if self.complete_before else None

        scheduled_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.scheduled_time, Unset):
            scheduled_time = self.scheduled_time.isoformat() if self.scheduled_time else None

        assignee = self.assignee
        auto_assign = self.auto_assign
        position: Union[Unset, None, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.isoformat() if self.position else None

        priority = self.priority
        duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict() if self.duration else None

        size: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.size, Unset):
            if self.size is None:
                size = None
            else:
                size = self.size

        is_full_load = self.is_full_load
        metafields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metafields, Unset):
            metafields = self.metafields.to_dict()

        forms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forms, Unset):
            forms = self.forms.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "account": account,
                "order_reference": order_reference,
                "orderer_name": orderer_name,
                "address": address,
                "state": state,
                "completed_at": completed_at,
                "cancelled_at": cancelled_at,
                "assignee_proximity": assignee_proximity,
                "created_by": created_by,
                "issues": issues,
                "created_at": created_at,
                "updated_at": updated_at,
                "events": events,
                "documents": documents,
                "signatures": signatures,
                "actions": actions,
                "counts": counts,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if order is not UNSET:
            field_dict["order"] = order
        if route is not UNSET:
            field_dict["route"] = route
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if category is not UNSET:
            field_dict["category"] = category
        if orderer is not UNSET:
            field_dict["orderer"] = orderer
        if receiver is not UNSET:
            field_dict["receiver"] = receiver
        if contact is not UNSET:
            field_dict["contact"] = contact
        if description is not UNSET:
            field_dict["description"] = description
        if reference is not UNSET:
            field_dict["reference"] = reference
        if complete_after is not UNSET:
            field_dict["complete_after"] = complete_after
        if complete_before is not UNSET:
            field_dict["complete_before"] = complete_before
        if scheduled_time is not UNSET:
            field_dict["scheduled_time"] = scheduled_time
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if auto_assign is not UNSET:
            field_dict["auto_assign"] = auto_assign
        if position is not UNSET:
            field_dict["position"] = position
        if priority is not UNSET:
            field_dict["priority"] = priority
        if duration is not UNSET:
            field_dict["duration"] = duration
        if size is not UNSET:
            field_dict["size"] = size
        if is_full_load is not UNSET:
            field_dict["is_full_load"] = is_full_load
        if metafields is not UNSET:
            field_dict["metafields"] = metafields
        if forms is not UNSET:
            field_dict["forms"] = forms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        account = d.pop("account")

        order_reference = d.pop("order_reference")

        orderer_name = d.pop("orderer_name")

        address = NestedAddress.from_dict(d.pop("address"))

        state = StateEf4Enum(d.pop("state"))

        completed_at = isoparse(d.pop("completed_at"))

        cancelled_at = isoparse(d.pop("cancelled_at"))

        assignee_proximity = AssigneeProximityEnum(d.pop("assignee_proximity"))

        created_by = d.pop("created_by")

        issues = d.pop("issues")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        events = d.pop("events")

        documents = d.pop("documents")

        signatures = d.pop("signatures")

        actions = d.pop("actions")

        counts = d.pop("counts")

        id = d.pop("id", UNSET)

        order = d.pop("order", UNSET)

        route = d.pop("route", UNSET)

        external_id = d.pop("external_id", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, CategoryEnum]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CategoryEnum(_category)

        orderer = d.pop("orderer", UNSET)

        receiver = d.pop("receiver", UNSET)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, LegacyNestedContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = LegacyNestedContact.from_dict(_contact)

        description = d.pop("description", UNSET)

        reference = d.pop("reference", UNSET)

        _complete_after = d.pop("complete_after", UNSET)
        complete_after: Union[Unset, None, datetime.datetime]
        if _complete_after is None:
            complete_after = None
        elif isinstance(_complete_after, Unset):
            complete_after = UNSET
        else:
            complete_after = isoparse(_complete_after)

        _complete_before = d.pop("complete_before", UNSET)
        complete_before: Union[Unset, None, datetime.datetime]
        if _complete_before is None:
            complete_before = None
        elif isinstance(_complete_before, Unset):
            complete_before = UNSET
        else:
            complete_before = isoparse(_complete_before)

        _scheduled_time = d.pop("scheduled_time", UNSET)
        scheduled_time: Union[Unset, None, datetime.datetime]
        if _scheduled_time is None:
            scheduled_time = None
        elif isinstance(_scheduled_time, Unset):
            scheduled_time = UNSET
        else:
            scheduled_time = isoparse(_scheduled_time)

        assignee = d.pop("assignee", UNSET)

        auto_assign = d.pop("auto_assign", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, None, datetime.datetime]
        if _position is None:
            position = None
        elif isinstance(_position, Unset):
            position = UNSET
        else:
            position = isoparse(_position)

        priority = d.pop("priority", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, None, LegacyTaskDuration]
        if _duration is None:
            duration = None
        elif isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = LegacyTaskDuration.from_dict(_duration)

        size = cast(List[int], d.pop("size", UNSET))

        is_full_load = d.pop("is_full_load", UNSET)

        _metafields = d.pop("metafields", UNSET)
        metafields: Union[Unset, LegacyTaskMetafields]
        if isinstance(_metafields, Unset):
            metafields = UNSET
        else:
            metafields = LegacyTaskMetafields.from_dict(_metafields)

        _forms = d.pop("forms", UNSET)
        forms: Union[Unset, LegacyTaskForms]
        if isinstance(_forms, Unset):
            forms = UNSET
        else:
            forms = LegacyTaskForms.from_dict(_forms)

        legacy_task = cls(
            url=url,
            account=account,
            order_reference=order_reference,
            orderer_name=orderer_name,
            address=address,
            state=state,
            completed_at=completed_at,
            cancelled_at=cancelled_at,
            assignee_proximity=assignee_proximity,
            created_by=created_by,
            issues=issues,
            created_at=created_at,
            updated_at=updated_at,
            events=events,
            documents=documents,
            signatures=signatures,
            actions=actions,
            counts=counts,
            id=id,
            order=order,
            route=route,
            external_id=external_id,
            category=category,
            orderer=orderer,
            receiver=receiver,
            contact=contact,
            description=description,
            reference=reference,
            complete_after=complete_after,
            complete_before=complete_before,
            scheduled_time=scheduled_time,
            assignee=assignee,
            auto_assign=auto_assign,
            position=position,
            priority=priority,
            duration=duration,
            size=size,
            is_full_load=is_full_load,
            metafields=metafields,
            forms=forms,
        )

        legacy_task.additional_properties = d
        return legacy_task

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

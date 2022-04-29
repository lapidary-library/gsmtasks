import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.assignee_proximity_enum import AssigneeProximityEnum
from ..models.category_enum import CategoryEnum
from ..models.nested_address import NestedAddress
from ..models.nested_contact import NestedContact
from ..models.patched_task_serializer_v2_duration import PatchedTaskSerializerV2Duration
from ..models.patched_task_serializer_v2_metafields import PatchedTaskSerializerV2Metafields
from ..models.state_ef_4_enum import StateEf4Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedTaskSerializerV2")


@attr.s(auto_attribs=True)
class PatchedTaskSerializerV2:
    """
    Attributes:
        id (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        reference (Union[Unset, str]):
        barcodes (Union[Unset, List[str]]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        state (Union[Unset, StateEf4Enum]):
        assignee (Union[Unset, None, str]):
        order (Union[Unset, None, str]):
        orderer_name (Union[Unset, str]):
        route (Union[Unset, None, str]):
        category (Union[Unset, CategoryEnum]):
        contact (Union[Unset, NestedContact]):
        address (Union[Unset, NestedAddress]):
        description (Union[Unset, str]):
        complete_after (Union[Unset, None, datetime.datetime]):
        complete_before (Union[Unset, None, datetime.datetime]):
        scheduled_time (Union[Unset, None, datetime.datetime]):
        completed_at (Union[Unset, datetime.datetime]):
        cancelled_at (Union[Unset, datetime.datetime]):
        auto_assign (Union[Unset, bool]):
        assignee_proximity (Union[Unset, AssigneeProximityEnum]):
        position (Union[Unset, float]):
        priority (Union[Unset, int]):
        duration (Union[Unset, None, PatchedTaskSerializerV2Duration]):
        size (Union[Unset, None, List[int]]):
        documents (Union[Unset, List[str]]):
        signatures (Union[Unset, List[str]]):
        metafields (Union[Unset, PatchedTaskSerializerV2Metafields]):
        issues (Union[Unset, str]):
        counts (Union[Unset, str]):
        actions (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    reference: Union[Unset, str] = UNSET
    barcodes: Union[Unset, List[str]] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    state: Union[Unset, StateEf4Enum] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    order: Union[Unset, None, str] = UNSET
    orderer_name: Union[Unset, str] = UNSET
    route: Union[Unset, None, str] = UNSET
    category: Union[Unset, CategoryEnum] = UNSET
    contact: Union[Unset, NestedContact] = UNSET
    address: Union[Unset, NestedAddress] = UNSET
    description: Union[Unset, str] = UNSET
    complete_after: Union[Unset, None, datetime.datetime] = UNSET
    complete_before: Union[Unset, None, datetime.datetime] = UNSET
    scheduled_time: Union[Unset, None, datetime.datetime] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    cancelled_at: Union[Unset, datetime.datetime] = UNSET
    auto_assign: Union[Unset, bool] = UNSET
    assignee_proximity: Union[Unset, AssigneeProximityEnum] = UNSET
    position: Union[Unset, float] = UNSET
    priority: Union[Unset, int] = UNSET
    duration: Union[Unset, None, PatchedTaskSerializerV2Duration] = UNSET
    size: Union[Unset, None, List[int]] = UNSET
    documents: Union[Unset, List[str]] = UNSET
    signatures: Union[Unset, List[str]] = UNSET
    metafields: Union[Unset, PatchedTaskSerializerV2Metafields] = UNSET
    issues: Union[Unset, str] = UNSET
    counts: Union[Unset, str] = UNSET
    actions: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        external_id = self.external_id
        reference = self.reference
        barcodes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.barcodes, Unset):
            barcodes = self.barcodes

        url = self.url
        account = self.account
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        assignee = self.assignee
        order = self.order
        orderer_name = self.orderer_name
        route = self.route
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        description = self.description
        complete_after: Union[Unset, None, str] = UNSET
        if not isinstance(self.complete_after, Unset):
            complete_after = self.complete_after.isoformat() if self.complete_after else None

        complete_before: Union[Unset, None, str] = UNSET
        if not isinstance(self.complete_before, Unset):
            complete_before = self.complete_before.isoformat() if self.complete_before else None

        scheduled_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.scheduled_time, Unset):
            scheduled_time = self.scheduled_time.isoformat() if self.scheduled_time else None

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        cancelled_at: Union[Unset, str] = UNSET
        if not isinstance(self.cancelled_at, Unset):
            cancelled_at = self.cancelled_at.isoformat()

        auto_assign = self.auto_assign
        assignee_proximity: Union[Unset, str] = UNSET
        if not isinstance(self.assignee_proximity, Unset):
            assignee_proximity = self.assignee_proximity.value

        position = self.position
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

        documents: Union[Unset, List[str]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents

        signatures: Union[Unset, List[str]] = UNSET
        if not isinstance(self.signatures, Unset):
            signatures = self.signatures

        metafields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metafields, Unset):
            metafields = self.metafields.to_dict()

        issues = self.issues
        counts = self.counts
        actions = self.actions
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
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if barcodes is not UNSET:
            field_dict["barcodes"] = barcodes
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if state is not UNSET:
            field_dict["state"] = state
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if order is not UNSET:
            field_dict["order"] = order
        if orderer_name is not UNSET:
            field_dict["orderer_name"] = orderer_name
        if route is not UNSET:
            field_dict["route"] = route
        if category is not UNSET:
            field_dict["category"] = category
        if contact is not UNSET:
            field_dict["contact"] = contact
        if address is not UNSET:
            field_dict["address"] = address
        if description is not UNSET:
            field_dict["description"] = description
        if complete_after is not UNSET:
            field_dict["complete_after"] = complete_after
        if complete_before is not UNSET:
            field_dict["complete_before"] = complete_before
        if scheduled_time is not UNSET:
            field_dict["scheduled_time"] = scheduled_time
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if auto_assign is not UNSET:
            field_dict["auto_assign"] = auto_assign
        if assignee_proximity is not UNSET:
            field_dict["assignee_proximity"] = assignee_proximity
        if position is not UNSET:
            field_dict["position"] = position
        if priority is not UNSET:
            field_dict["priority"] = priority
        if duration is not UNSET:
            field_dict["duration"] = duration
        if size is not UNSET:
            field_dict["size"] = size
        if documents is not UNSET:
            field_dict["documents"] = documents
        if signatures is not UNSET:
            field_dict["signatures"] = signatures
        if metafields is not UNSET:
            field_dict["metafields"] = metafields
        if issues is not UNSET:
            field_dict["issues"] = issues
        if counts is not UNSET:
            field_dict["counts"] = counts
        if actions is not UNSET:
            field_dict["actions"] = actions
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        external_id = d.pop("external_id", UNSET)

        reference = d.pop("reference", UNSET)

        barcodes = cast(List[str], d.pop("barcodes", UNSET))

        url = d.pop("url", UNSET)

        account = d.pop("account", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StateEf4Enum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateEf4Enum(_state)

        assignee = d.pop("assignee", UNSET)

        order = d.pop("order", UNSET)

        orderer_name = d.pop("orderer_name", UNSET)

        route = d.pop("route", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, CategoryEnum]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CategoryEnum(_category)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, NestedContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = NestedContact.from_dict(_contact)

        _address = d.pop("address", UNSET)
        address: Union[Unset, NestedAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = NestedAddress.from_dict(_address)

        description = d.pop("description", UNSET)

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

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _cancelled_at = d.pop("cancelled_at", UNSET)
        cancelled_at: Union[Unset, datetime.datetime]
        if isinstance(_cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = isoparse(_cancelled_at)

        auto_assign = d.pop("auto_assign", UNSET)

        _assignee_proximity = d.pop("assignee_proximity", UNSET)
        assignee_proximity: Union[Unset, AssigneeProximityEnum]
        if isinstance(_assignee_proximity, Unset):
            assignee_proximity = UNSET
        else:
            assignee_proximity = AssigneeProximityEnum(_assignee_proximity)

        position = d.pop("position", UNSET)

        priority = d.pop("priority", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, None, PatchedTaskSerializerV2Duration]
        if _duration is None:
            duration = None
        elif isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = PatchedTaskSerializerV2Duration.from_dict(_duration)

        size = cast(List[int], d.pop("size", UNSET))

        documents = cast(List[str], d.pop("documents", UNSET))

        signatures = cast(List[str], d.pop("signatures", UNSET))

        _metafields = d.pop("metafields", UNSET)
        metafields: Union[Unset, PatchedTaskSerializerV2Metafields]
        if isinstance(_metafields, Unset):
            metafields = UNSET
        else:
            metafields = PatchedTaskSerializerV2Metafields.from_dict(_metafields)

        issues = d.pop("issues", UNSET)

        counts = d.pop("counts", UNSET)

        actions = d.pop("actions", UNSET)

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

        patched_task_serializer_v2 = cls(
            id=id,
            external_id=external_id,
            reference=reference,
            barcodes=barcodes,
            url=url,
            account=account,
            state=state,
            assignee=assignee,
            order=order,
            orderer_name=orderer_name,
            route=route,
            category=category,
            contact=contact,
            address=address,
            description=description,
            complete_after=complete_after,
            complete_before=complete_before,
            scheduled_time=scheduled_time,
            completed_at=completed_at,
            cancelled_at=cancelled_at,
            auto_assign=auto_assign,
            assignee_proximity=assignee_proximity,
            position=position,
            priority=priority,
            duration=duration,
            size=size,
            documents=documents,
            signatures=signatures,
            metafields=metafields,
            issues=issues,
            counts=counts,
            actions=actions,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_task_serializer_v2.additional_properties = d
        return patched_task_serializer_v2

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.assignee_proximity_enum import AssigneeProximityEnum
from ..models.category_enum import CategoryEnum
from ..models.nested_address import NestedAddress
from ..models.nested_contact import NestedContact
from ..models.state_ef_4_enum import StateEf4Enum
from ..models.task_serializer_v2_duration import TaskSerializerV2Duration
from ..models.task_serializer_v2_metafields import TaskSerializerV2Metafields
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskSerializerV2")


@attr.s(auto_attribs=True)
class TaskSerializerV2:
    """
    Attributes:
        url (str):
        account (str):
        state (StateEf4Enum):
        orderer_name (str):
        address (NestedAddress):
        completed_at (datetime.datetime):
        cancelled_at (datetime.datetime):
        assignee_proximity (AssigneeProximityEnum):
        issues (str):
        counts (str):
        actions (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        id (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        reference (Union[Unset, str]):
        barcodes (Union[Unset, List[str]]):
        assignee (Union[Unset, None, str]):
        order (Union[Unset, None, str]):
        route (Union[Unset, None, str]):
        category (Union[Unset, CategoryEnum]):
        contact (Union[Unset, NestedContact]):
        description (Union[Unset, str]):
        complete_after (Union[Unset, None, datetime.datetime]):
        complete_before (Union[Unset, None, datetime.datetime]):
        scheduled_time (Union[Unset, None, datetime.datetime]):
        auto_assign (Union[Unset, bool]):
        position (Union[Unset, float]):
        priority (Union[Unset, int]):
        duration (Union[Unset, None, TaskSerializerV2Duration]):
        size (Union[Unset, None, List[int]]):
        documents (Union[Unset, List[str]]):
        signatures (Union[Unset, List[str]]):
        metafields (Union[Unset, TaskSerializerV2Metafields]):
    """

    url: str
    account: str
    state: StateEf4Enum
    orderer_name: str
    address: NestedAddress
    completed_at: datetime.datetime
    cancelled_at: datetime.datetime
    assignee_proximity: AssigneeProximityEnum
    issues: str
    counts: str
    actions: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, None, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    reference: Union[Unset, str] = UNSET
    barcodes: Union[Unset, List[str]] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    order: Union[Unset, None, str] = UNSET
    route: Union[Unset, None, str] = UNSET
    category: Union[Unset, CategoryEnum] = UNSET
    contact: Union[Unset, NestedContact] = UNSET
    description: Union[Unset, str] = UNSET
    complete_after: Union[Unset, None, datetime.datetime] = UNSET
    complete_before: Union[Unset, None, datetime.datetime] = UNSET
    scheduled_time: Union[Unset, None, datetime.datetime] = UNSET
    auto_assign: Union[Unset, bool] = UNSET
    position: Union[Unset, float] = UNSET
    priority: Union[Unset, int] = UNSET
    duration: Union[Unset, None, TaskSerializerV2Duration] = UNSET
    size: Union[Unset, None, List[int]] = UNSET
    documents: Union[Unset, List[str]] = UNSET
    signatures: Union[Unset, List[str]] = UNSET
    metafields: Union[Unset, TaskSerializerV2Metafields] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        account = self.account
        state = self.state.value

        orderer_name = self.orderer_name
        address = self.address.to_dict()

        completed_at = self.completed_at.isoformat()

        cancelled_at = self.cancelled_at.isoformat()

        assignee_proximity = self.assignee_proximity.value

        issues = self.issues
        counts = self.counts
        actions = self.actions
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id
        external_id = self.external_id
        reference = self.reference
        barcodes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.barcodes, Unset):
            barcodes = self.barcodes

        assignee = self.assignee
        order = self.order
        route = self.route
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

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

        auto_assign = self.auto_assign
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "account": account,
                "state": state,
                "orderer_name": orderer_name,
                "address": address,
                "completed_at": completed_at,
                "cancelled_at": cancelled_at,
                "assignee_proximity": assignee_proximity,
                "issues": issues,
                "counts": counts,
                "actions": actions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if barcodes is not UNSET:
            field_dict["barcodes"] = barcodes
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if order is not UNSET:
            field_dict["order"] = order
        if route is not UNSET:
            field_dict["route"] = route
        if category is not UNSET:
            field_dict["category"] = category
        if contact is not UNSET:
            field_dict["contact"] = contact
        if description is not UNSET:
            field_dict["description"] = description
        if complete_after is not UNSET:
            field_dict["complete_after"] = complete_after
        if complete_before is not UNSET:
            field_dict["complete_before"] = complete_before
        if scheduled_time is not UNSET:
            field_dict["scheduled_time"] = scheduled_time
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
        if documents is not UNSET:
            field_dict["documents"] = documents
        if signatures is not UNSET:
            field_dict["signatures"] = signatures
        if metafields is not UNSET:
            field_dict["metafields"] = metafields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        account = d.pop("account")

        state = StateEf4Enum(d.pop("state"))

        orderer_name = d.pop("orderer_name")

        address = NestedAddress.from_dict(d.pop("address"))

        completed_at = isoparse(d.pop("completed_at"))

        cancelled_at = isoparse(d.pop("cancelled_at"))

        assignee_proximity = AssigneeProximityEnum(d.pop("assignee_proximity"))

        issues = d.pop("issues")

        counts = d.pop("counts")

        actions = d.pop("actions")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        id = d.pop("id", UNSET)

        external_id = d.pop("external_id", UNSET)

        reference = d.pop("reference", UNSET)

        barcodes = cast(List[str], d.pop("barcodes", UNSET))

        assignee = d.pop("assignee", UNSET)

        order = d.pop("order", UNSET)

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

        auto_assign = d.pop("auto_assign", UNSET)

        position = d.pop("position", UNSET)

        priority = d.pop("priority", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, None, TaskSerializerV2Duration]
        if _duration is None:
            duration = None
        elif isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = TaskSerializerV2Duration.from_dict(_duration)

        size = cast(List[int], d.pop("size", UNSET))

        documents = cast(List[str], d.pop("documents", UNSET))

        signatures = cast(List[str], d.pop("signatures", UNSET))

        _metafields = d.pop("metafields", UNSET)
        metafields: Union[Unset, TaskSerializerV2Metafields]
        if isinstance(_metafields, Unset):
            metafields = UNSET
        else:
            metafields = TaskSerializerV2Metafields.from_dict(_metafields)

        task_serializer_v2 = cls(
            url=url,
            account=account,
            state=state,
            orderer_name=orderer_name,
            address=address,
            completed_at=completed_at,
            cancelled_at=cancelled_at,
            assignee_proximity=assignee_proximity,
            issues=issues,
            counts=counts,
            actions=actions,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            external_id=external_id,
            reference=reference,
            barcodes=barcodes,
            assignee=assignee,
            order=order,
            route=route,
            category=category,
            contact=contact,
            description=description,
            complete_after=complete_after,
            complete_before=complete_before,
            scheduled_time=scheduled_time,
            auto_assign=auto_assign,
            position=position,
            priority=priority,
            duration=duration,
            size=size,
            documents=documents,
            signatures=signatures,
            metafields=metafields,
        )

        task_serializer_v2.additional_properties = d
        return task_serializer_v2

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

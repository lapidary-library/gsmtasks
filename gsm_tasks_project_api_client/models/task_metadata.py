import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.task_metadata_accepted_duration import TaskMetadataAcceptedDuration
from ..models.task_metadata_active_duration import TaskMetadataActiveDuration
from ..models.task_metadata_assigned_duration import TaskMetadataAssignedDuration
from ..models.task_metadata_cancelled_duration import TaskMetadataCancelledDuration
from ..models.task_metadata_completed_duration import TaskMetadataCompletedDuration
from ..models.task_metadata_failed_duration import TaskMetadataFailedDuration
from ..models.task_metadata_transit_duration import TaskMetadataTransitDuration
from ..models.task_metadata_unassigned_duration import TaskMetadataUnassignedDuration
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskMetadata")


@attr.s(auto_attribs=True)
class TaskMetadata:
    """
    Attributes:
        id (str):
        url (str):
        task (str):
        events_count (Union[Unset, None, int]):
        task_event_notes_count (Union[Unset, None, int]):
        documents_count (Union[Unset, None, int]):
        signatures_count (Union[Unset, None, int]):
        forms_count (Union[Unset, None, int]):
        forms_completed_count (Union[Unset, None, int]):
        last_task_event_notes (Union[Unset, str]):
        unassigned_duration (Union[Unset, None, TaskMetadataUnassignedDuration]):
        assigned_duration (Union[Unset, None, TaskMetadataAssignedDuration]):
        accepted_duration (Union[Unset, None, TaskMetadataAcceptedDuration]):
        transit_duration (Union[Unset, None, TaskMetadataTransitDuration]):
        active_duration (Union[Unset, None, TaskMetadataActiveDuration]):
        completed_duration (Union[Unset, None, TaskMetadataCompletedDuration]):
        failed_duration (Union[Unset, None, TaskMetadataFailedDuration]):
        cancelled_duration (Union[Unset, None, TaskMetadataCancelledDuration]):
        unassigned_distance (Union[Unset, None, int]):
        assigned_distance (Union[Unset, None, int]):
        accepted_distance (Union[Unset, None, int]):
        transit_distance (Union[Unset, None, int]):
        active_distance (Union[Unset, None, int]):
        completed_distance (Union[Unset, None, int]):
        failed_distance (Union[Unset, None, int]):
        cancelled_distance (Union[Unset, None, int]):
        last_unassigned_at (Union[Unset, None, datetime.datetime]):
        last_assigned_at (Union[Unset, None, datetime.datetime]):
        last_accepted_at (Union[Unset, None, datetime.datetime]):
        last_transit_at (Union[Unset, None, datetime.datetime]):
        last_active_at (Union[Unset, None, datetime.datetime]):
        last_completed_at (Union[Unset, None, datetime.datetime]):
        last_failed_at (Union[Unset, None, datetime.datetime]):
        last_cancelled_at (Union[Unset, None, datetime.datetime]):
    """

    id: str
    url: str
    task: str
    events_count: Union[Unset, None, int] = UNSET
    task_event_notes_count: Union[Unset, None, int] = UNSET
    documents_count: Union[Unset, None, int] = UNSET
    signatures_count: Union[Unset, None, int] = UNSET
    forms_count: Union[Unset, None, int] = UNSET
    forms_completed_count: Union[Unset, None, int] = UNSET
    last_task_event_notes: Union[Unset, str] = UNSET
    unassigned_duration: Union[Unset, None, TaskMetadataUnassignedDuration] = UNSET
    assigned_duration: Union[Unset, None, TaskMetadataAssignedDuration] = UNSET
    accepted_duration: Union[Unset, None, TaskMetadataAcceptedDuration] = UNSET
    transit_duration: Union[Unset, None, TaskMetadataTransitDuration] = UNSET
    active_duration: Union[Unset, None, TaskMetadataActiveDuration] = UNSET
    completed_duration: Union[Unset, None, TaskMetadataCompletedDuration] = UNSET
    failed_duration: Union[Unset, None, TaskMetadataFailedDuration] = UNSET
    cancelled_duration: Union[Unset, None, TaskMetadataCancelledDuration] = UNSET
    unassigned_distance: Union[Unset, None, int] = UNSET
    assigned_distance: Union[Unset, None, int] = UNSET
    accepted_distance: Union[Unset, None, int] = UNSET
    transit_distance: Union[Unset, None, int] = UNSET
    active_distance: Union[Unset, None, int] = UNSET
    completed_distance: Union[Unset, None, int] = UNSET
    failed_distance: Union[Unset, None, int] = UNSET
    cancelled_distance: Union[Unset, None, int] = UNSET
    last_unassigned_at: Union[Unset, None, datetime.datetime] = UNSET
    last_assigned_at: Union[Unset, None, datetime.datetime] = UNSET
    last_accepted_at: Union[Unset, None, datetime.datetime] = UNSET
    last_transit_at: Union[Unset, None, datetime.datetime] = UNSET
    last_active_at: Union[Unset, None, datetime.datetime] = UNSET
    last_completed_at: Union[Unset, None, datetime.datetime] = UNSET
    last_failed_at: Union[Unset, None, datetime.datetime] = UNSET
    last_cancelled_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        task = self.task
        events_count = self.events_count
        task_event_notes_count = self.task_event_notes_count
        documents_count = self.documents_count
        signatures_count = self.signatures_count
        forms_count = self.forms_count
        forms_completed_count = self.forms_completed_count
        last_task_event_notes = self.last_task_event_notes
        unassigned_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.unassigned_duration, Unset):
            unassigned_duration = self.unassigned_duration.to_dict() if self.unassigned_duration else None

        assigned_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_duration, Unset):
            assigned_duration = self.assigned_duration.to_dict() if self.assigned_duration else None

        accepted_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.accepted_duration, Unset):
            accepted_duration = self.accepted_duration.to_dict() if self.accepted_duration else None

        transit_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transit_duration, Unset):
            transit_duration = self.transit_duration.to_dict() if self.transit_duration else None

        active_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.active_duration, Unset):
            active_duration = self.active_duration.to_dict() if self.active_duration else None

        completed_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.completed_duration, Unset):
            completed_duration = self.completed_duration.to_dict() if self.completed_duration else None

        failed_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.failed_duration, Unset):
            failed_duration = self.failed_duration.to_dict() if self.failed_duration else None

        cancelled_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.cancelled_duration, Unset):
            cancelled_duration = self.cancelled_duration.to_dict() if self.cancelled_duration else None

        unassigned_distance = self.unassigned_distance
        assigned_distance = self.assigned_distance
        accepted_distance = self.accepted_distance
        transit_distance = self.transit_distance
        active_distance = self.active_distance
        completed_distance = self.completed_distance
        failed_distance = self.failed_distance
        cancelled_distance = self.cancelled_distance
        last_unassigned_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_unassigned_at, Unset):
            last_unassigned_at = self.last_unassigned_at.isoformat() if self.last_unassigned_at else None

        last_assigned_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_assigned_at, Unset):
            last_assigned_at = self.last_assigned_at.isoformat() if self.last_assigned_at else None

        last_accepted_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_accepted_at, Unset):
            last_accepted_at = self.last_accepted_at.isoformat() if self.last_accepted_at else None

        last_transit_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_transit_at, Unset):
            last_transit_at = self.last_transit_at.isoformat() if self.last_transit_at else None

        last_active_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_active_at, Unset):
            last_active_at = self.last_active_at.isoformat() if self.last_active_at else None

        last_completed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_completed_at, Unset):
            last_completed_at = self.last_completed_at.isoformat() if self.last_completed_at else None

        last_failed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_failed_at, Unset):
            last_failed_at = self.last_failed_at.isoformat() if self.last_failed_at else None

        last_cancelled_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_cancelled_at, Unset):
            last_cancelled_at = self.last_cancelled_at.isoformat() if self.last_cancelled_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "task": task,
            }
        )
        if events_count is not UNSET:
            field_dict["events_count"] = events_count
        if task_event_notes_count is not UNSET:
            field_dict["task_event_notes_count"] = task_event_notes_count
        if documents_count is not UNSET:
            field_dict["documents_count"] = documents_count
        if signatures_count is not UNSET:
            field_dict["signatures_count"] = signatures_count
        if forms_count is not UNSET:
            field_dict["forms_count"] = forms_count
        if forms_completed_count is not UNSET:
            field_dict["forms_completed_count"] = forms_completed_count
        if last_task_event_notes is not UNSET:
            field_dict["last_task_event_notes"] = last_task_event_notes
        if unassigned_duration is not UNSET:
            field_dict["unassigned_duration"] = unassigned_duration
        if assigned_duration is not UNSET:
            field_dict["assigned_duration"] = assigned_duration
        if accepted_duration is not UNSET:
            field_dict["accepted_duration"] = accepted_duration
        if transit_duration is not UNSET:
            field_dict["transit_duration"] = transit_duration
        if active_duration is not UNSET:
            field_dict["active_duration"] = active_duration
        if completed_duration is not UNSET:
            field_dict["completed_duration"] = completed_duration
        if failed_duration is not UNSET:
            field_dict["failed_duration"] = failed_duration
        if cancelled_duration is not UNSET:
            field_dict["cancelled_duration"] = cancelled_duration
        if unassigned_distance is not UNSET:
            field_dict["unassigned_distance"] = unassigned_distance
        if assigned_distance is not UNSET:
            field_dict["assigned_distance"] = assigned_distance
        if accepted_distance is not UNSET:
            field_dict["accepted_distance"] = accepted_distance
        if transit_distance is not UNSET:
            field_dict["transit_distance"] = transit_distance
        if active_distance is not UNSET:
            field_dict["active_distance"] = active_distance
        if completed_distance is not UNSET:
            field_dict["completed_distance"] = completed_distance
        if failed_distance is not UNSET:
            field_dict["failed_distance"] = failed_distance
        if cancelled_distance is not UNSET:
            field_dict["cancelled_distance"] = cancelled_distance
        if last_unassigned_at is not UNSET:
            field_dict["last_unassigned_at"] = last_unassigned_at
        if last_assigned_at is not UNSET:
            field_dict["last_assigned_at"] = last_assigned_at
        if last_accepted_at is not UNSET:
            field_dict["last_accepted_at"] = last_accepted_at
        if last_transit_at is not UNSET:
            field_dict["last_transit_at"] = last_transit_at
        if last_active_at is not UNSET:
            field_dict["last_active_at"] = last_active_at
        if last_completed_at is not UNSET:
            field_dict["last_completed_at"] = last_completed_at
        if last_failed_at is not UNSET:
            field_dict["last_failed_at"] = last_failed_at
        if last_cancelled_at is not UNSET:
            field_dict["last_cancelled_at"] = last_cancelled_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        task = d.pop("task")

        events_count = d.pop("events_count", UNSET)

        task_event_notes_count = d.pop("task_event_notes_count", UNSET)

        documents_count = d.pop("documents_count", UNSET)

        signatures_count = d.pop("signatures_count", UNSET)

        forms_count = d.pop("forms_count", UNSET)

        forms_completed_count = d.pop("forms_completed_count", UNSET)

        last_task_event_notes = d.pop("last_task_event_notes", UNSET)

        _unassigned_duration = d.pop("unassigned_duration", UNSET)
        unassigned_duration: Union[Unset, None, TaskMetadataUnassignedDuration]
        if _unassigned_duration is None:
            unassigned_duration = None
        elif isinstance(_unassigned_duration, Unset):
            unassigned_duration = UNSET
        else:
            unassigned_duration = TaskMetadataUnassignedDuration.from_dict(_unassigned_duration)

        _assigned_duration = d.pop("assigned_duration", UNSET)
        assigned_duration: Union[Unset, None, TaskMetadataAssignedDuration]
        if _assigned_duration is None:
            assigned_duration = None
        elif isinstance(_assigned_duration, Unset):
            assigned_duration = UNSET
        else:
            assigned_duration = TaskMetadataAssignedDuration.from_dict(_assigned_duration)

        _accepted_duration = d.pop("accepted_duration", UNSET)
        accepted_duration: Union[Unset, None, TaskMetadataAcceptedDuration]
        if _accepted_duration is None:
            accepted_duration = None
        elif isinstance(_accepted_duration, Unset):
            accepted_duration = UNSET
        else:
            accepted_duration = TaskMetadataAcceptedDuration.from_dict(_accepted_duration)

        _transit_duration = d.pop("transit_duration", UNSET)
        transit_duration: Union[Unset, None, TaskMetadataTransitDuration]
        if _transit_duration is None:
            transit_duration = None
        elif isinstance(_transit_duration, Unset):
            transit_duration = UNSET
        else:
            transit_duration = TaskMetadataTransitDuration.from_dict(_transit_duration)

        _active_duration = d.pop("active_duration", UNSET)
        active_duration: Union[Unset, None, TaskMetadataActiveDuration]
        if _active_duration is None:
            active_duration = None
        elif isinstance(_active_duration, Unset):
            active_duration = UNSET
        else:
            active_duration = TaskMetadataActiveDuration.from_dict(_active_duration)

        _completed_duration = d.pop("completed_duration", UNSET)
        completed_duration: Union[Unset, None, TaskMetadataCompletedDuration]
        if _completed_duration is None:
            completed_duration = None
        elif isinstance(_completed_duration, Unset):
            completed_duration = UNSET
        else:
            completed_duration = TaskMetadataCompletedDuration.from_dict(_completed_duration)

        _failed_duration = d.pop("failed_duration", UNSET)
        failed_duration: Union[Unset, None, TaskMetadataFailedDuration]
        if _failed_duration is None:
            failed_duration = None
        elif isinstance(_failed_duration, Unset):
            failed_duration = UNSET
        else:
            failed_duration = TaskMetadataFailedDuration.from_dict(_failed_duration)

        _cancelled_duration = d.pop("cancelled_duration", UNSET)
        cancelled_duration: Union[Unset, None, TaskMetadataCancelledDuration]
        if _cancelled_duration is None:
            cancelled_duration = None
        elif isinstance(_cancelled_duration, Unset):
            cancelled_duration = UNSET
        else:
            cancelled_duration = TaskMetadataCancelledDuration.from_dict(_cancelled_duration)

        unassigned_distance = d.pop("unassigned_distance", UNSET)

        assigned_distance = d.pop("assigned_distance", UNSET)

        accepted_distance = d.pop("accepted_distance", UNSET)

        transit_distance = d.pop("transit_distance", UNSET)

        active_distance = d.pop("active_distance", UNSET)

        completed_distance = d.pop("completed_distance", UNSET)

        failed_distance = d.pop("failed_distance", UNSET)

        cancelled_distance = d.pop("cancelled_distance", UNSET)

        _last_unassigned_at = d.pop("last_unassigned_at", UNSET)
        last_unassigned_at: Union[Unset, None, datetime.datetime]
        if _last_unassigned_at is None:
            last_unassigned_at = None
        elif isinstance(_last_unassigned_at, Unset):
            last_unassigned_at = UNSET
        else:
            last_unassigned_at = isoparse(_last_unassigned_at)

        _last_assigned_at = d.pop("last_assigned_at", UNSET)
        last_assigned_at: Union[Unset, None, datetime.datetime]
        if _last_assigned_at is None:
            last_assigned_at = None
        elif isinstance(_last_assigned_at, Unset):
            last_assigned_at = UNSET
        else:
            last_assigned_at = isoparse(_last_assigned_at)

        _last_accepted_at = d.pop("last_accepted_at", UNSET)
        last_accepted_at: Union[Unset, None, datetime.datetime]
        if _last_accepted_at is None:
            last_accepted_at = None
        elif isinstance(_last_accepted_at, Unset):
            last_accepted_at = UNSET
        else:
            last_accepted_at = isoparse(_last_accepted_at)

        _last_transit_at = d.pop("last_transit_at", UNSET)
        last_transit_at: Union[Unset, None, datetime.datetime]
        if _last_transit_at is None:
            last_transit_at = None
        elif isinstance(_last_transit_at, Unset):
            last_transit_at = UNSET
        else:
            last_transit_at = isoparse(_last_transit_at)

        _last_active_at = d.pop("last_active_at", UNSET)
        last_active_at: Union[Unset, None, datetime.datetime]
        if _last_active_at is None:
            last_active_at = None
        elif isinstance(_last_active_at, Unset):
            last_active_at = UNSET
        else:
            last_active_at = isoparse(_last_active_at)

        _last_completed_at = d.pop("last_completed_at", UNSET)
        last_completed_at: Union[Unset, None, datetime.datetime]
        if _last_completed_at is None:
            last_completed_at = None
        elif isinstance(_last_completed_at, Unset):
            last_completed_at = UNSET
        else:
            last_completed_at = isoparse(_last_completed_at)

        _last_failed_at = d.pop("last_failed_at", UNSET)
        last_failed_at: Union[Unset, None, datetime.datetime]
        if _last_failed_at is None:
            last_failed_at = None
        elif isinstance(_last_failed_at, Unset):
            last_failed_at = UNSET
        else:
            last_failed_at = isoparse(_last_failed_at)

        _last_cancelled_at = d.pop("last_cancelled_at", UNSET)
        last_cancelled_at: Union[Unset, None, datetime.datetime]
        if _last_cancelled_at is None:
            last_cancelled_at = None
        elif isinstance(_last_cancelled_at, Unset):
            last_cancelled_at = UNSET
        else:
            last_cancelled_at = isoparse(_last_cancelled_at)

        task_metadata = cls(
            id=id,
            url=url,
            task=task,
            events_count=events_count,
            task_event_notes_count=task_event_notes_count,
            documents_count=documents_count,
            signatures_count=signatures_count,
            forms_count=forms_count,
            forms_completed_count=forms_completed_count,
            last_task_event_notes=last_task_event_notes,
            unassigned_duration=unassigned_duration,
            assigned_duration=assigned_duration,
            accepted_duration=accepted_duration,
            transit_duration=transit_duration,
            active_duration=active_duration,
            completed_duration=completed_duration,
            failed_duration=failed_duration,
            cancelled_duration=cancelled_duration,
            unassigned_distance=unassigned_distance,
            assigned_distance=assigned_distance,
            accepted_distance=accepted_distance,
            transit_distance=transit_distance,
            active_distance=active_distance,
            completed_distance=completed_distance,
            failed_distance=failed_distance,
            cancelled_distance=cancelled_distance,
            last_unassigned_at=last_unassigned_at,
            last_assigned_at=last_assigned_at,
            last_accepted_at=last_accepted_at,
            last_transit_at=last_transit_at,
            last_active_at=last_active_at,
            last_completed_at=last_completed_at,
            last_failed_at=last_failed_at,
            last_cancelled_at=last_cancelled_at,
        )

        task_metadata.additional_properties = d
        return task_metadata

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

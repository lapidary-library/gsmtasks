import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.assignee_proximity_enum import AssigneeProximityEnum
from ..models.category_enum import CategoryEnum
from ..models.task_export_address_location import TaskExportAddressLocation
from ..models.task_export_duration import TaskExportDuration
from ..models.task_export_metadata_accepted_duration import TaskExportMetadataAcceptedDuration
from ..models.task_export_metadata_active_duration import TaskExportMetadataActiveDuration
from ..models.task_export_metadata_assigned_duration import TaskExportMetadataAssignedDuration
from ..models.task_export_metadata_cancelled_duration import TaskExportMetadataCancelledDuration
from ..models.task_export_metadata_completed_duration import TaskExportMetadataCompletedDuration
from ..models.task_export_metadata_failed_duration import TaskExportMetadataFailedDuration
from ..models.task_export_metadata_transit_duration import TaskExportMetadataTransitDuration
from ..models.task_export_metadata_unassigned_duration import TaskExportMetadataUnassignedDuration
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskExport")


@attr.s(auto_attribs=True)
class TaskExport:
    """
    Attributes:
        state (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        account_name (str):
        assignee_display_name (str):
        address_location (TaskExportAddressLocation):
        created_by_display_name (str):
        metadata_events_count (int):
        metadata_documents_count (int):
        metadata_signatures_count (int):
        metadata_forms_count (int):
        metadata_forms_completed_count (int):
        metadata_unassigned_duration (TaskExportMetadataUnassignedDuration):
        metadata_assigned_duration (TaskExportMetadataAssignedDuration):
        metadata_accepted_duration (TaskExportMetadataAcceptedDuration):
        metadata_transit_duration (TaskExportMetadataTransitDuration):
        metadata_active_duration (TaskExportMetadataActiveDuration):
        metadata_completed_duration (TaskExportMetadataCompletedDuration):
        metadata_failed_duration (TaskExportMetadataFailedDuration):
        metadata_cancelled_duration (TaskExportMetadataCancelledDuration):
        metadata_unassigned_distance (int):
        metadata_assigned_distance (int):
        metadata_accepted_distance (int):
        metadata_transit_distance (int):
        metadata_active_distance (int):
        metadata_completed_distance (int):
        metadata_failed_distance (int):
        metadata_cancelled_distance (int):
        id (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        category (Union[Unset, CategoryEnum]):
        description (Union[Unset, str]):
        reference (Union[Unset, str]):
        complete_after (Union[Unset, None, datetime.datetime]):
        complete_before (Union[Unset, None, datetime.datetime]):
        scheduled_time (Union[Unset, None, datetime.datetime]):
        position (Union[Unset, None, datetime.datetime]):
        priority (Union[Unset, int]):
        duration (Union[Unset, None, TaskExportDuration]):
        is_full_load (Union[Unset, bool]):
        assignee_proximity (Union[Unset, AssigneeProximityEnum]):
        auto_assign (Union[Unset, bool]):
        issues (Union[Unset, List[str]]):
        size (Union[Unset, None, List[int]]):
        completed_at (Union[Unset, None, datetime.datetime]):
        cancelled_at (Union[Unset, None, datetime.datetime]):
        order_id (Union[Unset, str]):  Default: ''.
        order_external_id (Union[Unset, str]):  Default: ''.
        order_reference (Union[Unset, str]):  Default: ''.
        order_auto_assign (Union[Unset, str]):  Default: ''.
        order_created_by (Union[Unset, str]):  Default: ''.
        order_created_at (Union[Unset, datetime.datetime]):
        order_orderer_name (Union[Unset, str]):  Default: ''.
        order_orderer_company (Union[Unset, str]):  Default: ''.
        order_orderer_emails (Union[Unset, List[str]]):
        order_orderer_phones (Union[Unset, List[str]]):
        order_orderer_notes (Union[Unset, str]):  Default: ''.
        orderer_name (Union[Unset, str]):  Default: ''.
        contact_name (Union[Unset, str]):  Default: ''.
        contact_company (Union[Unset, str]):  Default: ''.
        contact_emails (Union[Unset, List[str]]):
        contact_phones (Union[Unset, List[str]]):
        contact_notes (Union[Unset, str]):  Default: ''.
        assignee_email (Union[Unset, str]):  Default: ''.
        assignee_phone (Union[Unset, str]):  Default: ''.
        address_raw_address (Union[Unset, str]):  Default: ''.
        address_formatted_address (Union[Unset, str]):  Default: ''.
        address_google_place_id (Union[Unset, str]):  Default: ''.
        address_point_of_interest (Union[Unset, str]):  Default: ''.
        address_street (Union[Unset, str]):  Default: ''.
        address_house_number (Union[Unset, str]):  Default: ''.
        address_apartment_number (Union[Unset, str]):  Default: ''.
        address_city (Union[Unset, str]):  Default: ''.
        address_state (Union[Unset, str]):  Default: ''.
        address_postal_code (Union[Unset, str]):  Default: ''.
        address_country (Union[Unset, str]):  Default: ''.
        address_country_code (Union[Unset, str]):  Default: ''.
        route_code (Union[Unset, str]):  Default: ''.
        route_description (Union[Unset, str]):  Default: ''.
        created_by_email (Union[Unset, str]):  Default: ''.
        created_by_phone (Union[Unset, str]):  Default: ''.
        metadata_task_event_notes_count (Union[Unset, int]):
        metadata_last_task_event_notes (Union[Unset, str]):  Default: ''.
        metadata_last_unassigned_at (Union[Unset, datetime.datetime]):
        metadata_last_assigned_at (Union[Unset, datetime.datetime]):
        metadata_last_accepted_at (Union[Unset, datetime.datetime]):
        metadata_last_transit_at (Union[Unset, datetime.datetime]):
        metadata_last_active_at (Union[Unset, datetime.datetime]):
        metadata_last_completed_at (Union[Unset, datetime.datetime]):
        metadata_last_failed_at (Union[Unset, datetime.datetime]):
        metadata_last_cancelled_at (Union[Unset, datetime.datetime]):
    """

    state: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    account_name: str
    assignee_display_name: str
    address_location: TaskExportAddressLocation
    created_by_display_name: str
    metadata_events_count: int
    metadata_documents_count: int
    metadata_signatures_count: int
    metadata_forms_count: int
    metadata_forms_completed_count: int
    metadata_unassigned_duration: TaskExportMetadataUnassignedDuration
    metadata_assigned_duration: TaskExportMetadataAssignedDuration
    metadata_accepted_duration: TaskExportMetadataAcceptedDuration
    metadata_transit_duration: TaskExportMetadataTransitDuration
    metadata_active_duration: TaskExportMetadataActiveDuration
    metadata_completed_duration: TaskExportMetadataCompletedDuration
    metadata_failed_duration: TaskExportMetadataFailedDuration
    metadata_cancelled_duration: TaskExportMetadataCancelledDuration
    metadata_unassigned_distance: int
    metadata_assigned_distance: int
    metadata_accepted_distance: int
    metadata_transit_distance: int
    metadata_active_distance: int
    metadata_completed_distance: int
    metadata_failed_distance: int
    metadata_cancelled_distance: int
    id: Union[Unset, None, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    category: Union[Unset, CategoryEnum] = UNSET
    description: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    complete_after: Union[Unset, None, datetime.datetime] = UNSET
    complete_before: Union[Unset, None, datetime.datetime] = UNSET
    scheduled_time: Union[Unset, None, datetime.datetime] = UNSET
    position: Union[Unset, None, datetime.datetime] = UNSET
    priority: Union[Unset, int] = UNSET
    duration: Union[Unset, None, TaskExportDuration] = UNSET
    is_full_load: Union[Unset, bool] = UNSET
    assignee_proximity: Union[Unset, AssigneeProximityEnum] = UNSET
    auto_assign: Union[Unset, bool] = UNSET
    issues: Union[Unset, List[str]] = UNSET
    size: Union[Unset, None, List[int]] = UNSET
    completed_at: Union[Unset, None, datetime.datetime] = UNSET
    cancelled_at: Union[Unset, None, datetime.datetime] = UNSET
    order_id: Union[Unset, str] = ""
    order_external_id: Union[Unset, str] = ""
    order_reference: Union[Unset, str] = ""
    order_auto_assign: Union[Unset, str] = ""
    order_created_by: Union[Unset, str] = ""
    order_created_at: Union[Unset, datetime.datetime] = UNSET
    order_orderer_name: Union[Unset, str] = ""
    order_orderer_company: Union[Unset, str] = ""
    order_orderer_emails: Union[Unset, List[str]] = UNSET
    order_orderer_phones: Union[Unset, List[str]] = UNSET
    order_orderer_notes: Union[Unset, str] = ""
    orderer_name: Union[Unset, str] = ""
    contact_name: Union[Unset, str] = ""
    contact_company: Union[Unset, str] = ""
    contact_emails: Union[Unset, List[str]] = UNSET
    contact_phones: Union[Unset, List[str]] = UNSET
    contact_notes: Union[Unset, str] = ""
    assignee_email: Union[Unset, str] = ""
    assignee_phone: Union[Unset, str] = ""
    address_raw_address: Union[Unset, str] = ""
    address_formatted_address: Union[Unset, str] = ""
    address_google_place_id: Union[Unset, str] = ""
    address_point_of_interest: Union[Unset, str] = ""
    address_street: Union[Unset, str] = ""
    address_house_number: Union[Unset, str] = ""
    address_apartment_number: Union[Unset, str] = ""
    address_city: Union[Unset, str] = ""
    address_state: Union[Unset, str] = ""
    address_postal_code: Union[Unset, str] = ""
    address_country: Union[Unset, str] = ""
    address_country_code: Union[Unset, str] = ""
    route_code: Union[Unset, str] = ""
    route_description: Union[Unset, str] = ""
    created_by_email: Union[Unset, str] = ""
    created_by_phone: Union[Unset, str] = ""
    metadata_task_event_notes_count: Union[Unset, int] = 0
    metadata_last_task_event_notes: Union[Unset, str] = ""
    metadata_last_unassigned_at: Union[Unset, datetime.datetime] = UNSET
    metadata_last_assigned_at: Union[Unset, datetime.datetime] = UNSET
    metadata_last_accepted_at: Union[Unset, datetime.datetime] = UNSET
    metadata_last_transit_at: Union[Unset, datetime.datetime] = UNSET
    metadata_last_active_at: Union[Unset, datetime.datetime] = UNSET
    metadata_last_completed_at: Union[Unset, datetime.datetime] = UNSET
    metadata_last_failed_at: Union[Unset, datetime.datetime] = UNSET
    metadata_last_cancelled_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        account_name = self.account_name
        assignee_display_name = self.assignee_display_name
        address_location = self.address_location.to_dict()

        created_by_display_name = self.created_by_display_name
        metadata_events_count = self.metadata_events_count
        metadata_documents_count = self.metadata_documents_count
        metadata_signatures_count = self.metadata_signatures_count
        metadata_forms_count = self.metadata_forms_count
        metadata_forms_completed_count = self.metadata_forms_completed_count
        metadata_unassigned_duration = self.metadata_unassigned_duration.to_dict()

        metadata_assigned_duration = self.metadata_assigned_duration.to_dict()

        metadata_accepted_duration = self.metadata_accepted_duration.to_dict()

        metadata_transit_duration = self.metadata_transit_duration.to_dict()

        metadata_active_duration = self.metadata_active_duration.to_dict()

        metadata_completed_duration = self.metadata_completed_duration.to_dict()

        metadata_failed_duration = self.metadata_failed_duration.to_dict()

        metadata_cancelled_duration = self.metadata_cancelled_duration.to_dict()

        metadata_unassigned_distance = self.metadata_unassigned_distance
        metadata_assigned_distance = self.metadata_assigned_distance
        metadata_accepted_distance = self.metadata_accepted_distance
        metadata_transit_distance = self.metadata_transit_distance
        metadata_active_distance = self.metadata_active_distance
        metadata_completed_distance = self.metadata_completed_distance
        metadata_failed_distance = self.metadata_failed_distance
        metadata_cancelled_distance = self.metadata_cancelled_distance
        id = self.id
        external_id = self.external_id
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

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

        position: Union[Unset, None, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.isoformat() if self.position else None

        priority = self.priority
        duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict() if self.duration else None

        is_full_load = self.is_full_load
        assignee_proximity: Union[Unset, str] = UNSET
        if not isinstance(self.assignee_proximity, Unset):
            assignee_proximity = self.assignee_proximity.value

        auto_assign = self.auto_assign
        issues: Union[Unset, List[str]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues

        size: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.size, Unset):
            if self.size is None:
                size = None
            else:
                size = self.size

        completed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat() if self.completed_at else None

        cancelled_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.cancelled_at, Unset):
            cancelled_at = self.cancelled_at.isoformat() if self.cancelled_at else None

        order_id = self.order_id
        order_external_id = self.order_external_id
        order_reference = self.order_reference
        order_auto_assign = self.order_auto_assign
        order_created_by = self.order_created_by
        order_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.order_created_at, Unset):
            order_created_at = self.order_created_at.isoformat()

        order_orderer_name = self.order_orderer_name
        order_orderer_company = self.order_orderer_company
        order_orderer_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.order_orderer_emails, Unset):
            order_orderer_emails = self.order_orderer_emails

        order_orderer_phones: Union[Unset, List[str]] = UNSET
        if not isinstance(self.order_orderer_phones, Unset):
            order_orderer_phones = self.order_orderer_phones

        order_orderer_notes = self.order_orderer_notes
        orderer_name = self.orderer_name
        contact_name = self.contact_name
        contact_company = self.contact_company
        contact_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contact_emails, Unset):
            contact_emails = self.contact_emails

        contact_phones: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contact_phones, Unset):
            contact_phones = self.contact_phones

        contact_notes = self.contact_notes
        assignee_email = self.assignee_email
        assignee_phone = self.assignee_phone
        address_raw_address = self.address_raw_address
        address_formatted_address = self.address_formatted_address
        address_google_place_id = self.address_google_place_id
        address_point_of_interest = self.address_point_of_interest
        address_street = self.address_street
        address_house_number = self.address_house_number
        address_apartment_number = self.address_apartment_number
        address_city = self.address_city
        address_state = self.address_state
        address_postal_code = self.address_postal_code
        address_country = self.address_country
        address_country_code = self.address_country_code
        route_code = self.route_code
        route_description = self.route_description
        created_by_email = self.created_by_email
        created_by_phone = self.created_by_phone
        metadata_task_event_notes_count = self.metadata_task_event_notes_count
        metadata_last_task_event_notes = self.metadata_last_task_event_notes
        metadata_last_unassigned_at: Union[Unset, str] = UNSET
        if not isinstance(self.metadata_last_unassigned_at, Unset):
            metadata_last_unassigned_at = self.metadata_last_unassigned_at.isoformat()

        metadata_last_assigned_at: Union[Unset, str] = UNSET
        if not isinstance(self.metadata_last_assigned_at, Unset):
            metadata_last_assigned_at = self.metadata_last_assigned_at.isoformat()

        metadata_last_accepted_at: Union[Unset, str] = UNSET
        if not isinstance(self.metadata_last_accepted_at, Unset):
            metadata_last_accepted_at = self.metadata_last_accepted_at.isoformat()

        metadata_last_transit_at: Union[Unset, str] = UNSET
        if not isinstance(self.metadata_last_transit_at, Unset):
            metadata_last_transit_at = self.metadata_last_transit_at.isoformat()

        metadata_last_active_at: Union[Unset, str] = UNSET
        if not isinstance(self.metadata_last_active_at, Unset):
            metadata_last_active_at = self.metadata_last_active_at.isoformat()

        metadata_last_completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.metadata_last_completed_at, Unset):
            metadata_last_completed_at = self.metadata_last_completed_at.isoformat()

        metadata_last_failed_at: Union[Unset, str] = UNSET
        if not isinstance(self.metadata_last_failed_at, Unset):
            metadata_last_failed_at = self.metadata_last_failed_at.isoformat()

        metadata_last_cancelled_at: Union[Unset, str] = UNSET
        if not isinstance(self.metadata_last_cancelled_at, Unset):
            metadata_last_cancelled_at = self.metadata_last_cancelled_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
                "account__name": account_name,
                "assignee__display_name": assignee_display_name,
                "address__location": address_location,
                "created_by__display_name": created_by_display_name,
                "metadata__events_count": metadata_events_count,
                "metadata__documents_count": metadata_documents_count,
                "metadata__signatures_count": metadata_signatures_count,
                "metadata__forms_count": metadata_forms_count,
                "metadata__forms_completed_count": metadata_forms_completed_count,
                "metadata__unassigned_duration": metadata_unassigned_duration,
                "metadata__assigned_duration": metadata_assigned_duration,
                "metadata__accepted_duration": metadata_accepted_duration,
                "metadata__transit_duration": metadata_transit_duration,
                "metadata__active_duration": metadata_active_duration,
                "metadata__completed_duration": metadata_completed_duration,
                "metadata__failed_duration": metadata_failed_duration,
                "metadata__cancelled_duration": metadata_cancelled_duration,
                "metadata__unassigned_distance": metadata_unassigned_distance,
                "metadata__assigned_distance": metadata_assigned_distance,
                "metadata__accepted_distance": metadata_accepted_distance,
                "metadata__transit_distance": metadata_transit_distance,
                "metadata__active_distance": metadata_active_distance,
                "metadata__completed_distance": metadata_completed_distance,
                "metadata__failed_distance": metadata_failed_distance,
                "metadata__cancelled_distance": metadata_cancelled_distance,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if category is not UNSET:
            field_dict["category"] = category
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
        if position is not UNSET:
            field_dict["position"] = position
        if priority is not UNSET:
            field_dict["priority"] = priority
        if duration is not UNSET:
            field_dict["duration"] = duration
        if is_full_load is not UNSET:
            field_dict["is_full_load"] = is_full_load
        if assignee_proximity is not UNSET:
            field_dict["assignee_proximity"] = assignee_proximity
        if auto_assign is not UNSET:
            field_dict["auto_assign"] = auto_assign
        if issues is not UNSET:
            field_dict["issues"] = issues
        if size is not UNSET:
            field_dict["size"] = size
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if order_id is not UNSET:
            field_dict["order__id"] = order_id
        if order_external_id is not UNSET:
            field_dict["order__external_id"] = order_external_id
        if order_reference is not UNSET:
            field_dict["order__reference"] = order_reference
        if order_auto_assign is not UNSET:
            field_dict["order__auto_assign"] = order_auto_assign
        if order_created_by is not UNSET:
            field_dict["order__created_by"] = order_created_by
        if order_created_at is not UNSET:
            field_dict["order__created_at"] = order_created_at
        if order_orderer_name is not UNSET:
            field_dict["order__orderer__name"] = order_orderer_name
        if order_orderer_company is not UNSET:
            field_dict["order__orderer__company"] = order_orderer_company
        if order_orderer_emails is not UNSET:
            field_dict["order__orderer__emails"] = order_orderer_emails
        if order_orderer_phones is not UNSET:
            field_dict["order__orderer__phones"] = order_orderer_phones
        if order_orderer_notes is not UNSET:
            field_dict["order__orderer__notes"] = order_orderer_notes
        if orderer_name is not UNSET:
            field_dict["orderer__name"] = orderer_name
        if contact_name is not UNSET:
            field_dict["contact__name"] = contact_name
        if contact_company is not UNSET:
            field_dict["contact__company"] = contact_company
        if contact_emails is not UNSET:
            field_dict["contact__emails"] = contact_emails
        if contact_phones is not UNSET:
            field_dict["contact__phones"] = contact_phones
        if contact_notes is not UNSET:
            field_dict["contact__notes"] = contact_notes
        if assignee_email is not UNSET:
            field_dict["assignee__email"] = assignee_email
        if assignee_phone is not UNSET:
            field_dict["assignee__phone"] = assignee_phone
        if address_raw_address is not UNSET:
            field_dict["address__raw_address"] = address_raw_address
        if address_formatted_address is not UNSET:
            field_dict["address__formatted_address"] = address_formatted_address
        if address_google_place_id is not UNSET:
            field_dict["address__google_place_id"] = address_google_place_id
        if address_point_of_interest is not UNSET:
            field_dict["address__point_of_interest"] = address_point_of_interest
        if address_street is not UNSET:
            field_dict["address__street"] = address_street
        if address_house_number is not UNSET:
            field_dict["address__house_number"] = address_house_number
        if address_apartment_number is not UNSET:
            field_dict["address__apartment_number"] = address_apartment_number
        if address_city is not UNSET:
            field_dict["address__city"] = address_city
        if address_state is not UNSET:
            field_dict["address__state"] = address_state
        if address_postal_code is not UNSET:
            field_dict["address__postal_code"] = address_postal_code
        if address_country is not UNSET:
            field_dict["address__country"] = address_country
        if address_country_code is not UNSET:
            field_dict["address__country_code"] = address_country_code
        if route_code is not UNSET:
            field_dict["route__code"] = route_code
        if route_description is not UNSET:
            field_dict["route__description"] = route_description
        if created_by_email is not UNSET:
            field_dict["created_by__email"] = created_by_email
        if created_by_phone is not UNSET:
            field_dict["created_by__phone"] = created_by_phone
        if metadata_task_event_notes_count is not UNSET:
            field_dict["metadata__task_event_notes_count"] = metadata_task_event_notes_count
        if metadata_last_task_event_notes is not UNSET:
            field_dict["metadata__last_task_event_notes"] = metadata_last_task_event_notes
        if metadata_last_unassigned_at is not UNSET:
            field_dict["metadata__last_unassigned_at"] = metadata_last_unassigned_at
        if metadata_last_assigned_at is not UNSET:
            field_dict["metadata__last_assigned_at"] = metadata_last_assigned_at
        if metadata_last_accepted_at is not UNSET:
            field_dict["metadata__last_accepted_at"] = metadata_last_accepted_at
        if metadata_last_transit_at is not UNSET:
            field_dict["metadata__last_transit_at"] = metadata_last_transit_at
        if metadata_last_active_at is not UNSET:
            field_dict["metadata__last_active_at"] = metadata_last_active_at
        if metadata_last_completed_at is not UNSET:
            field_dict["metadata__last_completed_at"] = metadata_last_completed_at
        if metadata_last_failed_at is not UNSET:
            field_dict["metadata__last_failed_at"] = metadata_last_failed_at
        if metadata_last_cancelled_at is not UNSET:
            field_dict["metadata__last_cancelled_at"] = metadata_last_cancelled_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = d.pop("state")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        account_name = d.pop("account__name")

        assignee_display_name = d.pop("assignee__display_name")

        address_location = TaskExportAddressLocation.from_dict(d.pop("address__location"))

        created_by_display_name = d.pop("created_by__display_name")

        metadata_events_count = d.pop("metadata__events_count")

        metadata_documents_count = d.pop("metadata__documents_count")

        metadata_signatures_count = d.pop("metadata__signatures_count")

        metadata_forms_count = d.pop("metadata__forms_count")

        metadata_forms_completed_count = d.pop("metadata__forms_completed_count")

        metadata_unassigned_duration = TaskExportMetadataUnassignedDuration.from_dict(
            d.pop("metadata__unassigned_duration")
        )

        metadata_assigned_duration = TaskExportMetadataAssignedDuration.from_dict(d.pop("metadata__assigned_duration"))

        metadata_accepted_duration = TaskExportMetadataAcceptedDuration.from_dict(d.pop("metadata__accepted_duration"))

        metadata_transit_duration = TaskExportMetadataTransitDuration.from_dict(d.pop("metadata__transit_duration"))

        metadata_active_duration = TaskExportMetadataActiveDuration.from_dict(d.pop("metadata__active_duration"))

        metadata_completed_duration = TaskExportMetadataCompletedDuration.from_dict(
            d.pop("metadata__completed_duration")
        )

        metadata_failed_duration = TaskExportMetadataFailedDuration.from_dict(d.pop("metadata__failed_duration"))

        metadata_cancelled_duration = TaskExportMetadataCancelledDuration.from_dict(
            d.pop("metadata__cancelled_duration")
        )

        metadata_unassigned_distance = d.pop("metadata__unassigned_distance")

        metadata_assigned_distance = d.pop("metadata__assigned_distance")

        metadata_accepted_distance = d.pop("metadata__accepted_distance")

        metadata_transit_distance = d.pop("metadata__transit_distance")

        metadata_active_distance = d.pop("metadata__active_distance")

        metadata_completed_distance = d.pop("metadata__completed_distance")

        metadata_failed_distance = d.pop("metadata__failed_distance")

        metadata_cancelled_distance = d.pop("metadata__cancelled_distance")

        id = d.pop("id", UNSET)

        external_id = d.pop("external_id", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, CategoryEnum]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CategoryEnum(_category)

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
        duration: Union[Unset, None, TaskExportDuration]
        if _duration is None:
            duration = None
        elif isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = TaskExportDuration.from_dict(_duration)

        is_full_load = d.pop("is_full_load", UNSET)

        _assignee_proximity = d.pop("assignee_proximity", UNSET)
        assignee_proximity: Union[Unset, AssigneeProximityEnum]
        if isinstance(_assignee_proximity, Unset):
            assignee_proximity = UNSET
        else:
            assignee_proximity = AssigneeProximityEnum(_assignee_proximity)

        auto_assign = d.pop("auto_assign", UNSET)

        issues = cast(List[str], d.pop("issues", UNSET))

        size = cast(List[int], d.pop("size", UNSET))

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, None, datetime.datetime]
        if _completed_at is None:
            completed_at = None
        elif isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _cancelled_at = d.pop("cancelled_at", UNSET)
        cancelled_at: Union[Unset, None, datetime.datetime]
        if _cancelled_at is None:
            cancelled_at = None
        elif isinstance(_cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = isoparse(_cancelled_at)

        order_id = d.pop("order__id", UNSET)

        order_external_id = d.pop("order__external_id", UNSET)

        order_reference = d.pop("order__reference", UNSET)

        order_auto_assign = d.pop("order__auto_assign", UNSET)

        order_created_by = d.pop("order__created_by", UNSET)

        _order_created_at = d.pop("order__created_at", UNSET)
        order_created_at: Union[Unset, datetime.datetime]
        if isinstance(_order_created_at, Unset):
            order_created_at = UNSET
        else:
            order_created_at = isoparse(_order_created_at)

        order_orderer_name = d.pop("order__orderer__name", UNSET)

        order_orderer_company = d.pop("order__orderer__company", UNSET)

        order_orderer_emails = cast(List[str], d.pop("order__orderer__emails", UNSET))

        order_orderer_phones = cast(List[str], d.pop("order__orderer__phones", UNSET))

        order_orderer_notes = d.pop("order__orderer__notes", UNSET)

        orderer_name = d.pop("orderer__name", UNSET)

        contact_name = d.pop("contact__name", UNSET)

        contact_company = d.pop("contact__company", UNSET)

        contact_emails = cast(List[str], d.pop("contact__emails", UNSET))

        contact_phones = cast(List[str], d.pop("contact__phones", UNSET))

        contact_notes = d.pop("contact__notes", UNSET)

        assignee_email = d.pop("assignee__email", UNSET)

        assignee_phone = d.pop("assignee__phone", UNSET)

        address_raw_address = d.pop("address__raw_address", UNSET)

        address_formatted_address = d.pop("address__formatted_address", UNSET)

        address_google_place_id = d.pop("address__google_place_id", UNSET)

        address_point_of_interest = d.pop("address__point_of_interest", UNSET)

        address_street = d.pop("address__street", UNSET)

        address_house_number = d.pop("address__house_number", UNSET)

        address_apartment_number = d.pop("address__apartment_number", UNSET)

        address_city = d.pop("address__city", UNSET)

        address_state = d.pop("address__state", UNSET)

        address_postal_code = d.pop("address__postal_code", UNSET)

        address_country = d.pop("address__country", UNSET)

        address_country_code = d.pop("address__country_code", UNSET)

        route_code = d.pop("route__code", UNSET)

        route_description = d.pop("route__description", UNSET)

        created_by_email = d.pop("created_by__email", UNSET)

        created_by_phone = d.pop("created_by__phone", UNSET)

        metadata_task_event_notes_count = d.pop("metadata__task_event_notes_count", UNSET)

        metadata_last_task_event_notes = d.pop("metadata__last_task_event_notes", UNSET)

        _metadata_last_unassigned_at = d.pop("metadata__last_unassigned_at", UNSET)
        metadata_last_unassigned_at: Union[Unset, datetime.datetime]
        if isinstance(_metadata_last_unassigned_at, Unset):
            metadata_last_unassigned_at = UNSET
        else:
            metadata_last_unassigned_at = isoparse(_metadata_last_unassigned_at)

        _metadata_last_assigned_at = d.pop("metadata__last_assigned_at", UNSET)
        metadata_last_assigned_at: Union[Unset, datetime.datetime]
        if isinstance(_metadata_last_assigned_at, Unset):
            metadata_last_assigned_at = UNSET
        else:
            metadata_last_assigned_at = isoparse(_metadata_last_assigned_at)

        _metadata_last_accepted_at = d.pop("metadata__last_accepted_at", UNSET)
        metadata_last_accepted_at: Union[Unset, datetime.datetime]
        if isinstance(_metadata_last_accepted_at, Unset):
            metadata_last_accepted_at = UNSET
        else:
            metadata_last_accepted_at = isoparse(_metadata_last_accepted_at)

        _metadata_last_transit_at = d.pop("metadata__last_transit_at", UNSET)
        metadata_last_transit_at: Union[Unset, datetime.datetime]
        if isinstance(_metadata_last_transit_at, Unset):
            metadata_last_transit_at = UNSET
        else:
            metadata_last_transit_at = isoparse(_metadata_last_transit_at)

        _metadata_last_active_at = d.pop("metadata__last_active_at", UNSET)
        metadata_last_active_at: Union[Unset, datetime.datetime]
        if isinstance(_metadata_last_active_at, Unset):
            metadata_last_active_at = UNSET
        else:
            metadata_last_active_at = isoparse(_metadata_last_active_at)

        _metadata_last_completed_at = d.pop("metadata__last_completed_at", UNSET)
        metadata_last_completed_at: Union[Unset, datetime.datetime]
        if isinstance(_metadata_last_completed_at, Unset):
            metadata_last_completed_at = UNSET
        else:
            metadata_last_completed_at = isoparse(_metadata_last_completed_at)

        _metadata_last_failed_at = d.pop("metadata__last_failed_at", UNSET)
        metadata_last_failed_at: Union[Unset, datetime.datetime]
        if isinstance(_metadata_last_failed_at, Unset):
            metadata_last_failed_at = UNSET
        else:
            metadata_last_failed_at = isoparse(_metadata_last_failed_at)

        _metadata_last_cancelled_at = d.pop("metadata__last_cancelled_at", UNSET)
        metadata_last_cancelled_at: Union[Unset, datetime.datetime]
        if isinstance(_metadata_last_cancelled_at, Unset):
            metadata_last_cancelled_at = UNSET
        else:
            metadata_last_cancelled_at = isoparse(_metadata_last_cancelled_at)

        task_export = cls(
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            account_name=account_name,
            assignee_display_name=assignee_display_name,
            address_location=address_location,
            created_by_display_name=created_by_display_name,
            metadata_events_count=metadata_events_count,
            metadata_documents_count=metadata_documents_count,
            metadata_signatures_count=metadata_signatures_count,
            metadata_forms_count=metadata_forms_count,
            metadata_forms_completed_count=metadata_forms_completed_count,
            metadata_unassigned_duration=metadata_unassigned_duration,
            metadata_assigned_duration=metadata_assigned_duration,
            metadata_accepted_duration=metadata_accepted_duration,
            metadata_transit_duration=metadata_transit_duration,
            metadata_active_duration=metadata_active_duration,
            metadata_completed_duration=metadata_completed_duration,
            metadata_failed_duration=metadata_failed_duration,
            metadata_cancelled_duration=metadata_cancelled_duration,
            metadata_unassigned_distance=metadata_unassigned_distance,
            metadata_assigned_distance=metadata_assigned_distance,
            metadata_accepted_distance=metadata_accepted_distance,
            metadata_transit_distance=metadata_transit_distance,
            metadata_active_distance=metadata_active_distance,
            metadata_completed_distance=metadata_completed_distance,
            metadata_failed_distance=metadata_failed_distance,
            metadata_cancelled_distance=metadata_cancelled_distance,
            id=id,
            external_id=external_id,
            category=category,
            description=description,
            reference=reference,
            complete_after=complete_after,
            complete_before=complete_before,
            scheduled_time=scheduled_time,
            position=position,
            priority=priority,
            duration=duration,
            is_full_load=is_full_load,
            assignee_proximity=assignee_proximity,
            auto_assign=auto_assign,
            issues=issues,
            size=size,
            completed_at=completed_at,
            cancelled_at=cancelled_at,
            order_id=order_id,
            order_external_id=order_external_id,
            order_reference=order_reference,
            order_auto_assign=order_auto_assign,
            order_created_by=order_created_by,
            order_created_at=order_created_at,
            order_orderer_name=order_orderer_name,
            order_orderer_company=order_orderer_company,
            order_orderer_emails=order_orderer_emails,
            order_orderer_phones=order_orderer_phones,
            order_orderer_notes=order_orderer_notes,
            orderer_name=orderer_name,
            contact_name=contact_name,
            contact_company=contact_company,
            contact_emails=contact_emails,
            contact_phones=contact_phones,
            contact_notes=contact_notes,
            assignee_email=assignee_email,
            assignee_phone=assignee_phone,
            address_raw_address=address_raw_address,
            address_formatted_address=address_formatted_address,
            address_google_place_id=address_google_place_id,
            address_point_of_interest=address_point_of_interest,
            address_street=address_street,
            address_house_number=address_house_number,
            address_apartment_number=address_apartment_number,
            address_city=address_city,
            address_state=address_state,
            address_postal_code=address_postal_code,
            address_country=address_country,
            address_country_code=address_country_code,
            route_code=route_code,
            route_description=route_description,
            created_by_email=created_by_email,
            created_by_phone=created_by_phone,
            metadata_task_event_notes_count=metadata_task_event_notes_count,
            metadata_last_task_event_notes=metadata_last_task_event_notes,
            metadata_last_unassigned_at=metadata_last_unassigned_at,
            metadata_last_assigned_at=metadata_last_assigned_at,
            metadata_last_accepted_at=metadata_last_accepted_at,
            metadata_last_transit_at=metadata_last_transit_at,
            metadata_last_active_at=metadata_last_active_at,
            metadata_last_completed_at=metadata_last_completed_at,
            metadata_last_failed_at=metadata_last_failed_at,
            metadata_last_cancelled_at=metadata_last_cancelled_at,
        )

        task_export.additional_properties = d
        return task_export

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

from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.task_export import TaskExport
from ...models.task_exports_list_assignee_proximity import TaskExportsListAssigneeProximity
from ...models.task_exports_list_category import TaskExportsListCategory
from ...models.task_exports_list_format import TaskExportsListFormat
from ...models.task_exports_list_state import TaskExportsListState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    address_apartment_number: Union[Unset, None, str] = UNSET,
    address_apartment_number_icontains: Union[Unset, None, str] = UNSET,
    address_apartment_number_in: Union[Unset, None, str] = UNSET,
    address_apartment_number_iregex: Union[Unset, None, str] = UNSET,
    address_apartment_number_istartswith: Union[Unset, None, str] = UNSET,
    address_apartment_number_search: Union[Unset, None, str] = UNSET,
    address_city: Union[Unset, None, str] = UNSET,
    address_city_icontains: Union[Unset, None, str] = UNSET,
    address_city_in: Union[Unset, None, str] = UNSET,
    address_city_iregex: Union[Unset, None, str] = UNSET,
    address_city_istartswith: Union[Unset, None, str] = UNSET,
    address_city_search: Union[Unset, None, str] = UNSET,
    address_country: Union[Unset, None, str] = UNSET,
    address_country_icontains: Union[Unset, None, str] = UNSET,
    address_country_in: Union[Unset, None, str] = UNSET,
    address_country_iregex: Union[Unset, None, str] = UNSET,
    address_country_istartswith: Union[Unset, None, str] = UNSET,
    address_country_search: Union[Unset, None, str] = UNSET,
    address_country_code: Union[Unset, None, str] = UNSET,
    address_country_code_icontains: Union[Unset, None, str] = UNSET,
    address_country_code_in: Union[Unset, None, str] = UNSET,
    address_country_code_iregex: Union[Unset, None, str] = UNSET,
    address_country_code_istartswith: Union[Unset, None, str] = UNSET,
    address_country_code_search: Union[Unset, None, str] = UNSET,
    address_formatted_address: Union[Unset, None, str] = UNSET,
    address_formatted_address_icontains: Union[Unset, None, str] = UNSET,
    address_formatted_address_in: Union[Unset, None, str] = UNSET,
    address_formatted_address_iregex: Union[Unset, None, str] = UNSET,
    address_formatted_address_istartswith: Union[Unset, None, str] = UNSET,
    address_formatted_address_search: Union[Unset, None, str] = UNSET,
    address_google_place_id: Union[Unset, None, str] = UNSET,
    address_google_place_id_icontains: Union[Unset, None, str] = UNSET,
    address_google_place_id_in: Union[Unset, None, str] = UNSET,
    address_google_place_id_iregex: Union[Unset, None, str] = UNSET,
    address_google_place_id_istartswith: Union[Unset, None, str] = UNSET,
    address_google_place_id_search: Union[Unset, None, str] = UNSET,
    address_house_number: Union[Unset, None, str] = UNSET,
    address_house_number_icontains: Union[Unset, None, str] = UNSET,
    address_house_number_in: Union[Unset, None, str] = UNSET,
    address_house_number_iregex: Union[Unset, None, str] = UNSET,
    address_house_number_istartswith: Union[Unset, None, str] = UNSET,
    address_house_number_search: Union[Unset, None, str] = UNSET,
    address_point_of_interest: Union[Unset, None, str] = UNSET,
    address_point_of_interest_icontains: Union[Unset, None, str] = UNSET,
    address_point_of_interest_in: Union[Unset, None, str] = UNSET,
    address_point_of_interest_iregex: Union[Unset, None, str] = UNSET,
    address_point_of_interest_istartswith: Union[Unset, None, str] = UNSET,
    address_point_of_interest_search: Union[Unset, None, str] = UNSET,
    address_postal_code: Union[Unset, None, str] = UNSET,
    address_postal_code_icontains: Union[Unset, None, str] = UNSET,
    address_postal_code_in: Union[Unset, None, str] = UNSET,
    address_postal_code_iregex: Union[Unset, None, str] = UNSET,
    address_postal_code_istartswith: Union[Unset, None, str] = UNSET,
    address_postal_code_search: Union[Unset, None, str] = UNSET,
    address_raw_address: Union[Unset, None, str] = UNSET,
    address_raw_address_icontains: Union[Unset, None, str] = UNSET,
    address_raw_address_in: Union[Unset, None, str] = UNSET,
    address_raw_address_iregex: Union[Unset, None, str] = UNSET,
    address_raw_address_istartswith: Union[Unset, None, str] = UNSET,
    address_raw_address_search: Union[Unset, None, str] = UNSET,
    address_state: Union[Unset, None, str] = UNSET,
    address_state_icontains: Union[Unset, None, str] = UNSET,
    address_state_in: Union[Unset, None, str] = UNSET,
    address_state_iregex: Union[Unset, None, str] = UNSET,
    address_state_istartswith: Union[Unset, None, str] = UNSET,
    address_state_search: Union[Unset, None, str] = UNSET,
    address_street: Union[Unset, None, str] = UNSET,
    address_street_icontains: Union[Unset, None, str] = UNSET,
    address_street_in: Union[Unset, None, str] = UNSET,
    address_street_iregex: Union[Unset, None, str] = UNSET,
    address_street_istartswith: Union[Unset, None, str] = UNSET,
    address_street_search: Union[Unset, None, str] = UNSET,
    address_id: Union[Unset, None, str] = UNSET,
    address_id_in: Union[Unset, None, str] = UNSET,
    address_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_email: Union[Unset, None, str] = UNSET,
    assignee_email_icontains: Union[Unset, None, str] = UNSET,
    assignee_email_iregex: Union[Unset, None, str] = UNSET,
    assignee_email_isnull: Union[Unset, None, str] = UNSET,
    assignee_email_istartswith: Union[Unset, None, str] = UNSET,
    assignee_email_search: Union[Unset, None, str] = UNSET,
    assignee_first_name: Union[Unset, None, str] = UNSET,
    assignee_first_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_first_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_first_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_first_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_first_name_search: Union[Unset, None, str] = UNSET,
    assignee_last_name: Union[Unset, None, str] = UNSET,
    assignee_last_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_last_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_last_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_last_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_last_name_search: Union[Unset, None, str] = UNSET,
    assignee_phone: Union[Unset, None, str] = UNSET,
    assignee_phone_icontains: Union[Unset, None, str] = UNSET,
    assignee_phone_iregex: Union[Unset, None, str] = UNSET,
    assignee_phone_isnull: Union[Unset, None, str] = UNSET,
    assignee_phone_istartswith: Union[Unset, None, str] = UNSET,
    assignee_phone_search: Union[Unset, None, str] = UNSET,
    assignee_id: Union[Unset, None, str] = UNSET,
    assignee_id_in: Union[Unset, None, str] = UNSET,
    assignee_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_proximity: Union[Unset, None, TaskExportsListAssigneeProximity] = UNSET,
    assignee_proximity_in: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskExportsListCategory] = UNSET,
    category_in: Union[Unset, None, str] = UNSET,
    contact_company_icontains: Union[Unset, None, str] = UNSET,
    contact_company_in: Union[Unset, None, str] = UNSET,
    contact_company_iregex: Union[Unset, None, str] = UNSET,
    contact_company_istartswith: Union[Unset, None, str] = UNSET,
    contact_company_search: Union[Unset, None, str] = UNSET,
    contact_email: Union[Unset, None, str] = UNSET,
    contact_email_icontains: Union[Unset, None, str] = UNSET,
    contact_email_in: Union[Unset, None, str] = UNSET,
    contact_email_iregex: Union[Unset, None, str] = UNSET,
    contact_email_istartswith: Union[Unset, None, str] = UNSET,
    contact_email_search: Union[Unset, None, str] = UNSET,
    contact_name: Union[Unset, None, str] = UNSET,
    contact_name_icontains: Union[Unset, None, str] = UNSET,
    contact_name_in: Union[Unset, None, str] = UNSET,
    contact_name_iregex: Union[Unset, None, str] = UNSET,
    contact_name_istartswith: Union[Unset, None, str] = UNSET,
    contact_name_search: Union[Unset, None, str] = UNSET,
    contact_notes: Union[Unset, None, str] = UNSET,
    contact_notes_icontains: Union[Unset, None, str] = UNSET,
    contact_notes_in: Union[Unset, None, str] = UNSET,
    contact_notes_iregex: Union[Unset, None, str] = UNSET,
    contact_notes_istartswith: Union[Unset, None, str] = UNSET,
    contact_notes_search: Union[Unset, None, str] = UNSET,
    contact_phone: Union[Unset, None, str] = UNSET,
    contact_phone_icontains: Union[Unset, None, str] = UNSET,
    contact_phone_in: Union[Unset, None, str] = UNSET,
    contact_phone_iregex: Union[Unset, None, str] = UNSET,
    contact_phone_istartswith: Union[Unset, None, str] = UNSET,
    contact_phone_search: Union[Unset, None, str] = UNSET,
    contact_id: Union[Unset, None, str] = UNSET,
    contact_id_in: Union[Unset, None, str] = UNSET,
    contact_id_isnull: Union[Unset, None, str] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    created_by_in: Union[Unset, None, str] = UNSET,
    created_by_isnull: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    description_icontains: Union[Unset, None, str] = UNSET,
    description_iregex: Union[Unset, None, str] = UNSET,
    description_istartswith: Union[Unset, None, str] = UNSET,
    description_search: Union[Unset, None, str] = UNSET,
    duration: Union[Unset, None, str] = UNSET,
    duration_gt: Union[Unset, None, str] = UNSET,
    duration_gte: Union[Unset, None, str] = UNSET,
    duration_lt: Union[Unset, None, str] = UNSET,
    duration_lte: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    external_id_in: Union[Unset, None, str] = UNSET,
    external_id_iregex: Union[Unset, None, str] = UNSET,
    external_id_isnull: Union[Unset, None, str] = UNSET,
    external_id_istartswith: Union[Unset, None, str] = UNSET,
    external_id_search: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, TaskExportsListFormat] = TaskExportsListFormat.JSON,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    is_optimal: Union[Unset, None, str] = UNSET,
    is_optimal_isnull: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_active_distance: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_active_duration: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_documents_count: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gte: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lte: Union[Unset, None, str] = UNSET,
    metadata_events_count: Union[Unset, None, str] = UNSET,
    metadata_events_count_gt: Union[Unset, None, str] = UNSET,
    metadata_events_count_gte: Union[Unset, None, str] = UNSET,
    metadata_events_count_lt: Union[Unset, None, str] = UNSET,
    metadata_events_count_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_count: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lte: Union[Unset, None, str] = UNSET,
    order_auto_assign: Union[Unset, None, str] = UNSET,
    order_created_by: Union[Unset, None, str] = UNSET,
    order_created_by_in: Union[Unset, None, str] = UNSET,
    order_created_by_isnull: Union[Unset, None, str] = UNSET,
    order_external_id: Union[Unset, None, str] = UNSET,
    order_external_id_icontains: Union[Unset, None, str] = UNSET,
    order_external_id_in: Union[Unset, None, str] = UNSET,
    order_external_id_iregex: Union[Unset, None, str] = UNSET,
    order_external_id_isnull: Union[Unset, None, str] = UNSET,
    order_external_id_istartswith: Union[Unset, None, str] = UNSET,
    order_external_id_search: Union[Unset, None, str] = UNSET,
    order_reference: Union[Unset, None, str] = UNSET,
    order_reference_icontains: Union[Unset, None, str] = UNSET,
    order_reference_in: Union[Unset, None, str] = UNSET,
    order_reference_iregex: Union[Unset, None, str] = UNSET,
    order_reference_istartswith: Union[Unset, None, str] = UNSET,
    order_reference_search: Union[Unset, None, str] = UNSET,
    order_id: Union[Unset, None, str] = UNSET,
    order_id_in: Union[Unset, None, str] = UNSET,
    order_id_isnull: Union[Unset, None, str] = UNSET,
    orderer_id: Union[Unset, None, str] = UNSET,
    orderer_id_in: Union[Unset, None, str] = UNSET,
    orderer_id_isnull: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    owner_id: Union[Unset, None, str] = UNSET,
    owner_id_in: Union[Unset, None, str] = UNSET,
    owner_id_isnull: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    priority_gt: Union[Unset, None, str] = UNSET,
    priority_gte: Union[Unset, None, str] = UNSET,
    priority_in: Union[Unset, None, str] = UNSET,
    priority_lt: Union[Unset, None, str] = UNSET,
    priority_lte: Union[Unset, None, str] = UNSET,
    receiver_id: Union[Unset, None, str] = UNSET,
    receiver_id_in: Union[Unset, None, str] = UNSET,
    receiver_id_isnull: Union[Unset, None, str] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    reference_icontains: Union[Unset, None, str] = UNSET,
    reference_in: Union[Unset, None, str] = UNSET,
    reference_iregex: Union[Unset, None, str] = UNSET,
    reference_istartswith: Union[Unset, None, str] = UNSET,
    reference_search: Union[Unset, None, str] = UNSET,
    route_id: Union[Unset, None, str] = UNSET,
    route_id_in: Union[Unset, None, str] = UNSET,
    route_id_isnull: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, TaskExportsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    unassignee_id: Union[Unset, None, str] = UNSET,
    unassignee_id_in: Union[Unset, None, str] = UNSET,
    unassignee_id_isnull: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/task_exports/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["address__apartment_number"] = address_apartment_number

    params["address__apartment_number__icontains"] = address_apartment_number_icontains

    params["address__apartment_number__in"] = address_apartment_number_in

    params["address__apartment_number__iregex"] = address_apartment_number_iregex

    params["address__apartment_number__istartswith"] = address_apartment_number_istartswith

    params["address__apartment_number__search"] = address_apartment_number_search

    params["address__city"] = address_city

    params["address__city__icontains"] = address_city_icontains

    params["address__city__in"] = address_city_in

    params["address__city__iregex"] = address_city_iregex

    params["address__city__istartswith"] = address_city_istartswith

    params["address__city__search"] = address_city_search

    params["address__country"] = address_country

    params["address__country__icontains"] = address_country_icontains

    params["address__country__in"] = address_country_in

    params["address__country__iregex"] = address_country_iregex

    params["address__country__istartswith"] = address_country_istartswith

    params["address__country__search"] = address_country_search

    params["address__country_code"] = address_country_code

    params["address__country_code__icontains"] = address_country_code_icontains

    params["address__country_code__in"] = address_country_code_in

    params["address__country_code__iregex"] = address_country_code_iregex

    params["address__country_code__istartswith"] = address_country_code_istartswith

    params["address__country_code__search"] = address_country_code_search

    params["address__formatted_address"] = address_formatted_address

    params["address__formatted_address__icontains"] = address_formatted_address_icontains

    params["address__formatted_address__in"] = address_formatted_address_in

    params["address__formatted_address__iregex"] = address_formatted_address_iregex

    params["address__formatted_address__istartswith"] = address_formatted_address_istartswith

    params["address__formatted_address__search"] = address_formatted_address_search

    params["address__google_place_id"] = address_google_place_id

    params["address__google_place_id__icontains"] = address_google_place_id_icontains

    params["address__google_place_id__in"] = address_google_place_id_in

    params["address__google_place_id__iregex"] = address_google_place_id_iregex

    params["address__google_place_id__istartswith"] = address_google_place_id_istartswith

    params["address__google_place_id__search"] = address_google_place_id_search

    params["address__house_number"] = address_house_number

    params["address__house_number__icontains"] = address_house_number_icontains

    params["address__house_number__in"] = address_house_number_in

    params["address__house_number__iregex"] = address_house_number_iregex

    params["address__house_number__istartswith"] = address_house_number_istartswith

    params["address__house_number__search"] = address_house_number_search

    params["address__point_of_interest"] = address_point_of_interest

    params["address__point_of_interest__icontains"] = address_point_of_interest_icontains

    params["address__point_of_interest__in"] = address_point_of_interest_in

    params["address__point_of_interest__iregex"] = address_point_of_interest_iregex

    params["address__point_of_interest__istartswith"] = address_point_of_interest_istartswith

    params["address__point_of_interest__search"] = address_point_of_interest_search

    params["address__postal_code"] = address_postal_code

    params["address__postal_code__icontains"] = address_postal_code_icontains

    params["address__postal_code__in"] = address_postal_code_in

    params["address__postal_code__iregex"] = address_postal_code_iregex

    params["address__postal_code__istartswith"] = address_postal_code_istartswith

    params["address__postal_code__search"] = address_postal_code_search

    params["address__raw_address"] = address_raw_address

    params["address__raw_address__icontains"] = address_raw_address_icontains

    params["address__raw_address__in"] = address_raw_address_in

    params["address__raw_address__iregex"] = address_raw_address_iregex

    params["address__raw_address__istartswith"] = address_raw_address_istartswith

    params["address__raw_address__search"] = address_raw_address_search

    params["address__state"] = address_state

    params["address__state__icontains"] = address_state_icontains

    params["address__state__in"] = address_state_in

    params["address__state__iregex"] = address_state_iregex

    params["address__state__istartswith"] = address_state_istartswith

    params["address__state__search"] = address_state_search

    params["address__street"] = address_street

    params["address__street__icontains"] = address_street_icontains

    params["address__street__in"] = address_street_in

    params["address__street__iregex"] = address_street_iregex

    params["address__street__istartswith"] = address_street_istartswith

    params["address__street__search"] = address_street_search

    params["address_id"] = address_id

    params["address_id__in"] = address_id_in

    params["address_id__isnull"] = address_id_isnull

    params["assignee__email"] = assignee_email

    params["assignee__email__icontains"] = assignee_email_icontains

    params["assignee__email__iregex"] = assignee_email_iregex

    params["assignee__email__isnull"] = assignee_email_isnull

    params["assignee__email__istartswith"] = assignee_email_istartswith

    params["assignee__email__search"] = assignee_email_search

    params["assignee__first_name"] = assignee_first_name

    params["assignee__first_name__icontains"] = assignee_first_name_icontains

    params["assignee__first_name__iregex"] = assignee_first_name_iregex

    params["assignee__first_name__isnull"] = assignee_first_name_isnull

    params["assignee__first_name__istartswith"] = assignee_first_name_istartswith

    params["assignee__first_name__search"] = assignee_first_name_search

    params["assignee__last_name"] = assignee_last_name

    params["assignee__last_name__icontains"] = assignee_last_name_icontains

    params["assignee__last_name__iregex"] = assignee_last_name_iregex

    params["assignee__last_name__isnull"] = assignee_last_name_isnull

    params["assignee__last_name__istartswith"] = assignee_last_name_istartswith

    params["assignee__last_name__search"] = assignee_last_name_search

    params["assignee__phone"] = assignee_phone

    params["assignee__phone__icontains"] = assignee_phone_icontains

    params["assignee__phone__iregex"] = assignee_phone_iregex

    params["assignee__phone__isnull"] = assignee_phone_isnull

    params["assignee__phone__istartswith"] = assignee_phone_istartswith

    params["assignee__phone__search"] = assignee_phone_search

    params["assignee_id"] = assignee_id

    params["assignee_id__in"] = assignee_id_in

    params["assignee_id__isnull"] = assignee_id_isnull

    json_assignee_proximity: Union[Unset, None, str] = UNSET
    if not isinstance(assignee_proximity, Unset):
        json_assignee_proximity = assignee_proximity.value if assignee_proximity else None

    params["assignee_proximity"] = json_assignee_proximity

    params["assignee_proximity__in"] = assignee_proximity_in

    json_category: Union[Unset, None, str] = UNSET
    if not isinstance(category, Unset):
        json_category = category.value if category else None

    params["category"] = json_category

    params["category__in"] = category_in

    params["contact__company__icontains"] = contact_company_icontains

    params["contact__company__in"] = contact_company_in

    params["contact__company__iregex"] = contact_company_iregex

    params["contact__company__istartswith"] = contact_company_istartswith

    params["contact__company__search"] = contact_company_search

    params["contact__email"] = contact_email

    params["contact__email__icontains"] = contact_email_icontains

    params["contact__email__in"] = contact_email_in

    params["contact__email__iregex"] = contact_email_iregex

    params["contact__email__istartswith"] = contact_email_istartswith

    params["contact__email__search"] = contact_email_search

    params["contact__name"] = contact_name

    params["contact__name__icontains"] = contact_name_icontains

    params["contact__name__in"] = contact_name_in

    params["contact__name__iregex"] = contact_name_iregex

    params["contact__name__istartswith"] = contact_name_istartswith

    params["contact__name__search"] = contact_name_search

    params["contact__notes"] = contact_notes

    params["contact__notes__icontains"] = contact_notes_icontains

    params["contact__notes__in"] = contact_notes_in

    params["contact__notes__iregex"] = contact_notes_iregex

    params["contact__notes__istartswith"] = contact_notes_istartswith

    params["contact__notes__search"] = contact_notes_search

    params["contact__phone"] = contact_phone

    params["contact__phone__icontains"] = contact_phone_icontains

    params["contact__phone__in"] = contact_phone_in

    params["contact__phone__iregex"] = contact_phone_iregex

    params["contact__phone__istartswith"] = contact_phone_istartswith

    params["contact__phone__search"] = contact_phone_search

    params["contact_id"] = contact_id

    params["contact_id__in"] = contact_id_in

    params["contact_id__isnull"] = contact_id_isnull

    params["created_by"] = created_by

    params["created_by__in"] = created_by_in

    params["created_by__isnull"] = created_by_isnull

    params["description"] = description

    params["description__icontains"] = description_icontains

    params["description__iregex"] = description_iregex

    params["description__istartswith"] = description_istartswith

    params["description__search"] = description_search

    params["duration"] = duration

    params["duration__gt"] = duration_gt

    params["duration__gte"] = duration_gte

    params["duration__lt"] = duration_lt

    params["duration__lte"] = duration_lte

    params["external_id"] = external_id

    params["external_id__icontains"] = external_id_icontains

    params["external_id__in"] = external_id_in

    params["external_id__iregex"] = external_id_iregex

    params["external_id__isnull"] = external_id_isnull

    params["external_id__istartswith"] = external_id_istartswith

    params["external_id__search"] = external_id_search

    params["fields"] = fields

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["id"] = id

    params["id__in"] = id_in

    params["is_optimal"] = is_optimal

    params["is_optimal__isnull"] = is_optimal_isnull

    params["metadata__accepted_distance"] = metadata_accepted_distance

    params["metadata__accepted_distance__gt"] = metadata_accepted_distance_gt

    params["metadata__accepted_distance__gte"] = metadata_accepted_distance_gte

    params["metadata__accepted_distance__lt"] = metadata_accepted_distance_lt

    params["metadata__accepted_distance__lte"] = metadata_accepted_distance_lte

    params["metadata__accepted_duration"] = metadata_accepted_duration

    params["metadata__accepted_duration__gt"] = metadata_accepted_duration_gt

    params["metadata__accepted_duration__gte"] = metadata_accepted_duration_gte

    params["metadata__accepted_duration__lt"] = metadata_accepted_duration_lt

    params["metadata__accepted_duration__lte"] = metadata_accepted_duration_lte

    params["metadata__active_distance"] = metadata_active_distance

    params["metadata__active_distance__gt"] = metadata_active_distance_gt

    params["metadata__active_distance__gte"] = metadata_active_distance_gte

    params["metadata__active_distance__lt"] = metadata_active_distance_lt

    params["metadata__active_distance__lte"] = metadata_active_distance_lte

    params["metadata__active_duration"] = metadata_active_duration

    params["metadata__active_duration__gt"] = metadata_active_duration_gt

    params["metadata__active_duration__gte"] = metadata_active_duration_gte

    params["metadata__active_duration__lt"] = metadata_active_duration_lt

    params["metadata__active_duration__lte"] = metadata_active_duration_lte

    params["metadata__assigned_distance"] = metadata_assigned_distance

    params["metadata__assigned_distance__gt"] = metadata_assigned_distance_gt

    params["metadata__assigned_distance__gte"] = metadata_assigned_distance_gte

    params["metadata__assigned_distance__lt"] = metadata_assigned_distance_lt

    params["metadata__assigned_distance__lte"] = metadata_assigned_distance_lte

    params["metadata__assigned_duration"] = metadata_assigned_duration

    params["metadata__assigned_duration__gt"] = metadata_assigned_duration_gt

    params["metadata__assigned_duration__gte"] = metadata_assigned_duration_gte

    params["metadata__assigned_duration__lt"] = metadata_assigned_duration_lt

    params["metadata__assigned_duration__lte"] = metadata_assigned_duration_lte

    params["metadata__cancelled_distance"] = metadata_cancelled_distance

    params["metadata__cancelled_distance__gt"] = metadata_cancelled_distance_gt

    params["metadata__cancelled_distance__gte"] = metadata_cancelled_distance_gte

    params["metadata__cancelled_distance__lt"] = metadata_cancelled_distance_lt

    params["metadata__cancelled_distance__lte"] = metadata_cancelled_distance_lte

    params["metadata__cancelled_duration"] = metadata_cancelled_duration

    params["metadata__cancelled_duration__gt"] = metadata_cancelled_duration_gt

    params["metadata__cancelled_duration__gte"] = metadata_cancelled_duration_gte

    params["metadata__cancelled_duration__lt"] = metadata_cancelled_duration_lt

    params["metadata__cancelled_duration__lte"] = metadata_cancelled_duration_lte

    params["metadata__completed_distance"] = metadata_completed_distance

    params["metadata__completed_distance__gt"] = metadata_completed_distance_gt

    params["metadata__completed_distance__gte"] = metadata_completed_distance_gte

    params["metadata__completed_distance__lt"] = metadata_completed_distance_lt

    params["metadata__completed_distance__lte"] = metadata_completed_distance_lte

    params["metadata__completed_duration"] = metadata_completed_duration

    params["metadata__completed_duration__gt"] = metadata_completed_duration_gt

    params["metadata__completed_duration__gte"] = metadata_completed_duration_gte

    params["metadata__completed_duration__lt"] = metadata_completed_duration_lt

    params["metadata__completed_duration__lte"] = metadata_completed_duration_lte

    params["metadata__documents_count"] = metadata_documents_count

    params["metadata__documents_count__gt"] = metadata_documents_count_gt

    params["metadata__documents_count__gte"] = metadata_documents_count_gte

    params["metadata__documents_count__lt"] = metadata_documents_count_lt

    params["metadata__documents_count__lte"] = metadata_documents_count_lte

    params["metadata__events_count"] = metadata_events_count

    params["metadata__events_count__gt"] = metadata_events_count_gt

    params["metadata__events_count__gte"] = metadata_events_count_gte

    params["metadata__events_count__lt"] = metadata_events_count_lt

    params["metadata__events_count__lte"] = metadata_events_count_lte

    params["metadata__failed_distance"] = metadata_failed_distance

    params["metadata__failed_distance__gt"] = metadata_failed_distance_gt

    params["metadata__failed_distance__gte"] = metadata_failed_distance_gte

    params["metadata__failed_distance__lt"] = metadata_failed_distance_lt

    params["metadata__failed_distance__lte"] = metadata_failed_distance_lte

    params["metadata__failed_duration"] = metadata_failed_duration

    params["metadata__failed_duration__gt"] = metadata_failed_duration_gt

    params["metadata__failed_duration__gte"] = metadata_failed_duration_gte

    params["metadata__failed_duration__lt"] = metadata_failed_duration_lt

    params["metadata__failed_duration__lte"] = metadata_failed_duration_lte

    params["metadata__forms_completed_count"] = metadata_forms_completed_count

    params["metadata__forms_completed_count__gt"] = metadata_forms_completed_count_gt

    params["metadata__forms_completed_count__gte"] = metadata_forms_completed_count_gte

    params["metadata__forms_completed_count__lt"] = metadata_forms_completed_count_lt

    params["metadata__forms_completed_count__lte"] = metadata_forms_completed_count_lte

    params["metadata__forms_count"] = metadata_forms_count

    params["metadata__forms_count__gt"] = metadata_forms_count_gt

    params["metadata__forms_count__gte"] = metadata_forms_count_gte

    params["metadata__forms_count__lt"] = metadata_forms_count_lt

    params["metadata__forms_count__lte"] = metadata_forms_count_lte

    params["metadata__signatures_count"] = metadata_signatures_count

    params["metadata__signatures_count__gt"] = metadata_signatures_count_gt

    params["metadata__signatures_count__gte"] = metadata_signatures_count_gte

    params["metadata__signatures_count__lt"] = metadata_signatures_count_lt

    params["metadata__signatures_count__lte"] = metadata_signatures_count_lte

    params["metadata__task_event_notes_count"] = metadata_task_event_notes_count

    params["metadata__task_event_notes_count__gt"] = metadata_task_event_notes_count_gt

    params["metadata__task_event_notes_count__gte"] = metadata_task_event_notes_count_gte

    params["metadata__task_event_notes_count__lt"] = metadata_task_event_notes_count_lt

    params["metadata__task_event_notes_count__lte"] = metadata_task_event_notes_count_lte

    params["metadata__transit_distance"] = metadata_transit_distance

    params["metadata__transit_distance__gt"] = metadata_transit_distance_gt

    params["metadata__transit_distance__gte"] = metadata_transit_distance_gte

    params["metadata__transit_distance__lt"] = metadata_transit_distance_lt

    params["metadata__transit_distance__lte"] = metadata_transit_distance_lte

    params["metadata__transit_duration"] = metadata_transit_duration

    params["metadata__transit_duration__gt"] = metadata_transit_duration_gt

    params["metadata__transit_duration__gte"] = metadata_transit_duration_gte

    params["metadata__transit_duration__lt"] = metadata_transit_duration_lt

    params["metadata__transit_duration__lte"] = metadata_transit_duration_lte

    params["metadata__unassigned_distance"] = metadata_unassigned_distance

    params["metadata__unassigned_distance__gt"] = metadata_unassigned_distance_gt

    params["metadata__unassigned_distance__gte"] = metadata_unassigned_distance_gte

    params["metadata__unassigned_distance__lt"] = metadata_unassigned_distance_lt

    params["metadata__unassigned_distance__lte"] = metadata_unassigned_distance_lte

    params["metadata__unassigned_duration"] = metadata_unassigned_duration

    params["metadata__unassigned_duration__gt"] = metadata_unassigned_duration_gt

    params["metadata__unassigned_duration__gte"] = metadata_unassigned_duration_gte

    params["metadata__unassigned_duration__lt"] = metadata_unassigned_duration_lt

    params["metadata__unassigned_duration__lte"] = metadata_unassigned_duration_lte

    params["order__auto_assign"] = order_auto_assign

    params["order__created_by"] = order_created_by

    params["order__created_by__in"] = order_created_by_in

    params["order__created_by__isnull"] = order_created_by_isnull

    params["order__external_id"] = order_external_id

    params["order__external_id__icontains"] = order_external_id_icontains

    params["order__external_id__in"] = order_external_id_in

    params["order__external_id__iregex"] = order_external_id_iregex

    params["order__external_id__isnull"] = order_external_id_isnull

    params["order__external_id__istartswith"] = order_external_id_istartswith

    params["order__external_id__search"] = order_external_id_search

    params["order__reference"] = order_reference

    params["order__reference__icontains"] = order_reference_icontains

    params["order__reference__in"] = order_reference_in

    params["order__reference__iregex"] = order_reference_iregex

    params["order__reference__istartswith"] = order_reference_istartswith

    params["order__reference__search"] = order_reference_search

    params["order_id"] = order_id

    params["order_id__in"] = order_id_in

    params["order_id__isnull"] = order_id_isnull

    params["orderer_id"] = orderer_id

    params["orderer_id__in"] = orderer_id_in

    params["orderer_id__isnull"] = orderer_id_isnull

    params["ordering"] = ordering

    params["owner_id"] = owner_id

    params["owner_id__in"] = owner_id_in

    params["owner_id__isnull"] = owner_id_isnull

    params["page"] = page

    params["page_size"] = page_size

    params["priority"] = priority

    params["priority__gt"] = priority_gt

    params["priority__gte"] = priority_gte

    params["priority__in"] = priority_in

    params["priority__lt"] = priority_lt

    params["priority__lte"] = priority_lte

    params["receiver_id"] = receiver_id

    params["receiver_id__in"] = receiver_id_in

    params["receiver_id__isnull"] = receiver_id_isnull

    params["reference"] = reference

    params["reference__icontains"] = reference_icontains

    params["reference__in"] = reference_in

    params["reference__iregex"] = reference_iregex

    params["reference__istartswith"] = reference_istartswith

    params["reference__search"] = reference_search

    params["route_id"] = route_id

    params["route_id__in"] = route_id_in

    params["route_id__isnull"] = route_id_isnull

    params["search"] = search

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["state__in"] = state_in

    params["unassignee_id"] = unassignee_id

    params["unassignee_id__in"] = unassignee_id_in

    params["unassignee_id__isnull"] = unassignee_id_isnull

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[TaskExport]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_task_export_list_item_data in _response_200:
            componentsschemas_paginated_task_export_list_item = TaskExport.from_dict(
                componentsschemas_paginated_task_export_list_item_data
            )

            response_200.append(componentsschemas_paginated_task_export_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[TaskExport]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    address_apartment_number: Union[Unset, None, str] = UNSET,
    address_apartment_number_icontains: Union[Unset, None, str] = UNSET,
    address_apartment_number_in: Union[Unset, None, str] = UNSET,
    address_apartment_number_iregex: Union[Unset, None, str] = UNSET,
    address_apartment_number_istartswith: Union[Unset, None, str] = UNSET,
    address_apartment_number_search: Union[Unset, None, str] = UNSET,
    address_city: Union[Unset, None, str] = UNSET,
    address_city_icontains: Union[Unset, None, str] = UNSET,
    address_city_in: Union[Unset, None, str] = UNSET,
    address_city_iregex: Union[Unset, None, str] = UNSET,
    address_city_istartswith: Union[Unset, None, str] = UNSET,
    address_city_search: Union[Unset, None, str] = UNSET,
    address_country: Union[Unset, None, str] = UNSET,
    address_country_icontains: Union[Unset, None, str] = UNSET,
    address_country_in: Union[Unset, None, str] = UNSET,
    address_country_iregex: Union[Unset, None, str] = UNSET,
    address_country_istartswith: Union[Unset, None, str] = UNSET,
    address_country_search: Union[Unset, None, str] = UNSET,
    address_country_code: Union[Unset, None, str] = UNSET,
    address_country_code_icontains: Union[Unset, None, str] = UNSET,
    address_country_code_in: Union[Unset, None, str] = UNSET,
    address_country_code_iregex: Union[Unset, None, str] = UNSET,
    address_country_code_istartswith: Union[Unset, None, str] = UNSET,
    address_country_code_search: Union[Unset, None, str] = UNSET,
    address_formatted_address: Union[Unset, None, str] = UNSET,
    address_formatted_address_icontains: Union[Unset, None, str] = UNSET,
    address_formatted_address_in: Union[Unset, None, str] = UNSET,
    address_formatted_address_iregex: Union[Unset, None, str] = UNSET,
    address_formatted_address_istartswith: Union[Unset, None, str] = UNSET,
    address_formatted_address_search: Union[Unset, None, str] = UNSET,
    address_google_place_id: Union[Unset, None, str] = UNSET,
    address_google_place_id_icontains: Union[Unset, None, str] = UNSET,
    address_google_place_id_in: Union[Unset, None, str] = UNSET,
    address_google_place_id_iregex: Union[Unset, None, str] = UNSET,
    address_google_place_id_istartswith: Union[Unset, None, str] = UNSET,
    address_google_place_id_search: Union[Unset, None, str] = UNSET,
    address_house_number: Union[Unset, None, str] = UNSET,
    address_house_number_icontains: Union[Unset, None, str] = UNSET,
    address_house_number_in: Union[Unset, None, str] = UNSET,
    address_house_number_iregex: Union[Unset, None, str] = UNSET,
    address_house_number_istartswith: Union[Unset, None, str] = UNSET,
    address_house_number_search: Union[Unset, None, str] = UNSET,
    address_point_of_interest: Union[Unset, None, str] = UNSET,
    address_point_of_interest_icontains: Union[Unset, None, str] = UNSET,
    address_point_of_interest_in: Union[Unset, None, str] = UNSET,
    address_point_of_interest_iregex: Union[Unset, None, str] = UNSET,
    address_point_of_interest_istartswith: Union[Unset, None, str] = UNSET,
    address_point_of_interest_search: Union[Unset, None, str] = UNSET,
    address_postal_code: Union[Unset, None, str] = UNSET,
    address_postal_code_icontains: Union[Unset, None, str] = UNSET,
    address_postal_code_in: Union[Unset, None, str] = UNSET,
    address_postal_code_iregex: Union[Unset, None, str] = UNSET,
    address_postal_code_istartswith: Union[Unset, None, str] = UNSET,
    address_postal_code_search: Union[Unset, None, str] = UNSET,
    address_raw_address: Union[Unset, None, str] = UNSET,
    address_raw_address_icontains: Union[Unset, None, str] = UNSET,
    address_raw_address_in: Union[Unset, None, str] = UNSET,
    address_raw_address_iregex: Union[Unset, None, str] = UNSET,
    address_raw_address_istartswith: Union[Unset, None, str] = UNSET,
    address_raw_address_search: Union[Unset, None, str] = UNSET,
    address_state: Union[Unset, None, str] = UNSET,
    address_state_icontains: Union[Unset, None, str] = UNSET,
    address_state_in: Union[Unset, None, str] = UNSET,
    address_state_iregex: Union[Unset, None, str] = UNSET,
    address_state_istartswith: Union[Unset, None, str] = UNSET,
    address_state_search: Union[Unset, None, str] = UNSET,
    address_street: Union[Unset, None, str] = UNSET,
    address_street_icontains: Union[Unset, None, str] = UNSET,
    address_street_in: Union[Unset, None, str] = UNSET,
    address_street_iregex: Union[Unset, None, str] = UNSET,
    address_street_istartswith: Union[Unset, None, str] = UNSET,
    address_street_search: Union[Unset, None, str] = UNSET,
    address_id: Union[Unset, None, str] = UNSET,
    address_id_in: Union[Unset, None, str] = UNSET,
    address_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_email: Union[Unset, None, str] = UNSET,
    assignee_email_icontains: Union[Unset, None, str] = UNSET,
    assignee_email_iregex: Union[Unset, None, str] = UNSET,
    assignee_email_isnull: Union[Unset, None, str] = UNSET,
    assignee_email_istartswith: Union[Unset, None, str] = UNSET,
    assignee_email_search: Union[Unset, None, str] = UNSET,
    assignee_first_name: Union[Unset, None, str] = UNSET,
    assignee_first_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_first_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_first_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_first_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_first_name_search: Union[Unset, None, str] = UNSET,
    assignee_last_name: Union[Unset, None, str] = UNSET,
    assignee_last_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_last_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_last_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_last_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_last_name_search: Union[Unset, None, str] = UNSET,
    assignee_phone: Union[Unset, None, str] = UNSET,
    assignee_phone_icontains: Union[Unset, None, str] = UNSET,
    assignee_phone_iregex: Union[Unset, None, str] = UNSET,
    assignee_phone_isnull: Union[Unset, None, str] = UNSET,
    assignee_phone_istartswith: Union[Unset, None, str] = UNSET,
    assignee_phone_search: Union[Unset, None, str] = UNSET,
    assignee_id: Union[Unset, None, str] = UNSET,
    assignee_id_in: Union[Unset, None, str] = UNSET,
    assignee_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_proximity: Union[Unset, None, TaskExportsListAssigneeProximity] = UNSET,
    assignee_proximity_in: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskExportsListCategory] = UNSET,
    category_in: Union[Unset, None, str] = UNSET,
    contact_company_icontains: Union[Unset, None, str] = UNSET,
    contact_company_in: Union[Unset, None, str] = UNSET,
    contact_company_iregex: Union[Unset, None, str] = UNSET,
    contact_company_istartswith: Union[Unset, None, str] = UNSET,
    contact_company_search: Union[Unset, None, str] = UNSET,
    contact_email: Union[Unset, None, str] = UNSET,
    contact_email_icontains: Union[Unset, None, str] = UNSET,
    contact_email_in: Union[Unset, None, str] = UNSET,
    contact_email_iregex: Union[Unset, None, str] = UNSET,
    contact_email_istartswith: Union[Unset, None, str] = UNSET,
    contact_email_search: Union[Unset, None, str] = UNSET,
    contact_name: Union[Unset, None, str] = UNSET,
    contact_name_icontains: Union[Unset, None, str] = UNSET,
    contact_name_in: Union[Unset, None, str] = UNSET,
    contact_name_iregex: Union[Unset, None, str] = UNSET,
    contact_name_istartswith: Union[Unset, None, str] = UNSET,
    contact_name_search: Union[Unset, None, str] = UNSET,
    contact_notes: Union[Unset, None, str] = UNSET,
    contact_notes_icontains: Union[Unset, None, str] = UNSET,
    contact_notes_in: Union[Unset, None, str] = UNSET,
    contact_notes_iregex: Union[Unset, None, str] = UNSET,
    contact_notes_istartswith: Union[Unset, None, str] = UNSET,
    contact_notes_search: Union[Unset, None, str] = UNSET,
    contact_phone: Union[Unset, None, str] = UNSET,
    contact_phone_icontains: Union[Unset, None, str] = UNSET,
    contact_phone_in: Union[Unset, None, str] = UNSET,
    contact_phone_iregex: Union[Unset, None, str] = UNSET,
    contact_phone_istartswith: Union[Unset, None, str] = UNSET,
    contact_phone_search: Union[Unset, None, str] = UNSET,
    contact_id: Union[Unset, None, str] = UNSET,
    contact_id_in: Union[Unset, None, str] = UNSET,
    contact_id_isnull: Union[Unset, None, str] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    created_by_in: Union[Unset, None, str] = UNSET,
    created_by_isnull: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    description_icontains: Union[Unset, None, str] = UNSET,
    description_iregex: Union[Unset, None, str] = UNSET,
    description_istartswith: Union[Unset, None, str] = UNSET,
    description_search: Union[Unset, None, str] = UNSET,
    duration: Union[Unset, None, str] = UNSET,
    duration_gt: Union[Unset, None, str] = UNSET,
    duration_gte: Union[Unset, None, str] = UNSET,
    duration_lt: Union[Unset, None, str] = UNSET,
    duration_lte: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    external_id_in: Union[Unset, None, str] = UNSET,
    external_id_iregex: Union[Unset, None, str] = UNSET,
    external_id_isnull: Union[Unset, None, str] = UNSET,
    external_id_istartswith: Union[Unset, None, str] = UNSET,
    external_id_search: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, TaskExportsListFormat] = TaskExportsListFormat.JSON,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    is_optimal: Union[Unset, None, str] = UNSET,
    is_optimal_isnull: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_active_distance: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_active_duration: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_documents_count: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gte: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lte: Union[Unset, None, str] = UNSET,
    metadata_events_count: Union[Unset, None, str] = UNSET,
    metadata_events_count_gt: Union[Unset, None, str] = UNSET,
    metadata_events_count_gte: Union[Unset, None, str] = UNSET,
    metadata_events_count_lt: Union[Unset, None, str] = UNSET,
    metadata_events_count_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_count: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lte: Union[Unset, None, str] = UNSET,
    order_auto_assign: Union[Unset, None, str] = UNSET,
    order_created_by: Union[Unset, None, str] = UNSET,
    order_created_by_in: Union[Unset, None, str] = UNSET,
    order_created_by_isnull: Union[Unset, None, str] = UNSET,
    order_external_id: Union[Unset, None, str] = UNSET,
    order_external_id_icontains: Union[Unset, None, str] = UNSET,
    order_external_id_in: Union[Unset, None, str] = UNSET,
    order_external_id_iregex: Union[Unset, None, str] = UNSET,
    order_external_id_isnull: Union[Unset, None, str] = UNSET,
    order_external_id_istartswith: Union[Unset, None, str] = UNSET,
    order_external_id_search: Union[Unset, None, str] = UNSET,
    order_reference: Union[Unset, None, str] = UNSET,
    order_reference_icontains: Union[Unset, None, str] = UNSET,
    order_reference_in: Union[Unset, None, str] = UNSET,
    order_reference_iregex: Union[Unset, None, str] = UNSET,
    order_reference_istartswith: Union[Unset, None, str] = UNSET,
    order_reference_search: Union[Unset, None, str] = UNSET,
    order_id: Union[Unset, None, str] = UNSET,
    order_id_in: Union[Unset, None, str] = UNSET,
    order_id_isnull: Union[Unset, None, str] = UNSET,
    orderer_id: Union[Unset, None, str] = UNSET,
    orderer_id_in: Union[Unset, None, str] = UNSET,
    orderer_id_isnull: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    owner_id: Union[Unset, None, str] = UNSET,
    owner_id_in: Union[Unset, None, str] = UNSET,
    owner_id_isnull: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    priority_gt: Union[Unset, None, str] = UNSET,
    priority_gte: Union[Unset, None, str] = UNSET,
    priority_in: Union[Unset, None, str] = UNSET,
    priority_lt: Union[Unset, None, str] = UNSET,
    priority_lte: Union[Unset, None, str] = UNSET,
    receiver_id: Union[Unset, None, str] = UNSET,
    receiver_id_in: Union[Unset, None, str] = UNSET,
    receiver_id_isnull: Union[Unset, None, str] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    reference_icontains: Union[Unset, None, str] = UNSET,
    reference_in: Union[Unset, None, str] = UNSET,
    reference_iregex: Union[Unset, None, str] = UNSET,
    reference_istartswith: Union[Unset, None, str] = UNSET,
    reference_search: Union[Unset, None, str] = UNSET,
    route_id: Union[Unset, None, str] = UNSET,
    route_id_in: Union[Unset, None, str] = UNSET,
    route_id_isnull: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, TaskExportsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    unassignee_id: Union[Unset, None, str] = UNSET,
    unassignee_id_in: Union[Unset, None, str] = UNSET,
    unassignee_id_isnull: Union[Unset, None, str] = UNSET,
) -> Response[List[TaskExport]]:
    """This view has multiple renderer classes available: `json` and `xlsx`. In order to export the data as
    an excel file, just set query argument `format` to `xlsx`.When downloading `xlsx` format, use Accept
    header `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; version=...`

    The user can request what fields and in what order will be rendered using query argument `fields`.
    This is a comma separated list of field names used in the API. Available fields are visible in the
    example.
    Also metafields can be added to the response. For this just add them as fields, using structure
    `metafields__{metafield.namespace}__{metafield.key}`.

    When exporting to **excel**, the column names may be changed based on account metafield names or
    pre-defined field name and width mapping.

    Changes in version 2.2.1:
     * field names have been updated to reflect the Task fields schema and filters.
     * Invalid fields in fields request will return a ValidationError.
     * Account filter is required.
     * AccountRole display name is annotated to user objects.
     * 'task_event_notes' is dropped.
     * 'contact_phone' and 'contact_email' is replaced with 'contact_phones' and 'contact_emails'.

    Args:
        address_apartment_number (Union[Unset, None, str]):
        address_apartment_number_icontains (Union[Unset, None, str]):
        address_apartment_number_in (Union[Unset, None, str]):
        address_apartment_number_iregex (Union[Unset, None, str]):
        address_apartment_number_istartswith (Union[Unset, None, str]):
        address_apartment_number_search (Union[Unset, None, str]):
        address_city (Union[Unset, None, str]):
        address_city_icontains (Union[Unset, None, str]):
        address_city_in (Union[Unset, None, str]):
        address_city_iregex (Union[Unset, None, str]):
        address_city_istartswith (Union[Unset, None, str]):
        address_city_search (Union[Unset, None, str]):
        address_country (Union[Unset, None, str]):
        address_country_icontains (Union[Unset, None, str]):
        address_country_in (Union[Unset, None, str]):
        address_country_iregex (Union[Unset, None, str]):
        address_country_istartswith (Union[Unset, None, str]):
        address_country_search (Union[Unset, None, str]):
        address_country_code (Union[Unset, None, str]):
        address_country_code_icontains (Union[Unset, None, str]):
        address_country_code_in (Union[Unset, None, str]):
        address_country_code_iregex (Union[Unset, None, str]):
        address_country_code_istartswith (Union[Unset, None, str]):
        address_country_code_search (Union[Unset, None, str]):
        address_formatted_address (Union[Unset, None, str]):
        address_formatted_address_icontains (Union[Unset, None, str]):
        address_formatted_address_in (Union[Unset, None, str]):
        address_formatted_address_iregex (Union[Unset, None, str]):
        address_formatted_address_istartswith (Union[Unset, None, str]):
        address_formatted_address_search (Union[Unset, None, str]):
        address_google_place_id (Union[Unset, None, str]):
        address_google_place_id_icontains (Union[Unset, None, str]):
        address_google_place_id_in (Union[Unset, None, str]):
        address_google_place_id_iregex (Union[Unset, None, str]):
        address_google_place_id_istartswith (Union[Unset, None, str]):
        address_google_place_id_search (Union[Unset, None, str]):
        address_house_number (Union[Unset, None, str]):
        address_house_number_icontains (Union[Unset, None, str]):
        address_house_number_in (Union[Unset, None, str]):
        address_house_number_iregex (Union[Unset, None, str]):
        address_house_number_istartswith (Union[Unset, None, str]):
        address_house_number_search (Union[Unset, None, str]):
        address_point_of_interest (Union[Unset, None, str]):
        address_point_of_interest_icontains (Union[Unset, None, str]):
        address_point_of_interest_in (Union[Unset, None, str]):
        address_point_of_interest_iregex (Union[Unset, None, str]):
        address_point_of_interest_istartswith (Union[Unset, None, str]):
        address_point_of_interest_search (Union[Unset, None, str]):
        address_postal_code (Union[Unset, None, str]):
        address_postal_code_icontains (Union[Unset, None, str]):
        address_postal_code_in (Union[Unset, None, str]):
        address_postal_code_iregex (Union[Unset, None, str]):
        address_postal_code_istartswith (Union[Unset, None, str]):
        address_postal_code_search (Union[Unset, None, str]):
        address_raw_address (Union[Unset, None, str]):
        address_raw_address_icontains (Union[Unset, None, str]):
        address_raw_address_in (Union[Unset, None, str]):
        address_raw_address_iregex (Union[Unset, None, str]):
        address_raw_address_istartswith (Union[Unset, None, str]):
        address_raw_address_search (Union[Unset, None, str]):
        address_state (Union[Unset, None, str]):
        address_state_icontains (Union[Unset, None, str]):
        address_state_in (Union[Unset, None, str]):
        address_state_iregex (Union[Unset, None, str]):
        address_state_istartswith (Union[Unset, None, str]):
        address_state_search (Union[Unset, None, str]):
        address_street (Union[Unset, None, str]):
        address_street_icontains (Union[Unset, None, str]):
        address_street_in (Union[Unset, None, str]):
        address_street_iregex (Union[Unset, None, str]):
        address_street_istartswith (Union[Unset, None, str]):
        address_street_search (Union[Unset, None, str]):
        address_id (Union[Unset, None, str]):
        address_id_in (Union[Unset, None, str]):
        address_id_isnull (Union[Unset, None, str]):
        assignee_email (Union[Unset, None, str]):
        assignee_email_icontains (Union[Unset, None, str]):
        assignee_email_iregex (Union[Unset, None, str]):
        assignee_email_isnull (Union[Unset, None, str]):
        assignee_email_istartswith (Union[Unset, None, str]):
        assignee_email_search (Union[Unset, None, str]):
        assignee_first_name (Union[Unset, None, str]):
        assignee_first_name_icontains (Union[Unset, None, str]):
        assignee_first_name_iregex (Union[Unset, None, str]):
        assignee_first_name_isnull (Union[Unset, None, str]):
        assignee_first_name_istartswith (Union[Unset, None, str]):
        assignee_first_name_search (Union[Unset, None, str]):
        assignee_last_name (Union[Unset, None, str]):
        assignee_last_name_icontains (Union[Unset, None, str]):
        assignee_last_name_iregex (Union[Unset, None, str]):
        assignee_last_name_isnull (Union[Unset, None, str]):
        assignee_last_name_istartswith (Union[Unset, None, str]):
        assignee_last_name_search (Union[Unset, None, str]):
        assignee_phone (Union[Unset, None, str]):
        assignee_phone_icontains (Union[Unset, None, str]):
        assignee_phone_iregex (Union[Unset, None, str]):
        assignee_phone_isnull (Union[Unset, None, str]):
        assignee_phone_istartswith (Union[Unset, None, str]):
        assignee_phone_search (Union[Unset, None, str]):
        assignee_id (Union[Unset, None, str]):
        assignee_id_in (Union[Unset, None, str]):
        assignee_id_isnull (Union[Unset, None, str]):
        assignee_proximity (Union[Unset, None, TaskExportsListAssigneeProximity]):
        assignee_proximity_in (Union[Unset, None, str]):
        category (Union[Unset, None, TaskExportsListCategory]):
        category_in (Union[Unset, None, str]):
        contact_company_icontains (Union[Unset, None, str]):
        contact_company_in (Union[Unset, None, str]):
        contact_company_iregex (Union[Unset, None, str]):
        contact_company_istartswith (Union[Unset, None, str]):
        contact_company_search (Union[Unset, None, str]):
        contact_email (Union[Unset, None, str]):
        contact_email_icontains (Union[Unset, None, str]):
        contact_email_in (Union[Unset, None, str]):
        contact_email_iregex (Union[Unset, None, str]):
        contact_email_istartswith (Union[Unset, None, str]):
        contact_email_search (Union[Unset, None, str]):
        contact_name (Union[Unset, None, str]):
        contact_name_icontains (Union[Unset, None, str]):
        contact_name_in (Union[Unset, None, str]):
        contact_name_iregex (Union[Unset, None, str]):
        contact_name_istartswith (Union[Unset, None, str]):
        contact_name_search (Union[Unset, None, str]):
        contact_notes (Union[Unset, None, str]):
        contact_notes_icontains (Union[Unset, None, str]):
        contact_notes_in (Union[Unset, None, str]):
        contact_notes_iregex (Union[Unset, None, str]):
        contact_notes_istartswith (Union[Unset, None, str]):
        contact_notes_search (Union[Unset, None, str]):
        contact_phone (Union[Unset, None, str]):
        contact_phone_icontains (Union[Unset, None, str]):
        contact_phone_in (Union[Unset, None, str]):
        contact_phone_iregex (Union[Unset, None, str]):
        contact_phone_istartswith (Union[Unset, None, str]):
        contact_phone_search (Union[Unset, None, str]):
        contact_id (Union[Unset, None, str]):
        contact_id_in (Union[Unset, None, str]):
        contact_id_isnull (Union[Unset, None, str]):
        created_by (Union[Unset, None, str]):
        created_by_in (Union[Unset, None, str]):
        created_by_isnull (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        description_icontains (Union[Unset, None, str]):
        description_iregex (Union[Unset, None, str]):
        description_istartswith (Union[Unset, None, str]):
        description_search (Union[Unset, None, str]):
        duration (Union[Unset, None, str]):
        duration_gt (Union[Unset, None, str]):
        duration_gte (Union[Unset, None, str]):
        duration_lt (Union[Unset, None, str]):
        duration_lte (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        external_id_in (Union[Unset, None, str]):
        external_id_iregex (Union[Unset, None, str]):
        external_id_isnull (Union[Unset, None, str]):
        external_id_istartswith (Union[Unset, None, str]):
        external_id_search (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):
        format_ (Union[Unset, None, TaskExportsListFormat]):  Default: TaskExportsListFormat.JSON.
        id (Union[Unset, None, str]):
        id_in (Union[Unset, None, str]):
        is_optimal (Union[Unset, None, str]):
        is_optimal_isnull (Union[Unset, None, str]):
        metadata_accepted_distance (Union[Unset, None, str]):
        metadata_accepted_distance_gt (Union[Unset, None, str]):
        metadata_accepted_distance_gte (Union[Unset, None, str]):
        metadata_accepted_distance_lt (Union[Unset, None, str]):
        metadata_accepted_distance_lte (Union[Unset, None, str]):
        metadata_accepted_duration (Union[Unset, None, str]):
        metadata_accepted_duration_gt (Union[Unset, None, str]):
        metadata_accepted_duration_gte (Union[Unset, None, str]):
        metadata_accepted_duration_lt (Union[Unset, None, str]):
        metadata_accepted_duration_lte (Union[Unset, None, str]):
        metadata_active_distance (Union[Unset, None, str]):
        metadata_active_distance_gt (Union[Unset, None, str]):
        metadata_active_distance_gte (Union[Unset, None, str]):
        metadata_active_distance_lt (Union[Unset, None, str]):
        metadata_active_distance_lte (Union[Unset, None, str]):
        metadata_active_duration (Union[Unset, None, str]):
        metadata_active_duration_gt (Union[Unset, None, str]):
        metadata_active_duration_gte (Union[Unset, None, str]):
        metadata_active_duration_lt (Union[Unset, None, str]):
        metadata_active_duration_lte (Union[Unset, None, str]):
        metadata_assigned_distance (Union[Unset, None, str]):
        metadata_assigned_distance_gt (Union[Unset, None, str]):
        metadata_assigned_distance_gte (Union[Unset, None, str]):
        metadata_assigned_distance_lt (Union[Unset, None, str]):
        metadata_assigned_distance_lte (Union[Unset, None, str]):
        metadata_assigned_duration (Union[Unset, None, str]):
        metadata_assigned_duration_gt (Union[Unset, None, str]):
        metadata_assigned_duration_gte (Union[Unset, None, str]):
        metadata_assigned_duration_lt (Union[Unset, None, str]):
        metadata_assigned_duration_lte (Union[Unset, None, str]):
        metadata_cancelled_distance (Union[Unset, None, str]):
        metadata_cancelled_distance_gt (Union[Unset, None, str]):
        metadata_cancelled_distance_gte (Union[Unset, None, str]):
        metadata_cancelled_distance_lt (Union[Unset, None, str]):
        metadata_cancelled_distance_lte (Union[Unset, None, str]):
        metadata_cancelled_duration (Union[Unset, None, str]):
        metadata_cancelled_duration_gt (Union[Unset, None, str]):
        metadata_cancelled_duration_gte (Union[Unset, None, str]):
        metadata_cancelled_duration_lt (Union[Unset, None, str]):
        metadata_cancelled_duration_lte (Union[Unset, None, str]):
        metadata_completed_distance (Union[Unset, None, str]):
        metadata_completed_distance_gt (Union[Unset, None, str]):
        metadata_completed_distance_gte (Union[Unset, None, str]):
        metadata_completed_distance_lt (Union[Unset, None, str]):
        metadata_completed_distance_lte (Union[Unset, None, str]):
        metadata_completed_duration (Union[Unset, None, str]):
        metadata_completed_duration_gt (Union[Unset, None, str]):
        metadata_completed_duration_gte (Union[Unset, None, str]):
        metadata_completed_duration_lt (Union[Unset, None, str]):
        metadata_completed_duration_lte (Union[Unset, None, str]):
        metadata_documents_count (Union[Unset, None, str]):
        metadata_documents_count_gt (Union[Unset, None, str]):
        metadata_documents_count_gte (Union[Unset, None, str]):
        metadata_documents_count_lt (Union[Unset, None, str]):
        metadata_documents_count_lte (Union[Unset, None, str]):
        metadata_events_count (Union[Unset, None, str]):
        metadata_events_count_gt (Union[Unset, None, str]):
        metadata_events_count_gte (Union[Unset, None, str]):
        metadata_events_count_lt (Union[Unset, None, str]):
        metadata_events_count_lte (Union[Unset, None, str]):
        metadata_failed_distance (Union[Unset, None, str]):
        metadata_failed_distance_gt (Union[Unset, None, str]):
        metadata_failed_distance_gte (Union[Unset, None, str]):
        metadata_failed_distance_lt (Union[Unset, None, str]):
        metadata_failed_distance_lte (Union[Unset, None, str]):
        metadata_failed_duration (Union[Unset, None, str]):
        metadata_failed_duration_gt (Union[Unset, None, str]):
        metadata_failed_duration_gte (Union[Unset, None, str]):
        metadata_failed_duration_lt (Union[Unset, None, str]):
        metadata_failed_duration_lte (Union[Unset, None, str]):
        metadata_forms_completed_count (Union[Unset, None, str]):
        metadata_forms_completed_count_gt (Union[Unset, None, str]):
        metadata_forms_completed_count_gte (Union[Unset, None, str]):
        metadata_forms_completed_count_lt (Union[Unset, None, str]):
        metadata_forms_completed_count_lte (Union[Unset, None, str]):
        metadata_forms_count (Union[Unset, None, str]):
        metadata_forms_count_gt (Union[Unset, None, str]):
        metadata_forms_count_gte (Union[Unset, None, str]):
        metadata_forms_count_lt (Union[Unset, None, str]):
        metadata_forms_count_lte (Union[Unset, None, str]):
        metadata_signatures_count (Union[Unset, None, str]):
        metadata_signatures_count_gt (Union[Unset, None, str]):
        metadata_signatures_count_gte (Union[Unset, None, str]):
        metadata_signatures_count_lt (Union[Unset, None, str]):
        metadata_signatures_count_lte (Union[Unset, None, str]):
        metadata_task_event_notes_count (Union[Unset, None, str]):
        metadata_task_event_notes_count_gt (Union[Unset, None, str]):
        metadata_task_event_notes_count_gte (Union[Unset, None, str]):
        metadata_task_event_notes_count_lt (Union[Unset, None, str]):
        metadata_task_event_notes_count_lte (Union[Unset, None, str]):
        metadata_transit_distance (Union[Unset, None, str]):
        metadata_transit_distance_gt (Union[Unset, None, str]):
        metadata_transit_distance_gte (Union[Unset, None, str]):
        metadata_transit_distance_lt (Union[Unset, None, str]):
        metadata_transit_distance_lte (Union[Unset, None, str]):
        metadata_transit_duration (Union[Unset, None, str]):
        metadata_transit_duration_gt (Union[Unset, None, str]):
        metadata_transit_duration_gte (Union[Unset, None, str]):
        metadata_transit_duration_lt (Union[Unset, None, str]):
        metadata_transit_duration_lte (Union[Unset, None, str]):
        metadata_unassigned_distance (Union[Unset, None, str]):
        metadata_unassigned_distance_gt (Union[Unset, None, str]):
        metadata_unassigned_distance_gte (Union[Unset, None, str]):
        metadata_unassigned_distance_lt (Union[Unset, None, str]):
        metadata_unassigned_distance_lte (Union[Unset, None, str]):
        metadata_unassigned_duration (Union[Unset, None, str]):
        metadata_unassigned_duration_gt (Union[Unset, None, str]):
        metadata_unassigned_duration_gte (Union[Unset, None, str]):
        metadata_unassigned_duration_lt (Union[Unset, None, str]):
        metadata_unassigned_duration_lte (Union[Unset, None, str]):
        order_auto_assign (Union[Unset, None, str]):
        order_created_by (Union[Unset, None, str]):
        order_created_by_in (Union[Unset, None, str]):
        order_created_by_isnull (Union[Unset, None, str]):
        order_external_id (Union[Unset, None, str]):
        order_external_id_icontains (Union[Unset, None, str]):
        order_external_id_in (Union[Unset, None, str]):
        order_external_id_iregex (Union[Unset, None, str]):
        order_external_id_isnull (Union[Unset, None, str]):
        order_external_id_istartswith (Union[Unset, None, str]):
        order_external_id_search (Union[Unset, None, str]):
        order_reference (Union[Unset, None, str]):
        order_reference_icontains (Union[Unset, None, str]):
        order_reference_in (Union[Unset, None, str]):
        order_reference_iregex (Union[Unset, None, str]):
        order_reference_istartswith (Union[Unset, None, str]):
        order_reference_search (Union[Unset, None, str]):
        order_id (Union[Unset, None, str]):
        order_id_in (Union[Unset, None, str]):
        order_id_isnull (Union[Unset, None, str]):
        orderer_id (Union[Unset, None, str]):
        orderer_id_in (Union[Unset, None, str]):
        orderer_id_isnull (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        owner_id (Union[Unset, None, str]):
        owner_id_in (Union[Unset, None, str]):
        owner_id_isnull (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        priority (Union[Unset, None, str]):
        priority_gt (Union[Unset, None, str]):
        priority_gte (Union[Unset, None, str]):
        priority_in (Union[Unset, None, str]):
        priority_lt (Union[Unset, None, str]):
        priority_lte (Union[Unset, None, str]):
        receiver_id (Union[Unset, None, str]):
        receiver_id_in (Union[Unset, None, str]):
        receiver_id_isnull (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        reference_icontains (Union[Unset, None, str]):
        reference_in (Union[Unset, None, str]):
        reference_iregex (Union[Unset, None, str]):
        reference_istartswith (Union[Unset, None, str]):
        reference_search (Union[Unset, None, str]):
        route_id (Union[Unset, None, str]):
        route_id_in (Union[Unset, None, str]):
        route_id_isnull (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, TaskExportsListState]):
        state_in (Union[Unset, None, str]):
        unassignee_id (Union[Unset, None, str]):
        unassignee_id_in (Union[Unset, None, str]):
        unassignee_id_isnull (Union[Unset, None, str]):

    Returns:
        Response[List[TaskExport]]
    """

    kwargs = _get_kwargs(
        client=client,
        address_apartment_number=address_apartment_number,
        address_apartment_number_icontains=address_apartment_number_icontains,
        address_apartment_number_in=address_apartment_number_in,
        address_apartment_number_iregex=address_apartment_number_iregex,
        address_apartment_number_istartswith=address_apartment_number_istartswith,
        address_apartment_number_search=address_apartment_number_search,
        address_city=address_city,
        address_city_icontains=address_city_icontains,
        address_city_in=address_city_in,
        address_city_iregex=address_city_iregex,
        address_city_istartswith=address_city_istartswith,
        address_city_search=address_city_search,
        address_country=address_country,
        address_country_icontains=address_country_icontains,
        address_country_in=address_country_in,
        address_country_iregex=address_country_iregex,
        address_country_istartswith=address_country_istartswith,
        address_country_search=address_country_search,
        address_country_code=address_country_code,
        address_country_code_icontains=address_country_code_icontains,
        address_country_code_in=address_country_code_in,
        address_country_code_iregex=address_country_code_iregex,
        address_country_code_istartswith=address_country_code_istartswith,
        address_country_code_search=address_country_code_search,
        address_formatted_address=address_formatted_address,
        address_formatted_address_icontains=address_formatted_address_icontains,
        address_formatted_address_in=address_formatted_address_in,
        address_formatted_address_iregex=address_formatted_address_iregex,
        address_formatted_address_istartswith=address_formatted_address_istartswith,
        address_formatted_address_search=address_formatted_address_search,
        address_google_place_id=address_google_place_id,
        address_google_place_id_icontains=address_google_place_id_icontains,
        address_google_place_id_in=address_google_place_id_in,
        address_google_place_id_iregex=address_google_place_id_iregex,
        address_google_place_id_istartswith=address_google_place_id_istartswith,
        address_google_place_id_search=address_google_place_id_search,
        address_house_number=address_house_number,
        address_house_number_icontains=address_house_number_icontains,
        address_house_number_in=address_house_number_in,
        address_house_number_iregex=address_house_number_iregex,
        address_house_number_istartswith=address_house_number_istartswith,
        address_house_number_search=address_house_number_search,
        address_point_of_interest=address_point_of_interest,
        address_point_of_interest_icontains=address_point_of_interest_icontains,
        address_point_of_interest_in=address_point_of_interest_in,
        address_point_of_interest_iregex=address_point_of_interest_iregex,
        address_point_of_interest_istartswith=address_point_of_interest_istartswith,
        address_point_of_interest_search=address_point_of_interest_search,
        address_postal_code=address_postal_code,
        address_postal_code_icontains=address_postal_code_icontains,
        address_postal_code_in=address_postal_code_in,
        address_postal_code_iregex=address_postal_code_iregex,
        address_postal_code_istartswith=address_postal_code_istartswith,
        address_postal_code_search=address_postal_code_search,
        address_raw_address=address_raw_address,
        address_raw_address_icontains=address_raw_address_icontains,
        address_raw_address_in=address_raw_address_in,
        address_raw_address_iregex=address_raw_address_iregex,
        address_raw_address_istartswith=address_raw_address_istartswith,
        address_raw_address_search=address_raw_address_search,
        address_state=address_state,
        address_state_icontains=address_state_icontains,
        address_state_in=address_state_in,
        address_state_iregex=address_state_iregex,
        address_state_istartswith=address_state_istartswith,
        address_state_search=address_state_search,
        address_street=address_street,
        address_street_icontains=address_street_icontains,
        address_street_in=address_street_in,
        address_street_iregex=address_street_iregex,
        address_street_istartswith=address_street_istartswith,
        address_street_search=address_street_search,
        address_id=address_id,
        address_id_in=address_id_in,
        address_id_isnull=address_id_isnull,
        assignee_email=assignee_email,
        assignee_email_icontains=assignee_email_icontains,
        assignee_email_iregex=assignee_email_iregex,
        assignee_email_isnull=assignee_email_isnull,
        assignee_email_istartswith=assignee_email_istartswith,
        assignee_email_search=assignee_email_search,
        assignee_first_name=assignee_first_name,
        assignee_first_name_icontains=assignee_first_name_icontains,
        assignee_first_name_iregex=assignee_first_name_iregex,
        assignee_first_name_isnull=assignee_first_name_isnull,
        assignee_first_name_istartswith=assignee_first_name_istartswith,
        assignee_first_name_search=assignee_first_name_search,
        assignee_last_name=assignee_last_name,
        assignee_last_name_icontains=assignee_last_name_icontains,
        assignee_last_name_iregex=assignee_last_name_iregex,
        assignee_last_name_isnull=assignee_last_name_isnull,
        assignee_last_name_istartswith=assignee_last_name_istartswith,
        assignee_last_name_search=assignee_last_name_search,
        assignee_phone=assignee_phone,
        assignee_phone_icontains=assignee_phone_icontains,
        assignee_phone_iregex=assignee_phone_iregex,
        assignee_phone_isnull=assignee_phone_isnull,
        assignee_phone_istartswith=assignee_phone_istartswith,
        assignee_phone_search=assignee_phone_search,
        assignee_id=assignee_id,
        assignee_id_in=assignee_id_in,
        assignee_id_isnull=assignee_id_isnull,
        assignee_proximity=assignee_proximity,
        assignee_proximity_in=assignee_proximity_in,
        category=category,
        category_in=category_in,
        contact_company_icontains=contact_company_icontains,
        contact_company_in=contact_company_in,
        contact_company_iregex=contact_company_iregex,
        contact_company_istartswith=contact_company_istartswith,
        contact_company_search=contact_company_search,
        contact_email=contact_email,
        contact_email_icontains=contact_email_icontains,
        contact_email_in=contact_email_in,
        contact_email_iregex=contact_email_iregex,
        contact_email_istartswith=contact_email_istartswith,
        contact_email_search=contact_email_search,
        contact_name=contact_name,
        contact_name_icontains=contact_name_icontains,
        contact_name_in=contact_name_in,
        contact_name_iregex=contact_name_iregex,
        contact_name_istartswith=contact_name_istartswith,
        contact_name_search=contact_name_search,
        contact_notes=contact_notes,
        contact_notes_icontains=contact_notes_icontains,
        contact_notes_in=contact_notes_in,
        contact_notes_iregex=contact_notes_iregex,
        contact_notes_istartswith=contact_notes_istartswith,
        contact_notes_search=contact_notes_search,
        contact_phone=contact_phone,
        contact_phone_icontains=contact_phone_icontains,
        contact_phone_in=contact_phone_in,
        contact_phone_iregex=contact_phone_iregex,
        contact_phone_istartswith=contact_phone_istartswith,
        contact_phone_search=contact_phone_search,
        contact_id=contact_id,
        contact_id_in=contact_id_in,
        contact_id_isnull=contact_id_isnull,
        created_by=created_by,
        created_by_in=created_by_in,
        created_by_isnull=created_by_isnull,
        description=description,
        description_icontains=description_icontains,
        description_iregex=description_iregex,
        description_istartswith=description_istartswith,
        description_search=description_search,
        duration=duration,
        duration_gt=duration_gt,
        duration_gte=duration_gte,
        duration_lt=duration_lt,
        duration_lte=duration_lte,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        external_id_in=external_id_in,
        external_id_iregex=external_id_iregex,
        external_id_isnull=external_id_isnull,
        external_id_istartswith=external_id_istartswith,
        external_id_search=external_id_search,
        fields=fields,
        format_=format_,
        id=id,
        id_in=id_in,
        is_optimal=is_optimal,
        is_optimal_isnull=is_optimal_isnull,
        metadata_accepted_distance=metadata_accepted_distance,
        metadata_accepted_distance_gt=metadata_accepted_distance_gt,
        metadata_accepted_distance_gte=metadata_accepted_distance_gte,
        metadata_accepted_distance_lt=metadata_accepted_distance_lt,
        metadata_accepted_distance_lte=metadata_accepted_distance_lte,
        metadata_accepted_duration=metadata_accepted_duration,
        metadata_accepted_duration_gt=metadata_accepted_duration_gt,
        metadata_accepted_duration_gte=metadata_accepted_duration_gte,
        metadata_accepted_duration_lt=metadata_accepted_duration_lt,
        metadata_accepted_duration_lte=metadata_accepted_duration_lte,
        metadata_active_distance=metadata_active_distance,
        metadata_active_distance_gt=metadata_active_distance_gt,
        metadata_active_distance_gte=metadata_active_distance_gte,
        metadata_active_distance_lt=metadata_active_distance_lt,
        metadata_active_distance_lte=metadata_active_distance_lte,
        metadata_active_duration=metadata_active_duration,
        metadata_active_duration_gt=metadata_active_duration_gt,
        metadata_active_duration_gte=metadata_active_duration_gte,
        metadata_active_duration_lt=metadata_active_duration_lt,
        metadata_active_duration_lte=metadata_active_duration_lte,
        metadata_assigned_distance=metadata_assigned_distance,
        metadata_assigned_distance_gt=metadata_assigned_distance_gt,
        metadata_assigned_distance_gte=metadata_assigned_distance_gte,
        metadata_assigned_distance_lt=metadata_assigned_distance_lt,
        metadata_assigned_distance_lte=metadata_assigned_distance_lte,
        metadata_assigned_duration=metadata_assigned_duration,
        metadata_assigned_duration_gt=metadata_assigned_duration_gt,
        metadata_assigned_duration_gte=metadata_assigned_duration_gte,
        metadata_assigned_duration_lt=metadata_assigned_duration_lt,
        metadata_assigned_duration_lte=metadata_assigned_duration_lte,
        metadata_cancelled_distance=metadata_cancelled_distance,
        metadata_cancelled_distance_gt=metadata_cancelled_distance_gt,
        metadata_cancelled_distance_gte=metadata_cancelled_distance_gte,
        metadata_cancelled_distance_lt=metadata_cancelled_distance_lt,
        metadata_cancelled_distance_lte=metadata_cancelled_distance_lte,
        metadata_cancelled_duration=metadata_cancelled_duration,
        metadata_cancelled_duration_gt=metadata_cancelled_duration_gt,
        metadata_cancelled_duration_gte=metadata_cancelled_duration_gte,
        metadata_cancelled_duration_lt=metadata_cancelled_duration_lt,
        metadata_cancelled_duration_lte=metadata_cancelled_duration_lte,
        metadata_completed_distance=metadata_completed_distance,
        metadata_completed_distance_gt=metadata_completed_distance_gt,
        metadata_completed_distance_gte=metadata_completed_distance_gte,
        metadata_completed_distance_lt=metadata_completed_distance_lt,
        metadata_completed_distance_lte=metadata_completed_distance_lte,
        metadata_completed_duration=metadata_completed_duration,
        metadata_completed_duration_gt=metadata_completed_duration_gt,
        metadata_completed_duration_gte=metadata_completed_duration_gte,
        metadata_completed_duration_lt=metadata_completed_duration_lt,
        metadata_completed_duration_lte=metadata_completed_duration_lte,
        metadata_documents_count=metadata_documents_count,
        metadata_documents_count_gt=metadata_documents_count_gt,
        metadata_documents_count_gte=metadata_documents_count_gte,
        metadata_documents_count_lt=metadata_documents_count_lt,
        metadata_documents_count_lte=metadata_documents_count_lte,
        metadata_events_count=metadata_events_count,
        metadata_events_count_gt=metadata_events_count_gt,
        metadata_events_count_gte=metadata_events_count_gte,
        metadata_events_count_lt=metadata_events_count_lt,
        metadata_events_count_lte=metadata_events_count_lte,
        metadata_failed_distance=metadata_failed_distance,
        metadata_failed_distance_gt=metadata_failed_distance_gt,
        metadata_failed_distance_gte=metadata_failed_distance_gte,
        metadata_failed_distance_lt=metadata_failed_distance_lt,
        metadata_failed_distance_lte=metadata_failed_distance_lte,
        metadata_failed_duration=metadata_failed_duration,
        metadata_failed_duration_gt=metadata_failed_duration_gt,
        metadata_failed_duration_gte=metadata_failed_duration_gte,
        metadata_failed_duration_lt=metadata_failed_duration_lt,
        metadata_failed_duration_lte=metadata_failed_duration_lte,
        metadata_forms_completed_count=metadata_forms_completed_count,
        metadata_forms_completed_count_gt=metadata_forms_completed_count_gt,
        metadata_forms_completed_count_gte=metadata_forms_completed_count_gte,
        metadata_forms_completed_count_lt=metadata_forms_completed_count_lt,
        metadata_forms_completed_count_lte=metadata_forms_completed_count_lte,
        metadata_forms_count=metadata_forms_count,
        metadata_forms_count_gt=metadata_forms_count_gt,
        metadata_forms_count_gte=metadata_forms_count_gte,
        metadata_forms_count_lt=metadata_forms_count_lt,
        metadata_forms_count_lte=metadata_forms_count_lte,
        metadata_signatures_count=metadata_signatures_count,
        metadata_signatures_count_gt=metadata_signatures_count_gt,
        metadata_signatures_count_gte=metadata_signatures_count_gte,
        metadata_signatures_count_lt=metadata_signatures_count_lt,
        metadata_signatures_count_lte=metadata_signatures_count_lte,
        metadata_task_event_notes_count=metadata_task_event_notes_count,
        metadata_task_event_notes_count_gt=metadata_task_event_notes_count_gt,
        metadata_task_event_notes_count_gte=metadata_task_event_notes_count_gte,
        metadata_task_event_notes_count_lt=metadata_task_event_notes_count_lt,
        metadata_task_event_notes_count_lte=metadata_task_event_notes_count_lte,
        metadata_transit_distance=metadata_transit_distance,
        metadata_transit_distance_gt=metadata_transit_distance_gt,
        metadata_transit_distance_gte=metadata_transit_distance_gte,
        metadata_transit_distance_lt=metadata_transit_distance_lt,
        metadata_transit_distance_lte=metadata_transit_distance_lte,
        metadata_transit_duration=metadata_transit_duration,
        metadata_transit_duration_gt=metadata_transit_duration_gt,
        metadata_transit_duration_gte=metadata_transit_duration_gte,
        metadata_transit_duration_lt=metadata_transit_duration_lt,
        metadata_transit_duration_lte=metadata_transit_duration_lte,
        metadata_unassigned_distance=metadata_unassigned_distance,
        metadata_unassigned_distance_gt=metadata_unassigned_distance_gt,
        metadata_unassigned_distance_gte=metadata_unassigned_distance_gte,
        metadata_unassigned_distance_lt=metadata_unassigned_distance_lt,
        metadata_unassigned_distance_lte=metadata_unassigned_distance_lte,
        metadata_unassigned_duration=metadata_unassigned_duration,
        metadata_unassigned_duration_gt=metadata_unassigned_duration_gt,
        metadata_unassigned_duration_gte=metadata_unassigned_duration_gte,
        metadata_unassigned_duration_lt=metadata_unassigned_duration_lt,
        metadata_unassigned_duration_lte=metadata_unassigned_duration_lte,
        order_auto_assign=order_auto_assign,
        order_created_by=order_created_by,
        order_created_by_in=order_created_by_in,
        order_created_by_isnull=order_created_by_isnull,
        order_external_id=order_external_id,
        order_external_id_icontains=order_external_id_icontains,
        order_external_id_in=order_external_id_in,
        order_external_id_iregex=order_external_id_iregex,
        order_external_id_isnull=order_external_id_isnull,
        order_external_id_istartswith=order_external_id_istartswith,
        order_external_id_search=order_external_id_search,
        order_reference=order_reference,
        order_reference_icontains=order_reference_icontains,
        order_reference_in=order_reference_in,
        order_reference_iregex=order_reference_iregex,
        order_reference_istartswith=order_reference_istartswith,
        order_reference_search=order_reference_search,
        order_id=order_id,
        order_id_in=order_id_in,
        order_id_isnull=order_id_isnull,
        orderer_id=orderer_id,
        orderer_id_in=orderer_id_in,
        orderer_id_isnull=orderer_id_isnull,
        ordering=ordering,
        owner_id=owner_id,
        owner_id_in=owner_id_in,
        owner_id_isnull=owner_id_isnull,
        page=page,
        page_size=page_size,
        priority=priority,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_in=priority_in,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        receiver_id=receiver_id,
        receiver_id_in=receiver_id_in,
        receiver_id_isnull=receiver_id_isnull,
        reference=reference,
        reference_icontains=reference_icontains,
        reference_in=reference_in,
        reference_iregex=reference_iregex,
        reference_istartswith=reference_istartswith,
        reference_search=reference_search,
        route_id=route_id,
        route_id_in=route_id_in,
        route_id_isnull=route_id_isnull,
        search=search,
        state=state,
        state_in=state_in,
        unassignee_id=unassignee_id,
        unassignee_id_in=unassignee_id_in,
        unassignee_id_isnull=unassignee_id_isnull,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    address_apartment_number: Union[Unset, None, str] = UNSET,
    address_apartment_number_icontains: Union[Unset, None, str] = UNSET,
    address_apartment_number_in: Union[Unset, None, str] = UNSET,
    address_apartment_number_iregex: Union[Unset, None, str] = UNSET,
    address_apartment_number_istartswith: Union[Unset, None, str] = UNSET,
    address_apartment_number_search: Union[Unset, None, str] = UNSET,
    address_city: Union[Unset, None, str] = UNSET,
    address_city_icontains: Union[Unset, None, str] = UNSET,
    address_city_in: Union[Unset, None, str] = UNSET,
    address_city_iregex: Union[Unset, None, str] = UNSET,
    address_city_istartswith: Union[Unset, None, str] = UNSET,
    address_city_search: Union[Unset, None, str] = UNSET,
    address_country: Union[Unset, None, str] = UNSET,
    address_country_icontains: Union[Unset, None, str] = UNSET,
    address_country_in: Union[Unset, None, str] = UNSET,
    address_country_iregex: Union[Unset, None, str] = UNSET,
    address_country_istartswith: Union[Unset, None, str] = UNSET,
    address_country_search: Union[Unset, None, str] = UNSET,
    address_country_code: Union[Unset, None, str] = UNSET,
    address_country_code_icontains: Union[Unset, None, str] = UNSET,
    address_country_code_in: Union[Unset, None, str] = UNSET,
    address_country_code_iregex: Union[Unset, None, str] = UNSET,
    address_country_code_istartswith: Union[Unset, None, str] = UNSET,
    address_country_code_search: Union[Unset, None, str] = UNSET,
    address_formatted_address: Union[Unset, None, str] = UNSET,
    address_formatted_address_icontains: Union[Unset, None, str] = UNSET,
    address_formatted_address_in: Union[Unset, None, str] = UNSET,
    address_formatted_address_iregex: Union[Unset, None, str] = UNSET,
    address_formatted_address_istartswith: Union[Unset, None, str] = UNSET,
    address_formatted_address_search: Union[Unset, None, str] = UNSET,
    address_google_place_id: Union[Unset, None, str] = UNSET,
    address_google_place_id_icontains: Union[Unset, None, str] = UNSET,
    address_google_place_id_in: Union[Unset, None, str] = UNSET,
    address_google_place_id_iregex: Union[Unset, None, str] = UNSET,
    address_google_place_id_istartswith: Union[Unset, None, str] = UNSET,
    address_google_place_id_search: Union[Unset, None, str] = UNSET,
    address_house_number: Union[Unset, None, str] = UNSET,
    address_house_number_icontains: Union[Unset, None, str] = UNSET,
    address_house_number_in: Union[Unset, None, str] = UNSET,
    address_house_number_iregex: Union[Unset, None, str] = UNSET,
    address_house_number_istartswith: Union[Unset, None, str] = UNSET,
    address_house_number_search: Union[Unset, None, str] = UNSET,
    address_point_of_interest: Union[Unset, None, str] = UNSET,
    address_point_of_interest_icontains: Union[Unset, None, str] = UNSET,
    address_point_of_interest_in: Union[Unset, None, str] = UNSET,
    address_point_of_interest_iregex: Union[Unset, None, str] = UNSET,
    address_point_of_interest_istartswith: Union[Unset, None, str] = UNSET,
    address_point_of_interest_search: Union[Unset, None, str] = UNSET,
    address_postal_code: Union[Unset, None, str] = UNSET,
    address_postal_code_icontains: Union[Unset, None, str] = UNSET,
    address_postal_code_in: Union[Unset, None, str] = UNSET,
    address_postal_code_iregex: Union[Unset, None, str] = UNSET,
    address_postal_code_istartswith: Union[Unset, None, str] = UNSET,
    address_postal_code_search: Union[Unset, None, str] = UNSET,
    address_raw_address: Union[Unset, None, str] = UNSET,
    address_raw_address_icontains: Union[Unset, None, str] = UNSET,
    address_raw_address_in: Union[Unset, None, str] = UNSET,
    address_raw_address_iregex: Union[Unset, None, str] = UNSET,
    address_raw_address_istartswith: Union[Unset, None, str] = UNSET,
    address_raw_address_search: Union[Unset, None, str] = UNSET,
    address_state: Union[Unset, None, str] = UNSET,
    address_state_icontains: Union[Unset, None, str] = UNSET,
    address_state_in: Union[Unset, None, str] = UNSET,
    address_state_iregex: Union[Unset, None, str] = UNSET,
    address_state_istartswith: Union[Unset, None, str] = UNSET,
    address_state_search: Union[Unset, None, str] = UNSET,
    address_street: Union[Unset, None, str] = UNSET,
    address_street_icontains: Union[Unset, None, str] = UNSET,
    address_street_in: Union[Unset, None, str] = UNSET,
    address_street_iregex: Union[Unset, None, str] = UNSET,
    address_street_istartswith: Union[Unset, None, str] = UNSET,
    address_street_search: Union[Unset, None, str] = UNSET,
    address_id: Union[Unset, None, str] = UNSET,
    address_id_in: Union[Unset, None, str] = UNSET,
    address_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_email: Union[Unset, None, str] = UNSET,
    assignee_email_icontains: Union[Unset, None, str] = UNSET,
    assignee_email_iregex: Union[Unset, None, str] = UNSET,
    assignee_email_isnull: Union[Unset, None, str] = UNSET,
    assignee_email_istartswith: Union[Unset, None, str] = UNSET,
    assignee_email_search: Union[Unset, None, str] = UNSET,
    assignee_first_name: Union[Unset, None, str] = UNSET,
    assignee_first_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_first_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_first_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_first_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_first_name_search: Union[Unset, None, str] = UNSET,
    assignee_last_name: Union[Unset, None, str] = UNSET,
    assignee_last_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_last_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_last_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_last_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_last_name_search: Union[Unset, None, str] = UNSET,
    assignee_phone: Union[Unset, None, str] = UNSET,
    assignee_phone_icontains: Union[Unset, None, str] = UNSET,
    assignee_phone_iregex: Union[Unset, None, str] = UNSET,
    assignee_phone_isnull: Union[Unset, None, str] = UNSET,
    assignee_phone_istartswith: Union[Unset, None, str] = UNSET,
    assignee_phone_search: Union[Unset, None, str] = UNSET,
    assignee_id: Union[Unset, None, str] = UNSET,
    assignee_id_in: Union[Unset, None, str] = UNSET,
    assignee_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_proximity: Union[Unset, None, TaskExportsListAssigneeProximity] = UNSET,
    assignee_proximity_in: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskExportsListCategory] = UNSET,
    category_in: Union[Unset, None, str] = UNSET,
    contact_company_icontains: Union[Unset, None, str] = UNSET,
    contact_company_in: Union[Unset, None, str] = UNSET,
    contact_company_iregex: Union[Unset, None, str] = UNSET,
    contact_company_istartswith: Union[Unset, None, str] = UNSET,
    contact_company_search: Union[Unset, None, str] = UNSET,
    contact_email: Union[Unset, None, str] = UNSET,
    contact_email_icontains: Union[Unset, None, str] = UNSET,
    contact_email_in: Union[Unset, None, str] = UNSET,
    contact_email_iregex: Union[Unset, None, str] = UNSET,
    contact_email_istartswith: Union[Unset, None, str] = UNSET,
    contact_email_search: Union[Unset, None, str] = UNSET,
    contact_name: Union[Unset, None, str] = UNSET,
    contact_name_icontains: Union[Unset, None, str] = UNSET,
    contact_name_in: Union[Unset, None, str] = UNSET,
    contact_name_iregex: Union[Unset, None, str] = UNSET,
    contact_name_istartswith: Union[Unset, None, str] = UNSET,
    contact_name_search: Union[Unset, None, str] = UNSET,
    contact_notes: Union[Unset, None, str] = UNSET,
    contact_notes_icontains: Union[Unset, None, str] = UNSET,
    contact_notes_in: Union[Unset, None, str] = UNSET,
    contact_notes_iregex: Union[Unset, None, str] = UNSET,
    contact_notes_istartswith: Union[Unset, None, str] = UNSET,
    contact_notes_search: Union[Unset, None, str] = UNSET,
    contact_phone: Union[Unset, None, str] = UNSET,
    contact_phone_icontains: Union[Unset, None, str] = UNSET,
    contact_phone_in: Union[Unset, None, str] = UNSET,
    contact_phone_iregex: Union[Unset, None, str] = UNSET,
    contact_phone_istartswith: Union[Unset, None, str] = UNSET,
    contact_phone_search: Union[Unset, None, str] = UNSET,
    contact_id: Union[Unset, None, str] = UNSET,
    contact_id_in: Union[Unset, None, str] = UNSET,
    contact_id_isnull: Union[Unset, None, str] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    created_by_in: Union[Unset, None, str] = UNSET,
    created_by_isnull: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    description_icontains: Union[Unset, None, str] = UNSET,
    description_iregex: Union[Unset, None, str] = UNSET,
    description_istartswith: Union[Unset, None, str] = UNSET,
    description_search: Union[Unset, None, str] = UNSET,
    duration: Union[Unset, None, str] = UNSET,
    duration_gt: Union[Unset, None, str] = UNSET,
    duration_gte: Union[Unset, None, str] = UNSET,
    duration_lt: Union[Unset, None, str] = UNSET,
    duration_lte: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    external_id_in: Union[Unset, None, str] = UNSET,
    external_id_iregex: Union[Unset, None, str] = UNSET,
    external_id_isnull: Union[Unset, None, str] = UNSET,
    external_id_istartswith: Union[Unset, None, str] = UNSET,
    external_id_search: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, TaskExportsListFormat] = TaskExportsListFormat.JSON,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    is_optimal: Union[Unset, None, str] = UNSET,
    is_optimal_isnull: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_active_distance: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_active_duration: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_documents_count: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gte: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lte: Union[Unset, None, str] = UNSET,
    metadata_events_count: Union[Unset, None, str] = UNSET,
    metadata_events_count_gt: Union[Unset, None, str] = UNSET,
    metadata_events_count_gte: Union[Unset, None, str] = UNSET,
    metadata_events_count_lt: Union[Unset, None, str] = UNSET,
    metadata_events_count_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_count: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lte: Union[Unset, None, str] = UNSET,
    order_auto_assign: Union[Unset, None, str] = UNSET,
    order_created_by: Union[Unset, None, str] = UNSET,
    order_created_by_in: Union[Unset, None, str] = UNSET,
    order_created_by_isnull: Union[Unset, None, str] = UNSET,
    order_external_id: Union[Unset, None, str] = UNSET,
    order_external_id_icontains: Union[Unset, None, str] = UNSET,
    order_external_id_in: Union[Unset, None, str] = UNSET,
    order_external_id_iregex: Union[Unset, None, str] = UNSET,
    order_external_id_isnull: Union[Unset, None, str] = UNSET,
    order_external_id_istartswith: Union[Unset, None, str] = UNSET,
    order_external_id_search: Union[Unset, None, str] = UNSET,
    order_reference: Union[Unset, None, str] = UNSET,
    order_reference_icontains: Union[Unset, None, str] = UNSET,
    order_reference_in: Union[Unset, None, str] = UNSET,
    order_reference_iregex: Union[Unset, None, str] = UNSET,
    order_reference_istartswith: Union[Unset, None, str] = UNSET,
    order_reference_search: Union[Unset, None, str] = UNSET,
    order_id: Union[Unset, None, str] = UNSET,
    order_id_in: Union[Unset, None, str] = UNSET,
    order_id_isnull: Union[Unset, None, str] = UNSET,
    orderer_id: Union[Unset, None, str] = UNSET,
    orderer_id_in: Union[Unset, None, str] = UNSET,
    orderer_id_isnull: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    owner_id: Union[Unset, None, str] = UNSET,
    owner_id_in: Union[Unset, None, str] = UNSET,
    owner_id_isnull: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    priority_gt: Union[Unset, None, str] = UNSET,
    priority_gte: Union[Unset, None, str] = UNSET,
    priority_in: Union[Unset, None, str] = UNSET,
    priority_lt: Union[Unset, None, str] = UNSET,
    priority_lte: Union[Unset, None, str] = UNSET,
    receiver_id: Union[Unset, None, str] = UNSET,
    receiver_id_in: Union[Unset, None, str] = UNSET,
    receiver_id_isnull: Union[Unset, None, str] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    reference_icontains: Union[Unset, None, str] = UNSET,
    reference_in: Union[Unset, None, str] = UNSET,
    reference_iregex: Union[Unset, None, str] = UNSET,
    reference_istartswith: Union[Unset, None, str] = UNSET,
    reference_search: Union[Unset, None, str] = UNSET,
    route_id: Union[Unset, None, str] = UNSET,
    route_id_in: Union[Unset, None, str] = UNSET,
    route_id_isnull: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, TaskExportsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    unassignee_id: Union[Unset, None, str] = UNSET,
    unassignee_id_in: Union[Unset, None, str] = UNSET,
    unassignee_id_isnull: Union[Unset, None, str] = UNSET,
) -> Optional[List[TaskExport]]:
    """This view has multiple renderer classes available: `json` and `xlsx`. In order to export the data as
    an excel file, just set query argument `format` to `xlsx`.When downloading `xlsx` format, use Accept
    header `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; version=...`

    The user can request what fields and in what order will be rendered using query argument `fields`.
    This is a comma separated list of field names used in the API. Available fields are visible in the
    example.
    Also metafields can be added to the response. For this just add them as fields, using structure
    `metafields__{metafield.namespace}__{metafield.key}`.

    When exporting to **excel**, the column names may be changed based on account metafield names or
    pre-defined field name and width mapping.

    Changes in version 2.2.1:
     * field names have been updated to reflect the Task fields schema and filters.
     * Invalid fields in fields request will return a ValidationError.
     * Account filter is required.
     * AccountRole display name is annotated to user objects.
     * 'task_event_notes' is dropped.
     * 'contact_phone' and 'contact_email' is replaced with 'contact_phones' and 'contact_emails'.

    Args:
        address_apartment_number (Union[Unset, None, str]):
        address_apartment_number_icontains (Union[Unset, None, str]):
        address_apartment_number_in (Union[Unset, None, str]):
        address_apartment_number_iregex (Union[Unset, None, str]):
        address_apartment_number_istartswith (Union[Unset, None, str]):
        address_apartment_number_search (Union[Unset, None, str]):
        address_city (Union[Unset, None, str]):
        address_city_icontains (Union[Unset, None, str]):
        address_city_in (Union[Unset, None, str]):
        address_city_iregex (Union[Unset, None, str]):
        address_city_istartswith (Union[Unset, None, str]):
        address_city_search (Union[Unset, None, str]):
        address_country (Union[Unset, None, str]):
        address_country_icontains (Union[Unset, None, str]):
        address_country_in (Union[Unset, None, str]):
        address_country_iregex (Union[Unset, None, str]):
        address_country_istartswith (Union[Unset, None, str]):
        address_country_search (Union[Unset, None, str]):
        address_country_code (Union[Unset, None, str]):
        address_country_code_icontains (Union[Unset, None, str]):
        address_country_code_in (Union[Unset, None, str]):
        address_country_code_iregex (Union[Unset, None, str]):
        address_country_code_istartswith (Union[Unset, None, str]):
        address_country_code_search (Union[Unset, None, str]):
        address_formatted_address (Union[Unset, None, str]):
        address_formatted_address_icontains (Union[Unset, None, str]):
        address_formatted_address_in (Union[Unset, None, str]):
        address_formatted_address_iregex (Union[Unset, None, str]):
        address_formatted_address_istartswith (Union[Unset, None, str]):
        address_formatted_address_search (Union[Unset, None, str]):
        address_google_place_id (Union[Unset, None, str]):
        address_google_place_id_icontains (Union[Unset, None, str]):
        address_google_place_id_in (Union[Unset, None, str]):
        address_google_place_id_iregex (Union[Unset, None, str]):
        address_google_place_id_istartswith (Union[Unset, None, str]):
        address_google_place_id_search (Union[Unset, None, str]):
        address_house_number (Union[Unset, None, str]):
        address_house_number_icontains (Union[Unset, None, str]):
        address_house_number_in (Union[Unset, None, str]):
        address_house_number_iregex (Union[Unset, None, str]):
        address_house_number_istartswith (Union[Unset, None, str]):
        address_house_number_search (Union[Unset, None, str]):
        address_point_of_interest (Union[Unset, None, str]):
        address_point_of_interest_icontains (Union[Unset, None, str]):
        address_point_of_interest_in (Union[Unset, None, str]):
        address_point_of_interest_iregex (Union[Unset, None, str]):
        address_point_of_interest_istartswith (Union[Unset, None, str]):
        address_point_of_interest_search (Union[Unset, None, str]):
        address_postal_code (Union[Unset, None, str]):
        address_postal_code_icontains (Union[Unset, None, str]):
        address_postal_code_in (Union[Unset, None, str]):
        address_postal_code_iregex (Union[Unset, None, str]):
        address_postal_code_istartswith (Union[Unset, None, str]):
        address_postal_code_search (Union[Unset, None, str]):
        address_raw_address (Union[Unset, None, str]):
        address_raw_address_icontains (Union[Unset, None, str]):
        address_raw_address_in (Union[Unset, None, str]):
        address_raw_address_iregex (Union[Unset, None, str]):
        address_raw_address_istartswith (Union[Unset, None, str]):
        address_raw_address_search (Union[Unset, None, str]):
        address_state (Union[Unset, None, str]):
        address_state_icontains (Union[Unset, None, str]):
        address_state_in (Union[Unset, None, str]):
        address_state_iregex (Union[Unset, None, str]):
        address_state_istartswith (Union[Unset, None, str]):
        address_state_search (Union[Unset, None, str]):
        address_street (Union[Unset, None, str]):
        address_street_icontains (Union[Unset, None, str]):
        address_street_in (Union[Unset, None, str]):
        address_street_iregex (Union[Unset, None, str]):
        address_street_istartswith (Union[Unset, None, str]):
        address_street_search (Union[Unset, None, str]):
        address_id (Union[Unset, None, str]):
        address_id_in (Union[Unset, None, str]):
        address_id_isnull (Union[Unset, None, str]):
        assignee_email (Union[Unset, None, str]):
        assignee_email_icontains (Union[Unset, None, str]):
        assignee_email_iregex (Union[Unset, None, str]):
        assignee_email_isnull (Union[Unset, None, str]):
        assignee_email_istartswith (Union[Unset, None, str]):
        assignee_email_search (Union[Unset, None, str]):
        assignee_first_name (Union[Unset, None, str]):
        assignee_first_name_icontains (Union[Unset, None, str]):
        assignee_first_name_iregex (Union[Unset, None, str]):
        assignee_first_name_isnull (Union[Unset, None, str]):
        assignee_first_name_istartswith (Union[Unset, None, str]):
        assignee_first_name_search (Union[Unset, None, str]):
        assignee_last_name (Union[Unset, None, str]):
        assignee_last_name_icontains (Union[Unset, None, str]):
        assignee_last_name_iregex (Union[Unset, None, str]):
        assignee_last_name_isnull (Union[Unset, None, str]):
        assignee_last_name_istartswith (Union[Unset, None, str]):
        assignee_last_name_search (Union[Unset, None, str]):
        assignee_phone (Union[Unset, None, str]):
        assignee_phone_icontains (Union[Unset, None, str]):
        assignee_phone_iregex (Union[Unset, None, str]):
        assignee_phone_isnull (Union[Unset, None, str]):
        assignee_phone_istartswith (Union[Unset, None, str]):
        assignee_phone_search (Union[Unset, None, str]):
        assignee_id (Union[Unset, None, str]):
        assignee_id_in (Union[Unset, None, str]):
        assignee_id_isnull (Union[Unset, None, str]):
        assignee_proximity (Union[Unset, None, TaskExportsListAssigneeProximity]):
        assignee_proximity_in (Union[Unset, None, str]):
        category (Union[Unset, None, TaskExportsListCategory]):
        category_in (Union[Unset, None, str]):
        contact_company_icontains (Union[Unset, None, str]):
        contact_company_in (Union[Unset, None, str]):
        contact_company_iregex (Union[Unset, None, str]):
        contact_company_istartswith (Union[Unset, None, str]):
        contact_company_search (Union[Unset, None, str]):
        contact_email (Union[Unset, None, str]):
        contact_email_icontains (Union[Unset, None, str]):
        contact_email_in (Union[Unset, None, str]):
        contact_email_iregex (Union[Unset, None, str]):
        contact_email_istartswith (Union[Unset, None, str]):
        contact_email_search (Union[Unset, None, str]):
        contact_name (Union[Unset, None, str]):
        contact_name_icontains (Union[Unset, None, str]):
        contact_name_in (Union[Unset, None, str]):
        contact_name_iregex (Union[Unset, None, str]):
        contact_name_istartswith (Union[Unset, None, str]):
        contact_name_search (Union[Unset, None, str]):
        contact_notes (Union[Unset, None, str]):
        contact_notes_icontains (Union[Unset, None, str]):
        contact_notes_in (Union[Unset, None, str]):
        contact_notes_iregex (Union[Unset, None, str]):
        contact_notes_istartswith (Union[Unset, None, str]):
        contact_notes_search (Union[Unset, None, str]):
        contact_phone (Union[Unset, None, str]):
        contact_phone_icontains (Union[Unset, None, str]):
        contact_phone_in (Union[Unset, None, str]):
        contact_phone_iregex (Union[Unset, None, str]):
        contact_phone_istartswith (Union[Unset, None, str]):
        contact_phone_search (Union[Unset, None, str]):
        contact_id (Union[Unset, None, str]):
        contact_id_in (Union[Unset, None, str]):
        contact_id_isnull (Union[Unset, None, str]):
        created_by (Union[Unset, None, str]):
        created_by_in (Union[Unset, None, str]):
        created_by_isnull (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        description_icontains (Union[Unset, None, str]):
        description_iregex (Union[Unset, None, str]):
        description_istartswith (Union[Unset, None, str]):
        description_search (Union[Unset, None, str]):
        duration (Union[Unset, None, str]):
        duration_gt (Union[Unset, None, str]):
        duration_gte (Union[Unset, None, str]):
        duration_lt (Union[Unset, None, str]):
        duration_lte (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        external_id_in (Union[Unset, None, str]):
        external_id_iregex (Union[Unset, None, str]):
        external_id_isnull (Union[Unset, None, str]):
        external_id_istartswith (Union[Unset, None, str]):
        external_id_search (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):
        format_ (Union[Unset, None, TaskExportsListFormat]):  Default: TaskExportsListFormat.JSON.
        id (Union[Unset, None, str]):
        id_in (Union[Unset, None, str]):
        is_optimal (Union[Unset, None, str]):
        is_optimal_isnull (Union[Unset, None, str]):
        metadata_accepted_distance (Union[Unset, None, str]):
        metadata_accepted_distance_gt (Union[Unset, None, str]):
        metadata_accepted_distance_gte (Union[Unset, None, str]):
        metadata_accepted_distance_lt (Union[Unset, None, str]):
        metadata_accepted_distance_lte (Union[Unset, None, str]):
        metadata_accepted_duration (Union[Unset, None, str]):
        metadata_accepted_duration_gt (Union[Unset, None, str]):
        metadata_accepted_duration_gte (Union[Unset, None, str]):
        metadata_accepted_duration_lt (Union[Unset, None, str]):
        metadata_accepted_duration_lte (Union[Unset, None, str]):
        metadata_active_distance (Union[Unset, None, str]):
        metadata_active_distance_gt (Union[Unset, None, str]):
        metadata_active_distance_gte (Union[Unset, None, str]):
        metadata_active_distance_lt (Union[Unset, None, str]):
        metadata_active_distance_lte (Union[Unset, None, str]):
        metadata_active_duration (Union[Unset, None, str]):
        metadata_active_duration_gt (Union[Unset, None, str]):
        metadata_active_duration_gte (Union[Unset, None, str]):
        metadata_active_duration_lt (Union[Unset, None, str]):
        metadata_active_duration_lte (Union[Unset, None, str]):
        metadata_assigned_distance (Union[Unset, None, str]):
        metadata_assigned_distance_gt (Union[Unset, None, str]):
        metadata_assigned_distance_gte (Union[Unset, None, str]):
        metadata_assigned_distance_lt (Union[Unset, None, str]):
        metadata_assigned_distance_lte (Union[Unset, None, str]):
        metadata_assigned_duration (Union[Unset, None, str]):
        metadata_assigned_duration_gt (Union[Unset, None, str]):
        metadata_assigned_duration_gte (Union[Unset, None, str]):
        metadata_assigned_duration_lt (Union[Unset, None, str]):
        metadata_assigned_duration_lte (Union[Unset, None, str]):
        metadata_cancelled_distance (Union[Unset, None, str]):
        metadata_cancelled_distance_gt (Union[Unset, None, str]):
        metadata_cancelled_distance_gte (Union[Unset, None, str]):
        metadata_cancelled_distance_lt (Union[Unset, None, str]):
        metadata_cancelled_distance_lte (Union[Unset, None, str]):
        metadata_cancelled_duration (Union[Unset, None, str]):
        metadata_cancelled_duration_gt (Union[Unset, None, str]):
        metadata_cancelled_duration_gte (Union[Unset, None, str]):
        metadata_cancelled_duration_lt (Union[Unset, None, str]):
        metadata_cancelled_duration_lte (Union[Unset, None, str]):
        metadata_completed_distance (Union[Unset, None, str]):
        metadata_completed_distance_gt (Union[Unset, None, str]):
        metadata_completed_distance_gte (Union[Unset, None, str]):
        metadata_completed_distance_lt (Union[Unset, None, str]):
        metadata_completed_distance_lte (Union[Unset, None, str]):
        metadata_completed_duration (Union[Unset, None, str]):
        metadata_completed_duration_gt (Union[Unset, None, str]):
        metadata_completed_duration_gte (Union[Unset, None, str]):
        metadata_completed_duration_lt (Union[Unset, None, str]):
        metadata_completed_duration_lte (Union[Unset, None, str]):
        metadata_documents_count (Union[Unset, None, str]):
        metadata_documents_count_gt (Union[Unset, None, str]):
        metadata_documents_count_gte (Union[Unset, None, str]):
        metadata_documents_count_lt (Union[Unset, None, str]):
        metadata_documents_count_lte (Union[Unset, None, str]):
        metadata_events_count (Union[Unset, None, str]):
        metadata_events_count_gt (Union[Unset, None, str]):
        metadata_events_count_gte (Union[Unset, None, str]):
        metadata_events_count_lt (Union[Unset, None, str]):
        metadata_events_count_lte (Union[Unset, None, str]):
        metadata_failed_distance (Union[Unset, None, str]):
        metadata_failed_distance_gt (Union[Unset, None, str]):
        metadata_failed_distance_gte (Union[Unset, None, str]):
        metadata_failed_distance_lt (Union[Unset, None, str]):
        metadata_failed_distance_lte (Union[Unset, None, str]):
        metadata_failed_duration (Union[Unset, None, str]):
        metadata_failed_duration_gt (Union[Unset, None, str]):
        metadata_failed_duration_gte (Union[Unset, None, str]):
        metadata_failed_duration_lt (Union[Unset, None, str]):
        metadata_failed_duration_lte (Union[Unset, None, str]):
        metadata_forms_completed_count (Union[Unset, None, str]):
        metadata_forms_completed_count_gt (Union[Unset, None, str]):
        metadata_forms_completed_count_gte (Union[Unset, None, str]):
        metadata_forms_completed_count_lt (Union[Unset, None, str]):
        metadata_forms_completed_count_lte (Union[Unset, None, str]):
        metadata_forms_count (Union[Unset, None, str]):
        metadata_forms_count_gt (Union[Unset, None, str]):
        metadata_forms_count_gte (Union[Unset, None, str]):
        metadata_forms_count_lt (Union[Unset, None, str]):
        metadata_forms_count_lte (Union[Unset, None, str]):
        metadata_signatures_count (Union[Unset, None, str]):
        metadata_signatures_count_gt (Union[Unset, None, str]):
        metadata_signatures_count_gte (Union[Unset, None, str]):
        metadata_signatures_count_lt (Union[Unset, None, str]):
        metadata_signatures_count_lte (Union[Unset, None, str]):
        metadata_task_event_notes_count (Union[Unset, None, str]):
        metadata_task_event_notes_count_gt (Union[Unset, None, str]):
        metadata_task_event_notes_count_gte (Union[Unset, None, str]):
        metadata_task_event_notes_count_lt (Union[Unset, None, str]):
        metadata_task_event_notes_count_lte (Union[Unset, None, str]):
        metadata_transit_distance (Union[Unset, None, str]):
        metadata_transit_distance_gt (Union[Unset, None, str]):
        metadata_transit_distance_gte (Union[Unset, None, str]):
        metadata_transit_distance_lt (Union[Unset, None, str]):
        metadata_transit_distance_lte (Union[Unset, None, str]):
        metadata_transit_duration (Union[Unset, None, str]):
        metadata_transit_duration_gt (Union[Unset, None, str]):
        metadata_transit_duration_gte (Union[Unset, None, str]):
        metadata_transit_duration_lt (Union[Unset, None, str]):
        metadata_transit_duration_lte (Union[Unset, None, str]):
        metadata_unassigned_distance (Union[Unset, None, str]):
        metadata_unassigned_distance_gt (Union[Unset, None, str]):
        metadata_unassigned_distance_gte (Union[Unset, None, str]):
        metadata_unassigned_distance_lt (Union[Unset, None, str]):
        metadata_unassigned_distance_lte (Union[Unset, None, str]):
        metadata_unassigned_duration (Union[Unset, None, str]):
        metadata_unassigned_duration_gt (Union[Unset, None, str]):
        metadata_unassigned_duration_gte (Union[Unset, None, str]):
        metadata_unassigned_duration_lt (Union[Unset, None, str]):
        metadata_unassigned_duration_lte (Union[Unset, None, str]):
        order_auto_assign (Union[Unset, None, str]):
        order_created_by (Union[Unset, None, str]):
        order_created_by_in (Union[Unset, None, str]):
        order_created_by_isnull (Union[Unset, None, str]):
        order_external_id (Union[Unset, None, str]):
        order_external_id_icontains (Union[Unset, None, str]):
        order_external_id_in (Union[Unset, None, str]):
        order_external_id_iregex (Union[Unset, None, str]):
        order_external_id_isnull (Union[Unset, None, str]):
        order_external_id_istartswith (Union[Unset, None, str]):
        order_external_id_search (Union[Unset, None, str]):
        order_reference (Union[Unset, None, str]):
        order_reference_icontains (Union[Unset, None, str]):
        order_reference_in (Union[Unset, None, str]):
        order_reference_iregex (Union[Unset, None, str]):
        order_reference_istartswith (Union[Unset, None, str]):
        order_reference_search (Union[Unset, None, str]):
        order_id (Union[Unset, None, str]):
        order_id_in (Union[Unset, None, str]):
        order_id_isnull (Union[Unset, None, str]):
        orderer_id (Union[Unset, None, str]):
        orderer_id_in (Union[Unset, None, str]):
        orderer_id_isnull (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        owner_id (Union[Unset, None, str]):
        owner_id_in (Union[Unset, None, str]):
        owner_id_isnull (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        priority (Union[Unset, None, str]):
        priority_gt (Union[Unset, None, str]):
        priority_gte (Union[Unset, None, str]):
        priority_in (Union[Unset, None, str]):
        priority_lt (Union[Unset, None, str]):
        priority_lte (Union[Unset, None, str]):
        receiver_id (Union[Unset, None, str]):
        receiver_id_in (Union[Unset, None, str]):
        receiver_id_isnull (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        reference_icontains (Union[Unset, None, str]):
        reference_in (Union[Unset, None, str]):
        reference_iregex (Union[Unset, None, str]):
        reference_istartswith (Union[Unset, None, str]):
        reference_search (Union[Unset, None, str]):
        route_id (Union[Unset, None, str]):
        route_id_in (Union[Unset, None, str]):
        route_id_isnull (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, TaskExportsListState]):
        state_in (Union[Unset, None, str]):
        unassignee_id (Union[Unset, None, str]):
        unassignee_id_in (Union[Unset, None, str]):
        unassignee_id_isnull (Union[Unset, None, str]):

    Returns:
        Response[List[TaskExport]]
    """

    return sync_detailed(
        client=client,
        address_apartment_number=address_apartment_number,
        address_apartment_number_icontains=address_apartment_number_icontains,
        address_apartment_number_in=address_apartment_number_in,
        address_apartment_number_iregex=address_apartment_number_iregex,
        address_apartment_number_istartswith=address_apartment_number_istartswith,
        address_apartment_number_search=address_apartment_number_search,
        address_city=address_city,
        address_city_icontains=address_city_icontains,
        address_city_in=address_city_in,
        address_city_iregex=address_city_iregex,
        address_city_istartswith=address_city_istartswith,
        address_city_search=address_city_search,
        address_country=address_country,
        address_country_icontains=address_country_icontains,
        address_country_in=address_country_in,
        address_country_iregex=address_country_iregex,
        address_country_istartswith=address_country_istartswith,
        address_country_search=address_country_search,
        address_country_code=address_country_code,
        address_country_code_icontains=address_country_code_icontains,
        address_country_code_in=address_country_code_in,
        address_country_code_iregex=address_country_code_iregex,
        address_country_code_istartswith=address_country_code_istartswith,
        address_country_code_search=address_country_code_search,
        address_formatted_address=address_formatted_address,
        address_formatted_address_icontains=address_formatted_address_icontains,
        address_formatted_address_in=address_formatted_address_in,
        address_formatted_address_iregex=address_formatted_address_iregex,
        address_formatted_address_istartswith=address_formatted_address_istartswith,
        address_formatted_address_search=address_formatted_address_search,
        address_google_place_id=address_google_place_id,
        address_google_place_id_icontains=address_google_place_id_icontains,
        address_google_place_id_in=address_google_place_id_in,
        address_google_place_id_iregex=address_google_place_id_iregex,
        address_google_place_id_istartswith=address_google_place_id_istartswith,
        address_google_place_id_search=address_google_place_id_search,
        address_house_number=address_house_number,
        address_house_number_icontains=address_house_number_icontains,
        address_house_number_in=address_house_number_in,
        address_house_number_iregex=address_house_number_iregex,
        address_house_number_istartswith=address_house_number_istartswith,
        address_house_number_search=address_house_number_search,
        address_point_of_interest=address_point_of_interest,
        address_point_of_interest_icontains=address_point_of_interest_icontains,
        address_point_of_interest_in=address_point_of_interest_in,
        address_point_of_interest_iregex=address_point_of_interest_iregex,
        address_point_of_interest_istartswith=address_point_of_interest_istartswith,
        address_point_of_interest_search=address_point_of_interest_search,
        address_postal_code=address_postal_code,
        address_postal_code_icontains=address_postal_code_icontains,
        address_postal_code_in=address_postal_code_in,
        address_postal_code_iregex=address_postal_code_iregex,
        address_postal_code_istartswith=address_postal_code_istartswith,
        address_postal_code_search=address_postal_code_search,
        address_raw_address=address_raw_address,
        address_raw_address_icontains=address_raw_address_icontains,
        address_raw_address_in=address_raw_address_in,
        address_raw_address_iregex=address_raw_address_iregex,
        address_raw_address_istartswith=address_raw_address_istartswith,
        address_raw_address_search=address_raw_address_search,
        address_state=address_state,
        address_state_icontains=address_state_icontains,
        address_state_in=address_state_in,
        address_state_iregex=address_state_iregex,
        address_state_istartswith=address_state_istartswith,
        address_state_search=address_state_search,
        address_street=address_street,
        address_street_icontains=address_street_icontains,
        address_street_in=address_street_in,
        address_street_iregex=address_street_iregex,
        address_street_istartswith=address_street_istartswith,
        address_street_search=address_street_search,
        address_id=address_id,
        address_id_in=address_id_in,
        address_id_isnull=address_id_isnull,
        assignee_email=assignee_email,
        assignee_email_icontains=assignee_email_icontains,
        assignee_email_iregex=assignee_email_iregex,
        assignee_email_isnull=assignee_email_isnull,
        assignee_email_istartswith=assignee_email_istartswith,
        assignee_email_search=assignee_email_search,
        assignee_first_name=assignee_first_name,
        assignee_first_name_icontains=assignee_first_name_icontains,
        assignee_first_name_iregex=assignee_first_name_iregex,
        assignee_first_name_isnull=assignee_first_name_isnull,
        assignee_first_name_istartswith=assignee_first_name_istartswith,
        assignee_first_name_search=assignee_first_name_search,
        assignee_last_name=assignee_last_name,
        assignee_last_name_icontains=assignee_last_name_icontains,
        assignee_last_name_iregex=assignee_last_name_iregex,
        assignee_last_name_isnull=assignee_last_name_isnull,
        assignee_last_name_istartswith=assignee_last_name_istartswith,
        assignee_last_name_search=assignee_last_name_search,
        assignee_phone=assignee_phone,
        assignee_phone_icontains=assignee_phone_icontains,
        assignee_phone_iregex=assignee_phone_iregex,
        assignee_phone_isnull=assignee_phone_isnull,
        assignee_phone_istartswith=assignee_phone_istartswith,
        assignee_phone_search=assignee_phone_search,
        assignee_id=assignee_id,
        assignee_id_in=assignee_id_in,
        assignee_id_isnull=assignee_id_isnull,
        assignee_proximity=assignee_proximity,
        assignee_proximity_in=assignee_proximity_in,
        category=category,
        category_in=category_in,
        contact_company_icontains=contact_company_icontains,
        contact_company_in=contact_company_in,
        contact_company_iregex=contact_company_iregex,
        contact_company_istartswith=contact_company_istartswith,
        contact_company_search=contact_company_search,
        contact_email=contact_email,
        contact_email_icontains=contact_email_icontains,
        contact_email_in=contact_email_in,
        contact_email_iregex=contact_email_iregex,
        contact_email_istartswith=contact_email_istartswith,
        contact_email_search=contact_email_search,
        contact_name=contact_name,
        contact_name_icontains=contact_name_icontains,
        contact_name_in=contact_name_in,
        contact_name_iregex=contact_name_iregex,
        contact_name_istartswith=contact_name_istartswith,
        contact_name_search=contact_name_search,
        contact_notes=contact_notes,
        contact_notes_icontains=contact_notes_icontains,
        contact_notes_in=contact_notes_in,
        contact_notes_iregex=contact_notes_iregex,
        contact_notes_istartswith=contact_notes_istartswith,
        contact_notes_search=contact_notes_search,
        contact_phone=contact_phone,
        contact_phone_icontains=contact_phone_icontains,
        contact_phone_in=contact_phone_in,
        contact_phone_iregex=contact_phone_iregex,
        contact_phone_istartswith=contact_phone_istartswith,
        contact_phone_search=contact_phone_search,
        contact_id=contact_id,
        contact_id_in=contact_id_in,
        contact_id_isnull=contact_id_isnull,
        created_by=created_by,
        created_by_in=created_by_in,
        created_by_isnull=created_by_isnull,
        description=description,
        description_icontains=description_icontains,
        description_iregex=description_iregex,
        description_istartswith=description_istartswith,
        description_search=description_search,
        duration=duration,
        duration_gt=duration_gt,
        duration_gte=duration_gte,
        duration_lt=duration_lt,
        duration_lte=duration_lte,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        external_id_in=external_id_in,
        external_id_iregex=external_id_iregex,
        external_id_isnull=external_id_isnull,
        external_id_istartswith=external_id_istartswith,
        external_id_search=external_id_search,
        fields=fields,
        format_=format_,
        id=id,
        id_in=id_in,
        is_optimal=is_optimal,
        is_optimal_isnull=is_optimal_isnull,
        metadata_accepted_distance=metadata_accepted_distance,
        metadata_accepted_distance_gt=metadata_accepted_distance_gt,
        metadata_accepted_distance_gte=metadata_accepted_distance_gte,
        metadata_accepted_distance_lt=metadata_accepted_distance_lt,
        metadata_accepted_distance_lte=metadata_accepted_distance_lte,
        metadata_accepted_duration=metadata_accepted_duration,
        metadata_accepted_duration_gt=metadata_accepted_duration_gt,
        metadata_accepted_duration_gte=metadata_accepted_duration_gte,
        metadata_accepted_duration_lt=metadata_accepted_duration_lt,
        metadata_accepted_duration_lte=metadata_accepted_duration_lte,
        metadata_active_distance=metadata_active_distance,
        metadata_active_distance_gt=metadata_active_distance_gt,
        metadata_active_distance_gte=metadata_active_distance_gte,
        metadata_active_distance_lt=metadata_active_distance_lt,
        metadata_active_distance_lte=metadata_active_distance_lte,
        metadata_active_duration=metadata_active_duration,
        metadata_active_duration_gt=metadata_active_duration_gt,
        metadata_active_duration_gte=metadata_active_duration_gte,
        metadata_active_duration_lt=metadata_active_duration_lt,
        metadata_active_duration_lte=metadata_active_duration_lte,
        metadata_assigned_distance=metadata_assigned_distance,
        metadata_assigned_distance_gt=metadata_assigned_distance_gt,
        metadata_assigned_distance_gte=metadata_assigned_distance_gte,
        metadata_assigned_distance_lt=metadata_assigned_distance_lt,
        metadata_assigned_distance_lte=metadata_assigned_distance_lte,
        metadata_assigned_duration=metadata_assigned_duration,
        metadata_assigned_duration_gt=metadata_assigned_duration_gt,
        metadata_assigned_duration_gte=metadata_assigned_duration_gte,
        metadata_assigned_duration_lt=metadata_assigned_duration_lt,
        metadata_assigned_duration_lte=metadata_assigned_duration_lte,
        metadata_cancelled_distance=metadata_cancelled_distance,
        metadata_cancelled_distance_gt=metadata_cancelled_distance_gt,
        metadata_cancelled_distance_gte=metadata_cancelled_distance_gte,
        metadata_cancelled_distance_lt=metadata_cancelled_distance_lt,
        metadata_cancelled_distance_lte=metadata_cancelled_distance_lte,
        metadata_cancelled_duration=metadata_cancelled_duration,
        metadata_cancelled_duration_gt=metadata_cancelled_duration_gt,
        metadata_cancelled_duration_gte=metadata_cancelled_duration_gte,
        metadata_cancelled_duration_lt=metadata_cancelled_duration_lt,
        metadata_cancelled_duration_lte=metadata_cancelled_duration_lte,
        metadata_completed_distance=metadata_completed_distance,
        metadata_completed_distance_gt=metadata_completed_distance_gt,
        metadata_completed_distance_gte=metadata_completed_distance_gte,
        metadata_completed_distance_lt=metadata_completed_distance_lt,
        metadata_completed_distance_lte=metadata_completed_distance_lte,
        metadata_completed_duration=metadata_completed_duration,
        metadata_completed_duration_gt=metadata_completed_duration_gt,
        metadata_completed_duration_gte=metadata_completed_duration_gte,
        metadata_completed_duration_lt=metadata_completed_duration_lt,
        metadata_completed_duration_lte=metadata_completed_duration_lte,
        metadata_documents_count=metadata_documents_count,
        metadata_documents_count_gt=metadata_documents_count_gt,
        metadata_documents_count_gte=metadata_documents_count_gte,
        metadata_documents_count_lt=metadata_documents_count_lt,
        metadata_documents_count_lte=metadata_documents_count_lte,
        metadata_events_count=metadata_events_count,
        metadata_events_count_gt=metadata_events_count_gt,
        metadata_events_count_gte=metadata_events_count_gte,
        metadata_events_count_lt=metadata_events_count_lt,
        metadata_events_count_lte=metadata_events_count_lte,
        metadata_failed_distance=metadata_failed_distance,
        metadata_failed_distance_gt=metadata_failed_distance_gt,
        metadata_failed_distance_gte=metadata_failed_distance_gte,
        metadata_failed_distance_lt=metadata_failed_distance_lt,
        metadata_failed_distance_lte=metadata_failed_distance_lte,
        metadata_failed_duration=metadata_failed_duration,
        metadata_failed_duration_gt=metadata_failed_duration_gt,
        metadata_failed_duration_gte=metadata_failed_duration_gte,
        metadata_failed_duration_lt=metadata_failed_duration_lt,
        metadata_failed_duration_lte=metadata_failed_duration_lte,
        metadata_forms_completed_count=metadata_forms_completed_count,
        metadata_forms_completed_count_gt=metadata_forms_completed_count_gt,
        metadata_forms_completed_count_gte=metadata_forms_completed_count_gte,
        metadata_forms_completed_count_lt=metadata_forms_completed_count_lt,
        metadata_forms_completed_count_lte=metadata_forms_completed_count_lte,
        metadata_forms_count=metadata_forms_count,
        metadata_forms_count_gt=metadata_forms_count_gt,
        metadata_forms_count_gte=metadata_forms_count_gte,
        metadata_forms_count_lt=metadata_forms_count_lt,
        metadata_forms_count_lte=metadata_forms_count_lte,
        metadata_signatures_count=metadata_signatures_count,
        metadata_signatures_count_gt=metadata_signatures_count_gt,
        metadata_signatures_count_gte=metadata_signatures_count_gte,
        metadata_signatures_count_lt=metadata_signatures_count_lt,
        metadata_signatures_count_lte=metadata_signatures_count_lte,
        metadata_task_event_notes_count=metadata_task_event_notes_count,
        metadata_task_event_notes_count_gt=metadata_task_event_notes_count_gt,
        metadata_task_event_notes_count_gte=metadata_task_event_notes_count_gte,
        metadata_task_event_notes_count_lt=metadata_task_event_notes_count_lt,
        metadata_task_event_notes_count_lte=metadata_task_event_notes_count_lte,
        metadata_transit_distance=metadata_transit_distance,
        metadata_transit_distance_gt=metadata_transit_distance_gt,
        metadata_transit_distance_gte=metadata_transit_distance_gte,
        metadata_transit_distance_lt=metadata_transit_distance_lt,
        metadata_transit_distance_lte=metadata_transit_distance_lte,
        metadata_transit_duration=metadata_transit_duration,
        metadata_transit_duration_gt=metadata_transit_duration_gt,
        metadata_transit_duration_gte=metadata_transit_duration_gte,
        metadata_transit_duration_lt=metadata_transit_duration_lt,
        metadata_transit_duration_lte=metadata_transit_duration_lte,
        metadata_unassigned_distance=metadata_unassigned_distance,
        metadata_unassigned_distance_gt=metadata_unassigned_distance_gt,
        metadata_unassigned_distance_gte=metadata_unassigned_distance_gte,
        metadata_unassigned_distance_lt=metadata_unassigned_distance_lt,
        metadata_unassigned_distance_lte=metadata_unassigned_distance_lte,
        metadata_unassigned_duration=metadata_unassigned_duration,
        metadata_unassigned_duration_gt=metadata_unassigned_duration_gt,
        metadata_unassigned_duration_gte=metadata_unassigned_duration_gte,
        metadata_unassigned_duration_lt=metadata_unassigned_duration_lt,
        metadata_unassigned_duration_lte=metadata_unassigned_duration_lte,
        order_auto_assign=order_auto_assign,
        order_created_by=order_created_by,
        order_created_by_in=order_created_by_in,
        order_created_by_isnull=order_created_by_isnull,
        order_external_id=order_external_id,
        order_external_id_icontains=order_external_id_icontains,
        order_external_id_in=order_external_id_in,
        order_external_id_iregex=order_external_id_iregex,
        order_external_id_isnull=order_external_id_isnull,
        order_external_id_istartswith=order_external_id_istartswith,
        order_external_id_search=order_external_id_search,
        order_reference=order_reference,
        order_reference_icontains=order_reference_icontains,
        order_reference_in=order_reference_in,
        order_reference_iregex=order_reference_iregex,
        order_reference_istartswith=order_reference_istartswith,
        order_reference_search=order_reference_search,
        order_id=order_id,
        order_id_in=order_id_in,
        order_id_isnull=order_id_isnull,
        orderer_id=orderer_id,
        orderer_id_in=orderer_id_in,
        orderer_id_isnull=orderer_id_isnull,
        ordering=ordering,
        owner_id=owner_id,
        owner_id_in=owner_id_in,
        owner_id_isnull=owner_id_isnull,
        page=page,
        page_size=page_size,
        priority=priority,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_in=priority_in,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        receiver_id=receiver_id,
        receiver_id_in=receiver_id_in,
        receiver_id_isnull=receiver_id_isnull,
        reference=reference,
        reference_icontains=reference_icontains,
        reference_in=reference_in,
        reference_iregex=reference_iregex,
        reference_istartswith=reference_istartswith,
        reference_search=reference_search,
        route_id=route_id,
        route_id_in=route_id_in,
        route_id_isnull=route_id_isnull,
        search=search,
        state=state,
        state_in=state_in,
        unassignee_id=unassignee_id,
        unassignee_id_in=unassignee_id_in,
        unassignee_id_isnull=unassignee_id_isnull,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    address_apartment_number: Union[Unset, None, str] = UNSET,
    address_apartment_number_icontains: Union[Unset, None, str] = UNSET,
    address_apartment_number_in: Union[Unset, None, str] = UNSET,
    address_apartment_number_iregex: Union[Unset, None, str] = UNSET,
    address_apartment_number_istartswith: Union[Unset, None, str] = UNSET,
    address_apartment_number_search: Union[Unset, None, str] = UNSET,
    address_city: Union[Unset, None, str] = UNSET,
    address_city_icontains: Union[Unset, None, str] = UNSET,
    address_city_in: Union[Unset, None, str] = UNSET,
    address_city_iregex: Union[Unset, None, str] = UNSET,
    address_city_istartswith: Union[Unset, None, str] = UNSET,
    address_city_search: Union[Unset, None, str] = UNSET,
    address_country: Union[Unset, None, str] = UNSET,
    address_country_icontains: Union[Unset, None, str] = UNSET,
    address_country_in: Union[Unset, None, str] = UNSET,
    address_country_iregex: Union[Unset, None, str] = UNSET,
    address_country_istartswith: Union[Unset, None, str] = UNSET,
    address_country_search: Union[Unset, None, str] = UNSET,
    address_country_code: Union[Unset, None, str] = UNSET,
    address_country_code_icontains: Union[Unset, None, str] = UNSET,
    address_country_code_in: Union[Unset, None, str] = UNSET,
    address_country_code_iregex: Union[Unset, None, str] = UNSET,
    address_country_code_istartswith: Union[Unset, None, str] = UNSET,
    address_country_code_search: Union[Unset, None, str] = UNSET,
    address_formatted_address: Union[Unset, None, str] = UNSET,
    address_formatted_address_icontains: Union[Unset, None, str] = UNSET,
    address_formatted_address_in: Union[Unset, None, str] = UNSET,
    address_formatted_address_iregex: Union[Unset, None, str] = UNSET,
    address_formatted_address_istartswith: Union[Unset, None, str] = UNSET,
    address_formatted_address_search: Union[Unset, None, str] = UNSET,
    address_google_place_id: Union[Unset, None, str] = UNSET,
    address_google_place_id_icontains: Union[Unset, None, str] = UNSET,
    address_google_place_id_in: Union[Unset, None, str] = UNSET,
    address_google_place_id_iregex: Union[Unset, None, str] = UNSET,
    address_google_place_id_istartswith: Union[Unset, None, str] = UNSET,
    address_google_place_id_search: Union[Unset, None, str] = UNSET,
    address_house_number: Union[Unset, None, str] = UNSET,
    address_house_number_icontains: Union[Unset, None, str] = UNSET,
    address_house_number_in: Union[Unset, None, str] = UNSET,
    address_house_number_iregex: Union[Unset, None, str] = UNSET,
    address_house_number_istartswith: Union[Unset, None, str] = UNSET,
    address_house_number_search: Union[Unset, None, str] = UNSET,
    address_point_of_interest: Union[Unset, None, str] = UNSET,
    address_point_of_interest_icontains: Union[Unset, None, str] = UNSET,
    address_point_of_interest_in: Union[Unset, None, str] = UNSET,
    address_point_of_interest_iregex: Union[Unset, None, str] = UNSET,
    address_point_of_interest_istartswith: Union[Unset, None, str] = UNSET,
    address_point_of_interest_search: Union[Unset, None, str] = UNSET,
    address_postal_code: Union[Unset, None, str] = UNSET,
    address_postal_code_icontains: Union[Unset, None, str] = UNSET,
    address_postal_code_in: Union[Unset, None, str] = UNSET,
    address_postal_code_iregex: Union[Unset, None, str] = UNSET,
    address_postal_code_istartswith: Union[Unset, None, str] = UNSET,
    address_postal_code_search: Union[Unset, None, str] = UNSET,
    address_raw_address: Union[Unset, None, str] = UNSET,
    address_raw_address_icontains: Union[Unset, None, str] = UNSET,
    address_raw_address_in: Union[Unset, None, str] = UNSET,
    address_raw_address_iregex: Union[Unset, None, str] = UNSET,
    address_raw_address_istartswith: Union[Unset, None, str] = UNSET,
    address_raw_address_search: Union[Unset, None, str] = UNSET,
    address_state: Union[Unset, None, str] = UNSET,
    address_state_icontains: Union[Unset, None, str] = UNSET,
    address_state_in: Union[Unset, None, str] = UNSET,
    address_state_iregex: Union[Unset, None, str] = UNSET,
    address_state_istartswith: Union[Unset, None, str] = UNSET,
    address_state_search: Union[Unset, None, str] = UNSET,
    address_street: Union[Unset, None, str] = UNSET,
    address_street_icontains: Union[Unset, None, str] = UNSET,
    address_street_in: Union[Unset, None, str] = UNSET,
    address_street_iregex: Union[Unset, None, str] = UNSET,
    address_street_istartswith: Union[Unset, None, str] = UNSET,
    address_street_search: Union[Unset, None, str] = UNSET,
    address_id: Union[Unset, None, str] = UNSET,
    address_id_in: Union[Unset, None, str] = UNSET,
    address_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_email: Union[Unset, None, str] = UNSET,
    assignee_email_icontains: Union[Unset, None, str] = UNSET,
    assignee_email_iregex: Union[Unset, None, str] = UNSET,
    assignee_email_isnull: Union[Unset, None, str] = UNSET,
    assignee_email_istartswith: Union[Unset, None, str] = UNSET,
    assignee_email_search: Union[Unset, None, str] = UNSET,
    assignee_first_name: Union[Unset, None, str] = UNSET,
    assignee_first_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_first_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_first_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_first_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_first_name_search: Union[Unset, None, str] = UNSET,
    assignee_last_name: Union[Unset, None, str] = UNSET,
    assignee_last_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_last_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_last_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_last_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_last_name_search: Union[Unset, None, str] = UNSET,
    assignee_phone: Union[Unset, None, str] = UNSET,
    assignee_phone_icontains: Union[Unset, None, str] = UNSET,
    assignee_phone_iregex: Union[Unset, None, str] = UNSET,
    assignee_phone_isnull: Union[Unset, None, str] = UNSET,
    assignee_phone_istartswith: Union[Unset, None, str] = UNSET,
    assignee_phone_search: Union[Unset, None, str] = UNSET,
    assignee_id: Union[Unset, None, str] = UNSET,
    assignee_id_in: Union[Unset, None, str] = UNSET,
    assignee_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_proximity: Union[Unset, None, TaskExportsListAssigneeProximity] = UNSET,
    assignee_proximity_in: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskExportsListCategory] = UNSET,
    category_in: Union[Unset, None, str] = UNSET,
    contact_company_icontains: Union[Unset, None, str] = UNSET,
    contact_company_in: Union[Unset, None, str] = UNSET,
    contact_company_iregex: Union[Unset, None, str] = UNSET,
    contact_company_istartswith: Union[Unset, None, str] = UNSET,
    contact_company_search: Union[Unset, None, str] = UNSET,
    contact_email: Union[Unset, None, str] = UNSET,
    contact_email_icontains: Union[Unset, None, str] = UNSET,
    contact_email_in: Union[Unset, None, str] = UNSET,
    contact_email_iregex: Union[Unset, None, str] = UNSET,
    contact_email_istartswith: Union[Unset, None, str] = UNSET,
    contact_email_search: Union[Unset, None, str] = UNSET,
    contact_name: Union[Unset, None, str] = UNSET,
    contact_name_icontains: Union[Unset, None, str] = UNSET,
    contact_name_in: Union[Unset, None, str] = UNSET,
    contact_name_iregex: Union[Unset, None, str] = UNSET,
    contact_name_istartswith: Union[Unset, None, str] = UNSET,
    contact_name_search: Union[Unset, None, str] = UNSET,
    contact_notes: Union[Unset, None, str] = UNSET,
    contact_notes_icontains: Union[Unset, None, str] = UNSET,
    contact_notes_in: Union[Unset, None, str] = UNSET,
    contact_notes_iregex: Union[Unset, None, str] = UNSET,
    contact_notes_istartswith: Union[Unset, None, str] = UNSET,
    contact_notes_search: Union[Unset, None, str] = UNSET,
    contact_phone: Union[Unset, None, str] = UNSET,
    contact_phone_icontains: Union[Unset, None, str] = UNSET,
    contact_phone_in: Union[Unset, None, str] = UNSET,
    contact_phone_iregex: Union[Unset, None, str] = UNSET,
    contact_phone_istartswith: Union[Unset, None, str] = UNSET,
    contact_phone_search: Union[Unset, None, str] = UNSET,
    contact_id: Union[Unset, None, str] = UNSET,
    contact_id_in: Union[Unset, None, str] = UNSET,
    contact_id_isnull: Union[Unset, None, str] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    created_by_in: Union[Unset, None, str] = UNSET,
    created_by_isnull: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    description_icontains: Union[Unset, None, str] = UNSET,
    description_iregex: Union[Unset, None, str] = UNSET,
    description_istartswith: Union[Unset, None, str] = UNSET,
    description_search: Union[Unset, None, str] = UNSET,
    duration: Union[Unset, None, str] = UNSET,
    duration_gt: Union[Unset, None, str] = UNSET,
    duration_gte: Union[Unset, None, str] = UNSET,
    duration_lt: Union[Unset, None, str] = UNSET,
    duration_lte: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    external_id_in: Union[Unset, None, str] = UNSET,
    external_id_iregex: Union[Unset, None, str] = UNSET,
    external_id_isnull: Union[Unset, None, str] = UNSET,
    external_id_istartswith: Union[Unset, None, str] = UNSET,
    external_id_search: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, TaskExportsListFormat] = TaskExportsListFormat.JSON,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    is_optimal: Union[Unset, None, str] = UNSET,
    is_optimal_isnull: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_active_distance: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_active_duration: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_documents_count: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gte: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lte: Union[Unset, None, str] = UNSET,
    metadata_events_count: Union[Unset, None, str] = UNSET,
    metadata_events_count_gt: Union[Unset, None, str] = UNSET,
    metadata_events_count_gte: Union[Unset, None, str] = UNSET,
    metadata_events_count_lt: Union[Unset, None, str] = UNSET,
    metadata_events_count_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_count: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lte: Union[Unset, None, str] = UNSET,
    order_auto_assign: Union[Unset, None, str] = UNSET,
    order_created_by: Union[Unset, None, str] = UNSET,
    order_created_by_in: Union[Unset, None, str] = UNSET,
    order_created_by_isnull: Union[Unset, None, str] = UNSET,
    order_external_id: Union[Unset, None, str] = UNSET,
    order_external_id_icontains: Union[Unset, None, str] = UNSET,
    order_external_id_in: Union[Unset, None, str] = UNSET,
    order_external_id_iregex: Union[Unset, None, str] = UNSET,
    order_external_id_isnull: Union[Unset, None, str] = UNSET,
    order_external_id_istartswith: Union[Unset, None, str] = UNSET,
    order_external_id_search: Union[Unset, None, str] = UNSET,
    order_reference: Union[Unset, None, str] = UNSET,
    order_reference_icontains: Union[Unset, None, str] = UNSET,
    order_reference_in: Union[Unset, None, str] = UNSET,
    order_reference_iregex: Union[Unset, None, str] = UNSET,
    order_reference_istartswith: Union[Unset, None, str] = UNSET,
    order_reference_search: Union[Unset, None, str] = UNSET,
    order_id: Union[Unset, None, str] = UNSET,
    order_id_in: Union[Unset, None, str] = UNSET,
    order_id_isnull: Union[Unset, None, str] = UNSET,
    orderer_id: Union[Unset, None, str] = UNSET,
    orderer_id_in: Union[Unset, None, str] = UNSET,
    orderer_id_isnull: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    owner_id: Union[Unset, None, str] = UNSET,
    owner_id_in: Union[Unset, None, str] = UNSET,
    owner_id_isnull: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    priority_gt: Union[Unset, None, str] = UNSET,
    priority_gte: Union[Unset, None, str] = UNSET,
    priority_in: Union[Unset, None, str] = UNSET,
    priority_lt: Union[Unset, None, str] = UNSET,
    priority_lte: Union[Unset, None, str] = UNSET,
    receiver_id: Union[Unset, None, str] = UNSET,
    receiver_id_in: Union[Unset, None, str] = UNSET,
    receiver_id_isnull: Union[Unset, None, str] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    reference_icontains: Union[Unset, None, str] = UNSET,
    reference_in: Union[Unset, None, str] = UNSET,
    reference_iregex: Union[Unset, None, str] = UNSET,
    reference_istartswith: Union[Unset, None, str] = UNSET,
    reference_search: Union[Unset, None, str] = UNSET,
    route_id: Union[Unset, None, str] = UNSET,
    route_id_in: Union[Unset, None, str] = UNSET,
    route_id_isnull: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, TaskExportsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    unassignee_id: Union[Unset, None, str] = UNSET,
    unassignee_id_in: Union[Unset, None, str] = UNSET,
    unassignee_id_isnull: Union[Unset, None, str] = UNSET,
) -> Response[List[TaskExport]]:
    """This view has multiple renderer classes available: `json` and `xlsx`. In order to export the data as
    an excel file, just set query argument `format` to `xlsx`.When downloading `xlsx` format, use Accept
    header `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; version=...`

    The user can request what fields and in what order will be rendered using query argument `fields`.
    This is a comma separated list of field names used in the API. Available fields are visible in the
    example.
    Also metafields can be added to the response. For this just add them as fields, using structure
    `metafields__{metafield.namespace}__{metafield.key}`.

    When exporting to **excel**, the column names may be changed based on account metafield names or
    pre-defined field name and width mapping.

    Changes in version 2.2.1:
     * field names have been updated to reflect the Task fields schema and filters.
     * Invalid fields in fields request will return a ValidationError.
     * Account filter is required.
     * AccountRole display name is annotated to user objects.
     * 'task_event_notes' is dropped.
     * 'contact_phone' and 'contact_email' is replaced with 'contact_phones' and 'contact_emails'.

    Args:
        address_apartment_number (Union[Unset, None, str]):
        address_apartment_number_icontains (Union[Unset, None, str]):
        address_apartment_number_in (Union[Unset, None, str]):
        address_apartment_number_iregex (Union[Unset, None, str]):
        address_apartment_number_istartswith (Union[Unset, None, str]):
        address_apartment_number_search (Union[Unset, None, str]):
        address_city (Union[Unset, None, str]):
        address_city_icontains (Union[Unset, None, str]):
        address_city_in (Union[Unset, None, str]):
        address_city_iregex (Union[Unset, None, str]):
        address_city_istartswith (Union[Unset, None, str]):
        address_city_search (Union[Unset, None, str]):
        address_country (Union[Unset, None, str]):
        address_country_icontains (Union[Unset, None, str]):
        address_country_in (Union[Unset, None, str]):
        address_country_iregex (Union[Unset, None, str]):
        address_country_istartswith (Union[Unset, None, str]):
        address_country_search (Union[Unset, None, str]):
        address_country_code (Union[Unset, None, str]):
        address_country_code_icontains (Union[Unset, None, str]):
        address_country_code_in (Union[Unset, None, str]):
        address_country_code_iregex (Union[Unset, None, str]):
        address_country_code_istartswith (Union[Unset, None, str]):
        address_country_code_search (Union[Unset, None, str]):
        address_formatted_address (Union[Unset, None, str]):
        address_formatted_address_icontains (Union[Unset, None, str]):
        address_formatted_address_in (Union[Unset, None, str]):
        address_formatted_address_iregex (Union[Unset, None, str]):
        address_formatted_address_istartswith (Union[Unset, None, str]):
        address_formatted_address_search (Union[Unset, None, str]):
        address_google_place_id (Union[Unset, None, str]):
        address_google_place_id_icontains (Union[Unset, None, str]):
        address_google_place_id_in (Union[Unset, None, str]):
        address_google_place_id_iregex (Union[Unset, None, str]):
        address_google_place_id_istartswith (Union[Unset, None, str]):
        address_google_place_id_search (Union[Unset, None, str]):
        address_house_number (Union[Unset, None, str]):
        address_house_number_icontains (Union[Unset, None, str]):
        address_house_number_in (Union[Unset, None, str]):
        address_house_number_iregex (Union[Unset, None, str]):
        address_house_number_istartswith (Union[Unset, None, str]):
        address_house_number_search (Union[Unset, None, str]):
        address_point_of_interest (Union[Unset, None, str]):
        address_point_of_interest_icontains (Union[Unset, None, str]):
        address_point_of_interest_in (Union[Unset, None, str]):
        address_point_of_interest_iregex (Union[Unset, None, str]):
        address_point_of_interest_istartswith (Union[Unset, None, str]):
        address_point_of_interest_search (Union[Unset, None, str]):
        address_postal_code (Union[Unset, None, str]):
        address_postal_code_icontains (Union[Unset, None, str]):
        address_postal_code_in (Union[Unset, None, str]):
        address_postal_code_iregex (Union[Unset, None, str]):
        address_postal_code_istartswith (Union[Unset, None, str]):
        address_postal_code_search (Union[Unset, None, str]):
        address_raw_address (Union[Unset, None, str]):
        address_raw_address_icontains (Union[Unset, None, str]):
        address_raw_address_in (Union[Unset, None, str]):
        address_raw_address_iregex (Union[Unset, None, str]):
        address_raw_address_istartswith (Union[Unset, None, str]):
        address_raw_address_search (Union[Unset, None, str]):
        address_state (Union[Unset, None, str]):
        address_state_icontains (Union[Unset, None, str]):
        address_state_in (Union[Unset, None, str]):
        address_state_iregex (Union[Unset, None, str]):
        address_state_istartswith (Union[Unset, None, str]):
        address_state_search (Union[Unset, None, str]):
        address_street (Union[Unset, None, str]):
        address_street_icontains (Union[Unset, None, str]):
        address_street_in (Union[Unset, None, str]):
        address_street_iregex (Union[Unset, None, str]):
        address_street_istartswith (Union[Unset, None, str]):
        address_street_search (Union[Unset, None, str]):
        address_id (Union[Unset, None, str]):
        address_id_in (Union[Unset, None, str]):
        address_id_isnull (Union[Unset, None, str]):
        assignee_email (Union[Unset, None, str]):
        assignee_email_icontains (Union[Unset, None, str]):
        assignee_email_iregex (Union[Unset, None, str]):
        assignee_email_isnull (Union[Unset, None, str]):
        assignee_email_istartswith (Union[Unset, None, str]):
        assignee_email_search (Union[Unset, None, str]):
        assignee_first_name (Union[Unset, None, str]):
        assignee_first_name_icontains (Union[Unset, None, str]):
        assignee_first_name_iregex (Union[Unset, None, str]):
        assignee_first_name_isnull (Union[Unset, None, str]):
        assignee_first_name_istartswith (Union[Unset, None, str]):
        assignee_first_name_search (Union[Unset, None, str]):
        assignee_last_name (Union[Unset, None, str]):
        assignee_last_name_icontains (Union[Unset, None, str]):
        assignee_last_name_iregex (Union[Unset, None, str]):
        assignee_last_name_isnull (Union[Unset, None, str]):
        assignee_last_name_istartswith (Union[Unset, None, str]):
        assignee_last_name_search (Union[Unset, None, str]):
        assignee_phone (Union[Unset, None, str]):
        assignee_phone_icontains (Union[Unset, None, str]):
        assignee_phone_iregex (Union[Unset, None, str]):
        assignee_phone_isnull (Union[Unset, None, str]):
        assignee_phone_istartswith (Union[Unset, None, str]):
        assignee_phone_search (Union[Unset, None, str]):
        assignee_id (Union[Unset, None, str]):
        assignee_id_in (Union[Unset, None, str]):
        assignee_id_isnull (Union[Unset, None, str]):
        assignee_proximity (Union[Unset, None, TaskExportsListAssigneeProximity]):
        assignee_proximity_in (Union[Unset, None, str]):
        category (Union[Unset, None, TaskExportsListCategory]):
        category_in (Union[Unset, None, str]):
        contact_company_icontains (Union[Unset, None, str]):
        contact_company_in (Union[Unset, None, str]):
        contact_company_iregex (Union[Unset, None, str]):
        contact_company_istartswith (Union[Unset, None, str]):
        contact_company_search (Union[Unset, None, str]):
        contact_email (Union[Unset, None, str]):
        contact_email_icontains (Union[Unset, None, str]):
        contact_email_in (Union[Unset, None, str]):
        contact_email_iregex (Union[Unset, None, str]):
        contact_email_istartswith (Union[Unset, None, str]):
        contact_email_search (Union[Unset, None, str]):
        contact_name (Union[Unset, None, str]):
        contact_name_icontains (Union[Unset, None, str]):
        contact_name_in (Union[Unset, None, str]):
        contact_name_iregex (Union[Unset, None, str]):
        contact_name_istartswith (Union[Unset, None, str]):
        contact_name_search (Union[Unset, None, str]):
        contact_notes (Union[Unset, None, str]):
        contact_notes_icontains (Union[Unset, None, str]):
        contact_notes_in (Union[Unset, None, str]):
        contact_notes_iregex (Union[Unset, None, str]):
        contact_notes_istartswith (Union[Unset, None, str]):
        contact_notes_search (Union[Unset, None, str]):
        contact_phone (Union[Unset, None, str]):
        contact_phone_icontains (Union[Unset, None, str]):
        contact_phone_in (Union[Unset, None, str]):
        contact_phone_iregex (Union[Unset, None, str]):
        contact_phone_istartswith (Union[Unset, None, str]):
        contact_phone_search (Union[Unset, None, str]):
        contact_id (Union[Unset, None, str]):
        contact_id_in (Union[Unset, None, str]):
        contact_id_isnull (Union[Unset, None, str]):
        created_by (Union[Unset, None, str]):
        created_by_in (Union[Unset, None, str]):
        created_by_isnull (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        description_icontains (Union[Unset, None, str]):
        description_iregex (Union[Unset, None, str]):
        description_istartswith (Union[Unset, None, str]):
        description_search (Union[Unset, None, str]):
        duration (Union[Unset, None, str]):
        duration_gt (Union[Unset, None, str]):
        duration_gte (Union[Unset, None, str]):
        duration_lt (Union[Unset, None, str]):
        duration_lte (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        external_id_in (Union[Unset, None, str]):
        external_id_iregex (Union[Unset, None, str]):
        external_id_isnull (Union[Unset, None, str]):
        external_id_istartswith (Union[Unset, None, str]):
        external_id_search (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):
        format_ (Union[Unset, None, TaskExportsListFormat]):  Default: TaskExportsListFormat.JSON.
        id (Union[Unset, None, str]):
        id_in (Union[Unset, None, str]):
        is_optimal (Union[Unset, None, str]):
        is_optimal_isnull (Union[Unset, None, str]):
        metadata_accepted_distance (Union[Unset, None, str]):
        metadata_accepted_distance_gt (Union[Unset, None, str]):
        metadata_accepted_distance_gte (Union[Unset, None, str]):
        metadata_accepted_distance_lt (Union[Unset, None, str]):
        metadata_accepted_distance_lte (Union[Unset, None, str]):
        metadata_accepted_duration (Union[Unset, None, str]):
        metadata_accepted_duration_gt (Union[Unset, None, str]):
        metadata_accepted_duration_gte (Union[Unset, None, str]):
        metadata_accepted_duration_lt (Union[Unset, None, str]):
        metadata_accepted_duration_lte (Union[Unset, None, str]):
        metadata_active_distance (Union[Unset, None, str]):
        metadata_active_distance_gt (Union[Unset, None, str]):
        metadata_active_distance_gte (Union[Unset, None, str]):
        metadata_active_distance_lt (Union[Unset, None, str]):
        metadata_active_distance_lte (Union[Unset, None, str]):
        metadata_active_duration (Union[Unset, None, str]):
        metadata_active_duration_gt (Union[Unset, None, str]):
        metadata_active_duration_gte (Union[Unset, None, str]):
        metadata_active_duration_lt (Union[Unset, None, str]):
        metadata_active_duration_lte (Union[Unset, None, str]):
        metadata_assigned_distance (Union[Unset, None, str]):
        metadata_assigned_distance_gt (Union[Unset, None, str]):
        metadata_assigned_distance_gte (Union[Unset, None, str]):
        metadata_assigned_distance_lt (Union[Unset, None, str]):
        metadata_assigned_distance_lte (Union[Unset, None, str]):
        metadata_assigned_duration (Union[Unset, None, str]):
        metadata_assigned_duration_gt (Union[Unset, None, str]):
        metadata_assigned_duration_gte (Union[Unset, None, str]):
        metadata_assigned_duration_lt (Union[Unset, None, str]):
        metadata_assigned_duration_lte (Union[Unset, None, str]):
        metadata_cancelled_distance (Union[Unset, None, str]):
        metadata_cancelled_distance_gt (Union[Unset, None, str]):
        metadata_cancelled_distance_gte (Union[Unset, None, str]):
        metadata_cancelled_distance_lt (Union[Unset, None, str]):
        metadata_cancelled_distance_lte (Union[Unset, None, str]):
        metadata_cancelled_duration (Union[Unset, None, str]):
        metadata_cancelled_duration_gt (Union[Unset, None, str]):
        metadata_cancelled_duration_gte (Union[Unset, None, str]):
        metadata_cancelled_duration_lt (Union[Unset, None, str]):
        metadata_cancelled_duration_lte (Union[Unset, None, str]):
        metadata_completed_distance (Union[Unset, None, str]):
        metadata_completed_distance_gt (Union[Unset, None, str]):
        metadata_completed_distance_gte (Union[Unset, None, str]):
        metadata_completed_distance_lt (Union[Unset, None, str]):
        metadata_completed_distance_lte (Union[Unset, None, str]):
        metadata_completed_duration (Union[Unset, None, str]):
        metadata_completed_duration_gt (Union[Unset, None, str]):
        metadata_completed_duration_gte (Union[Unset, None, str]):
        metadata_completed_duration_lt (Union[Unset, None, str]):
        metadata_completed_duration_lte (Union[Unset, None, str]):
        metadata_documents_count (Union[Unset, None, str]):
        metadata_documents_count_gt (Union[Unset, None, str]):
        metadata_documents_count_gte (Union[Unset, None, str]):
        metadata_documents_count_lt (Union[Unset, None, str]):
        metadata_documents_count_lte (Union[Unset, None, str]):
        metadata_events_count (Union[Unset, None, str]):
        metadata_events_count_gt (Union[Unset, None, str]):
        metadata_events_count_gte (Union[Unset, None, str]):
        metadata_events_count_lt (Union[Unset, None, str]):
        metadata_events_count_lte (Union[Unset, None, str]):
        metadata_failed_distance (Union[Unset, None, str]):
        metadata_failed_distance_gt (Union[Unset, None, str]):
        metadata_failed_distance_gte (Union[Unset, None, str]):
        metadata_failed_distance_lt (Union[Unset, None, str]):
        metadata_failed_distance_lte (Union[Unset, None, str]):
        metadata_failed_duration (Union[Unset, None, str]):
        metadata_failed_duration_gt (Union[Unset, None, str]):
        metadata_failed_duration_gte (Union[Unset, None, str]):
        metadata_failed_duration_lt (Union[Unset, None, str]):
        metadata_failed_duration_lte (Union[Unset, None, str]):
        metadata_forms_completed_count (Union[Unset, None, str]):
        metadata_forms_completed_count_gt (Union[Unset, None, str]):
        metadata_forms_completed_count_gte (Union[Unset, None, str]):
        metadata_forms_completed_count_lt (Union[Unset, None, str]):
        metadata_forms_completed_count_lte (Union[Unset, None, str]):
        metadata_forms_count (Union[Unset, None, str]):
        metadata_forms_count_gt (Union[Unset, None, str]):
        metadata_forms_count_gte (Union[Unset, None, str]):
        metadata_forms_count_lt (Union[Unset, None, str]):
        metadata_forms_count_lte (Union[Unset, None, str]):
        metadata_signatures_count (Union[Unset, None, str]):
        metadata_signatures_count_gt (Union[Unset, None, str]):
        metadata_signatures_count_gte (Union[Unset, None, str]):
        metadata_signatures_count_lt (Union[Unset, None, str]):
        metadata_signatures_count_lte (Union[Unset, None, str]):
        metadata_task_event_notes_count (Union[Unset, None, str]):
        metadata_task_event_notes_count_gt (Union[Unset, None, str]):
        metadata_task_event_notes_count_gte (Union[Unset, None, str]):
        metadata_task_event_notes_count_lt (Union[Unset, None, str]):
        metadata_task_event_notes_count_lte (Union[Unset, None, str]):
        metadata_transit_distance (Union[Unset, None, str]):
        metadata_transit_distance_gt (Union[Unset, None, str]):
        metadata_transit_distance_gte (Union[Unset, None, str]):
        metadata_transit_distance_lt (Union[Unset, None, str]):
        metadata_transit_distance_lte (Union[Unset, None, str]):
        metadata_transit_duration (Union[Unset, None, str]):
        metadata_transit_duration_gt (Union[Unset, None, str]):
        metadata_transit_duration_gte (Union[Unset, None, str]):
        metadata_transit_duration_lt (Union[Unset, None, str]):
        metadata_transit_duration_lte (Union[Unset, None, str]):
        metadata_unassigned_distance (Union[Unset, None, str]):
        metadata_unassigned_distance_gt (Union[Unset, None, str]):
        metadata_unassigned_distance_gte (Union[Unset, None, str]):
        metadata_unassigned_distance_lt (Union[Unset, None, str]):
        metadata_unassigned_distance_lte (Union[Unset, None, str]):
        metadata_unassigned_duration (Union[Unset, None, str]):
        metadata_unassigned_duration_gt (Union[Unset, None, str]):
        metadata_unassigned_duration_gte (Union[Unset, None, str]):
        metadata_unassigned_duration_lt (Union[Unset, None, str]):
        metadata_unassigned_duration_lte (Union[Unset, None, str]):
        order_auto_assign (Union[Unset, None, str]):
        order_created_by (Union[Unset, None, str]):
        order_created_by_in (Union[Unset, None, str]):
        order_created_by_isnull (Union[Unset, None, str]):
        order_external_id (Union[Unset, None, str]):
        order_external_id_icontains (Union[Unset, None, str]):
        order_external_id_in (Union[Unset, None, str]):
        order_external_id_iregex (Union[Unset, None, str]):
        order_external_id_isnull (Union[Unset, None, str]):
        order_external_id_istartswith (Union[Unset, None, str]):
        order_external_id_search (Union[Unset, None, str]):
        order_reference (Union[Unset, None, str]):
        order_reference_icontains (Union[Unset, None, str]):
        order_reference_in (Union[Unset, None, str]):
        order_reference_iregex (Union[Unset, None, str]):
        order_reference_istartswith (Union[Unset, None, str]):
        order_reference_search (Union[Unset, None, str]):
        order_id (Union[Unset, None, str]):
        order_id_in (Union[Unset, None, str]):
        order_id_isnull (Union[Unset, None, str]):
        orderer_id (Union[Unset, None, str]):
        orderer_id_in (Union[Unset, None, str]):
        orderer_id_isnull (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        owner_id (Union[Unset, None, str]):
        owner_id_in (Union[Unset, None, str]):
        owner_id_isnull (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        priority (Union[Unset, None, str]):
        priority_gt (Union[Unset, None, str]):
        priority_gte (Union[Unset, None, str]):
        priority_in (Union[Unset, None, str]):
        priority_lt (Union[Unset, None, str]):
        priority_lte (Union[Unset, None, str]):
        receiver_id (Union[Unset, None, str]):
        receiver_id_in (Union[Unset, None, str]):
        receiver_id_isnull (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        reference_icontains (Union[Unset, None, str]):
        reference_in (Union[Unset, None, str]):
        reference_iregex (Union[Unset, None, str]):
        reference_istartswith (Union[Unset, None, str]):
        reference_search (Union[Unset, None, str]):
        route_id (Union[Unset, None, str]):
        route_id_in (Union[Unset, None, str]):
        route_id_isnull (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, TaskExportsListState]):
        state_in (Union[Unset, None, str]):
        unassignee_id (Union[Unset, None, str]):
        unassignee_id_in (Union[Unset, None, str]):
        unassignee_id_isnull (Union[Unset, None, str]):

    Returns:
        Response[List[TaskExport]]
    """

    kwargs = _get_kwargs(
        client=client,
        address_apartment_number=address_apartment_number,
        address_apartment_number_icontains=address_apartment_number_icontains,
        address_apartment_number_in=address_apartment_number_in,
        address_apartment_number_iregex=address_apartment_number_iregex,
        address_apartment_number_istartswith=address_apartment_number_istartswith,
        address_apartment_number_search=address_apartment_number_search,
        address_city=address_city,
        address_city_icontains=address_city_icontains,
        address_city_in=address_city_in,
        address_city_iregex=address_city_iregex,
        address_city_istartswith=address_city_istartswith,
        address_city_search=address_city_search,
        address_country=address_country,
        address_country_icontains=address_country_icontains,
        address_country_in=address_country_in,
        address_country_iregex=address_country_iregex,
        address_country_istartswith=address_country_istartswith,
        address_country_search=address_country_search,
        address_country_code=address_country_code,
        address_country_code_icontains=address_country_code_icontains,
        address_country_code_in=address_country_code_in,
        address_country_code_iregex=address_country_code_iregex,
        address_country_code_istartswith=address_country_code_istartswith,
        address_country_code_search=address_country_code_search,
        address_formatted_address=address_formatted_address,
        address_formatted_address_icontains=address_formatted_address_icontains,
        address_formatted_address_in=address_formatted_address_in,
        address_formatted_address_iregex=address_formatted_address_iregex,
        address_formatted_address_istartswith=address_formatted_address_istartswith,
        address_formatted_address_search=address_formatted_address_search,
        address_google_place_id=address_google_place_id,
        address_google_place_id_icontains=address_google_place_id_icontains,
        address_google_place_id_in=address_google_place_id_in,
        address_google_place_id_iregex=address_google_place_id_iregex,
        address_google_place_id_istartswith=address_google_place_id_istartswith,
        address_google_place_id_search=address_google_place_id_search,
        address_house_number=address_house_number,
        address_house_number_icontains=address_house_number_icontains,
        address_house_number_in=address_house_number_in,
        address_house_number_iregex=address_house_number_iregex,
        address_house_number_istartswith=address_house_number_istartswith,
        address_house_number_search=address_house_number_search,
        address_point_of_interest=address_point_of_interest,
        address_point_of_interest_icontains=address_point_of_interest_icontains,
        address_point_of_interest_in=address_point_of_interest_in,
        address_point_of_interest_iregex=address_point_of_interest_iregex,
        address_point_of_interest_istartswith=address_point_of_interest_istartswith,
        address_point_of_interest_search=address_point_of_interest_search,
        address_postal_code=address_postal_code,
        address_postal_code_icontains=address_postal_code_icontains,
        address_postal_code_in=address_postal_code_in,
        address_postal_code_iregex=address_postal_code_iregex,
        address_postal_code_istartswith=address_postal_code_istartswith,
        address_postal_code_search=address_postal_code_search,
        address_raw_address=address_raw_address,
        address_raw_address_icontains=address_raw_address_icontains,
        address_raw_address_in=address_raw_address_in,
        address_raw_address_iregex=address_raw_address_iregex,
        address_raw_address_istartswith=address_raw_address_istartswith,
        address_raw_address_search=address_raw_address_search,
        address_state=address_state,
        address_state_icontains=address_state_icontains,
        address_state_in=address_state_in,
        address_state_iregex=address_state_iregex,
        address_state_istartswith=address_state_istartswith,
        address_state_search=address_state_search,
        address_street=address_street,
        address_street_icontains=address_street_icontains,
        address_street_in=address_street_in,
        address_street_iregex=address_street_iregex,
        address_street_istartswith=address_street_istartswith,
        address_street_search=address_street_search,
        address_id=address_id,
        address_id_in=address_id_in,
        address_id_isnull=address_id_isnull,
        assignee_email=assignee_email,
        assignee_email_icontains=assignee_email_icontains,
        assignee_email_iregex=assignee_email_iregex,
        assignee_email_isnull=assignee_email_isnull,
        assignee_email_istartswith=assignee_email_istartswith,
        assignee_email_search=assignee_email_search,
        assignee_first_name=assignee_first_name,
        assignee_first_name_icontains=assignee_first_name_icontains,
        assignee_first_name_iregex=assignee_first_name_iregex,
        assignee_first_name_isnull=assignee_first_name_isnull,
        assignee_first_name_istartswith=assignee_first_name_istartswith,
        assignee_first_name_search=assignee_first_name_search,
        assignee_last_name=assignee_last_name,
        assignee_last_name_icontains=assignee_last_name_icontains,
        assignee_last_name_iregex=assignee_last_name_iregex,
        assignee_last_name_isnull=assignee_last_name_isnull,
        assignee_last_name_istartswith=assignee_last_name_istartswith,
        assignee_last_name_search=assignee_last_name_search,
        assignee_phone=assignee_phone,
        assignee_phone_icontains=assignee_phone_icontains,
        assignee_phone_iregex=assignee_phone_iregex,
        assignee_phone_isnull=assignee_phone_isnull,
        assignee_phone_istartswith=assignee_phone_istartswith,
        assignee_phone_search=assignee_phone_search,
        assignee_id=assignee_id,
        assignee_id_in=assignee_id_in,
        assignee_id_isnull=assignee_id_isnull,
        assignee_proximity=assignee_proximity,
        assignee_proximity_in=assignee_proximity_in,
        category=category,
        category_in=category_in,
        contact_company_icontains=contact_company_icontains,
        contact_company_in=contact_company_in,
        contact_company_iregex=contact_company_iregex,
        contact_company_istartswith=contact_company_istartswith,
        contact_company_search=contact_company_search,
        contact_email=contact_email,
        contact_email_icontains=contact_email_icontains,
        contact_email_in=contact_email_in,
        contact_email_iregex=contact_email_iregex,
        contact_email_istartswith=contact_email_istartswith,
        contact_email_search=contact_email_search,
        contact_name=contact_name,
        contact_name_icontains=contact_name_icontains,
        contact_name_in=contact_name_in,
        contact_name_iregex=contact_name_iregex,
        contact_name_istartswith=contact_name_istartswith,
        contact_name_search=contact_name_search,
        contact_notes=contact_notes,
        contact_notes_icontains=contact_notes_icontains,
        contact_notes_in=contact_notes_in,
        contact_notes_iregex=contact_notes_iregex,
        contact_notes_istartswith=contact_notes_istartswith,
        contact_notes_search=contact_notes_search,
        contact_phone=contact_phone,
        contact_phone_icontains=contact_phone_icontains,
        contact_phone_in=contact_phone_in,
        contact_phone_iregex=contact_phone_iregex,
        contact_phone_istartswith=contact_phone_istartswith,
        contact_phone_search=contact_phone_search,
        contact_id=contact_id,
        contact_id_in=contact_id_in,
        contact_id_isnull=contact_id_isnull,
        created_by=created_by,
        created_by_in=created_by_in,
        created_by_isnull=created_by_isnull,
        description=description,
        description_icontains=description_icontains,
        description_iregex=description_iregex,
        description_istartswith=description_istartswith,
        description_search=description_search,
        duration=duration,
        duration_gt=duration_gt,
        duration_gte=duration_gte,
        duration_lt=duration_lt,
        duration_lte=duration_lte,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        external_id_in=external_id_in,
        external_id_iregex=external_id_iregex,
        external_id_isnull=external_id_isnull,
        external_id_istartswith=external_id_istartswith,
        external_id_search=external_id_search,
        fields=fields,
        format_=format_,
        id=id,
        id_in=id_in,
        is_optimal=is_optimal,
        is_optimal_isnull=is_optimal_isnull,
        metadata_accepted_distance=metadata_accepted_distance,
        metadata_accepted_distance_gt=metadata_accepted_distance_gt,
        metadata_accepted_distance_gte=metadata_accepted_distance_gte,
        metadata_accepted_distance_lt=metadata_accepted_distance_lt,
        metadata_accepted_distance_lte=metadata_accepted_distance_lte,
        metadata_accepted_duration=metadata_accepted_duration,
        metadata_accepted_duration_gt=metadata_accepted_duration_gt,
        metadata_accepted_duration_gte=metadata_accepted_duration_gte,
        metadata_accepted_duration_lt=metadata_accepted_duration_lt,
        metadata_accepted_duration_lte=metadata_accepted_duration_lte,
        metadata_active_distance=metadata_active_distance,
        metadata_active_distance_gt=metadata_active_distance_gt,
        metadata_active_distance_gte=metadata_active_distance_gte,
        metadata_active_distance_lt=metadata_active_distance_lt,
        metadata_active_distance_lte=metadata_active_distance_lte,
        metadata_active_duration=metadata_active_duration,
        metadata_active_duration_gt=metadata_active_duration_gt,
        metadata_active_duration_gte=metadata_active_duration_gte,
        metadata_active_duration_lt=metadata_active_duration_lt,
        metadata_active_duration_lte=metadata_active_duration_lte,
        metadata_assigned_distance=metadata_assigned_distance,
        metadata_assigned_distance_gt=metadata_assigned_distance_gt,
        metadata_assigned_distance_gte=metadata_assigned_distance_gte,
        metadata_assigned_distance_lt=metadata_assigned_distance_lt,
        metadata_assigned_distance_lte=metadata_assigned_distance_lte,
        metadata_assigned_duration=metadata_assigned_duration,
        metadata_assigned_duration_gt=metadata_assigned_duration_gt,
        metadata_assigned_duration_gte=metadata_assigned_duration_gte,
        metadata_assigned_duration_lt=metadata_assigned_duration_lt,
        metadata_assigned_duration_lte=metadata_assigned_duration_lte,
        metadata_cancelled_distance=metadata_cancelled_distance,
        metadata_cancelled_distance_gt=metadata_cancelled_distance_gt,
        metadata_cancelled_distance_gte=metadata_cancelled_distance_gte,
        metadata_cancelled_distance_lt=metadata_cancelled_distance_lt,
        metadata_cancelled_distance_lte=metadata_cancelled_distance_lte,
        metadata_cancelled_duration=metadata_cancelled_duration,
        metadata_cancelled_duration_gt=metadata_cancelled_duration_gt,
        metadata_cancelled_duration_gte=metadata_cancelled_duration_gte,
        metadata_cancelled_duration_lt=metadata_cancelled_duration_lt,
        metadata_cancelled_duration_lte=metadata_cancelled_duration_lte,
        metadata_completed_distance=metadata_completed_distance,
        metadata_completed_distance_gt=metadata_completed_distance_gt,
        metadata_completed_distance_gte=metadata_completed_distance_gte,
        metadata_completed_distance_lt=metadata_completed_distance_lt,
        metadata_completed_distance_lte=metadata_completed_distance_lte,
        metadata_completed_duration=metadata_completed_duration,
        metadata_completed_duration_gt=metadata_completed_duration_gt,
        metadata_completed_duration_gte=metadata_completed_duration_gte,
        metadata_completed_duration_lt=metadata_completed_duration_lt,
        metadata_completed_duration_lte=metadata_completed_duration_lte,
        metadata_documents_count=metadata_documents_count,
        metadata_documents_count_gt=metadata_documents_count_gt,
        metadata_documents_count_gte=metadata_documents_count_gte,
        metadata_documents_count_lt=metadata_documents_count_lt,
        metadata_documents_count_lte=metadata_documents_count_lte,
        metadata_events_count=metadata_events_count,
        metadata_events_count_gt=metadata_events_count_gt,
        metadata_events_count_gte=metadata_events_count_gte,
        metadata_events_count_lt=metadata_events_count_lt,
        metadata_events_count_lte=metadata_events_count_lte,
        metadata_failed_distance=metadata_failed_distance,
        metadata_failed_distance_gt=metadata_failed_distance_gt,
        metadata_failed_distance_gte=metadata_failed_distance_gte,
        metadata_failed_distance_lt=metadata_failed_distance_lt,
        metadata_failed_distance_lte=metadata_failed_distance_lte,
        metadata_failed_duration=metadata_failed_duration,
        metadata_failed_duration_gt=metadata_failed_duration_gt,
        metadata_failed_duration_gte=metadata_failed_duration_gte,
        metadata_failed_duration_lt=metadata_failed_duration_lt,
        metadata_failed_duration_lte=metadata_failed_duration_lte,
        metadata_forms_completed_count=metadata_forms_completed_count,
        metadata_forms_completed_count_gt=metadata_forms_completed_count_gt,
        metadata_forms_completed_count_gte=metadata_forms_completed_count_gte,
        metadata_forms_completed_count_lt=metadata_forms_completed_count_lt,
        metadata_forms_completed_count_lte=metadata_forms_completed_count_lte,
        metadata_forms_count=metadata_forms_count,
        metadata_forms_count_gt=metadata_forms_count_gt,
        metadata_forms_count_gte=metadata_forms_count_gte,
        metadata_forms_count_lt=metadata_forms_count_lt,
        metadata_forms_count_lte=metadata_forms_count_lte,
        metadata_signatures_count=metadata_signatures_count,
        metadata_signatures_count_gt=metadata_signatures_count_gt,
        metadata_signatures_count_gte=metadata_signatures_count_gte,
        metadata_signatures_count_lt=metadata_signatures_count_lt,
        metadata_signatures_count_lte=metadata_signatures_count_lte,
        metadata_task_event_notes_count=metadata_task_event_notes_count,
        metadata_task_event_notes_count_gt=metadata_task_event_notes_count_gt,
        metadata_task_event_notes_count_gte=metadata_task_event_notes_count_gte,
        metadata_task_event_notes_count_lt=metadata_task_event_notes_count_lt,
        metadata_task_event_notes_count_lte=metadata_task_event_notes_count_lte,
        metadata_transit_distance=metadata_transit_distance,
        metadata_transit_distance_gt=metadata_transit_distance_gt,
        metadata_transit_distance_gte=metadata_transit_distance_gte,
        metadata_transit_distance_lt=metadata_transit_distance_lt,
        metadata_transit_distance_lte=metadata_transit_distance_lte,
        metadata_transit_duration=metadata_transit_duration,
        metadata_transit_duration_gt=metadata_transit_duration_gt,
        metadata_transit_duration_gte=metadata_transit_duration_gte,
        metadata_transit_duration_lt=metadata_transit_duration_lt,
        metadata_transit_duration_lte=metadata_transit_duration_lte,
        metadata_unassigned_distance=metadata_unassigned_distance,
        metadata_unassigned_distance_gt=metadata_unassigned_distance_gt,
        metadata_unassigned_distance_gte=metadata_unassigned_distance_gte,
        metadata_unassigned_distance_lt=metadata_unassigned_distance_lt,
        metadata_unassigned_distance_lte=metadata_unassigned_distance_lte,
        metadata_unassigned_duration=metadata_unassigned_duration,
        metadata_unassigned_duration_gt=metadata_unassigned_duration_gt,
        metadata_unassigned_duration_gte=metadata_unassigned_duration_gte,
        metadata_unassigned_duration_lt=metadata_unassigned_duration_lt,
        metadata_unassigned_duration_lte=metadata_unassigned_duration_lte,
        order_auto_assign=order_auto_assign,
        order_created_by=order_created_by,
        order_created_by_in=order_created_by_in,
        order_created_by_isnull=order_created_by_isnull,
        order_external_id=order_external_id,
        order_external_id_icontains=order_external_id_icontains,
        order_external_id_in=order_external_id_in,
        order_external_id_iregex=order_external_id_iregex,
        order_external_id_isnull=order_external_id_isnull,
        order_external_id_istartswith=order_external_id_istartswith,
        order_external_id_search=order_external_id_search,
        order_reference=order_reference,
        order_reference_icontains=order_reference_icontains,
        order_reference_in=order_reference_in,
        order_reference_iregex=order_reference_iregex,
        order_reference_istartswith=order_reference_istartswith,
        order_reference_search=order_reference_search,
        order_id=order_id,
        order_id_in=order_id_in,
        order_id_isnull=order_id_isnull,
        orderer_id=orderer_id,
        orderer_id_in=orderer_id_in,
        orderer_id_isnull=orderer_id_isnull,
        ordering=ordering,
        owner_id=owner_id,
        owner_id_in=owner_id_in,
        owner_id_isnull=owner_id_isnull,
        page=page,
        page_size=page_size,
        priority=priority,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_in=priority_in,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        receiver_id=receiver_id,
        receiver_id_in=receiver_id_in,
        receiver_id_isnull=receiver_id_isnull,
        reference=reference,
        reference_icontains=reference_icontains,
        reference_in=reference_in,
        reference_iregex=reference_iregex,
        reference_istartswith=reference_istartswith,
        reference_search=reference_search,
        route_id=route_id,
        route_id_in=route_id_in,
        route_id_isnull=route_id_isnull,
        search=search,
        state=state,
        state_in=state_in,
        unassignee_id=unassignee_id,
        unassignee_id_in=unassignee_id_in,
        unassignee_id_isnull=unassignee_id_isnull,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    address_apartment_number: Union[Unset, None, str] = UNSET,
    address_apartment_number_icontains: Union[Unset, None, str] = UNSET,
    address_apartment_number_in: Union[Unset, None, str] = UNSET,
    address_apartment_number_iregex: Union[Unset, None, str] = UNSET,
    address_apartment_number_istartswith: Union[Unset, None, str] = UNSET,
    address_apartment_number_search: Union[Unset, None, str] = UNSET,
    address_city: Union[Unset, None, str] = UNSET,
    address_city_icontains: Union[Unset, None, str] = UNSET,
    address_city_in: Union[Unset, None, str] = UNSET,
    address_city_iregex: Union[Unset, None, str] = UNSET,
    address_city_istartswith: Union[Unset, None, str] = UNSET,
    address_city_search: Union[Unset, None, str] = UNSET,
    address_country: Union[Unset, None, str] = UNSET,
    address_country_icontains: Union[Unset, None, str] = UNSET,
    address_country_in: Union[Unset, None, str] = UNSET,
    address_country_iregex: Union[Unset, None, str] = UNSET,
    address_country_istartswith: Union[Unset, None, str] = UNSET,
    address_country_search: Union[Unset, None, str] = UNSET,
    address_country_code: Union[Unset, None, str] = UNSET,
    address_country_code_icontains: Union[Unset, None, str] = UNSET,
    address_country_code_in: Union[Unset, None, str] = UNSET,
    address_country_code_iregex: Union[Unset, None, str] = UNSET,
    address_country_code_istartswith: Union[Unset, None, str] = UNSET,
    address_country_code_search: Union[Unset, None, str] = UNSET,
    address_formatted_address: Union[Unset, None, str] = UNSET,
    address_formatted_address_icontains: Union[Unset, None, str] = UNSET,
    address_formatted_address_in: Union[Unset, None, str] = UNSET,
    address_formatted_address_iregex: Union[Unset, None, str] = UNSET,
    address_formatted_address_istartswith: Union[Unset, None, str] = UNSET,
    address_formatted_address_search: Union[Unset, None, str] = UNSET,
    address_google_place_id: Union[Unset, None, str] = UNSET,
    address_google_place_id_icontains: Union[Unset, None, str] = UNSET,
    address_google_place_id_in: Union[Unset, None, str] = UNSET,
    address_google_place_id_iregex: Union[Unset, None, str] = UNSET,
    address_google_place_id_istartswith: Union[Unset, None, str] = UNSET,
    address_google_place_id_search: Union[Unset, None, str] = UNSET,
    address_house_number: Union[Unset, None, str] = UNSET,
    address_house_number_icontains: Union[Unset, None, str] = UNSET,
    address_house_number_in: Union[Unset, None, str] = UNSET,
    address_house_number_iregex: Union[Unset, None, str] = UNSET,
    address_house_number_istartswith: Union[Unset, None, str] = UNSET,
    address_house_number_search: Union[Unset, None, str] = UNSET,
    address_point_of_interest: Union[Unset, None, str] = UNSET,
    address_point_of_interest_icontains: Union[Unset, None, str] = UNSET,
    address_point_of_interest_in: Union[Unset, None, str] = UNSET,
    address_point_of_interest_iregex: Union[Unset, None, str] = UNSET,
    address_point_of_interest_istartswith: Union[Unset, None, str] = UNSET,
    address_point_of_interest_search: Union[Unset, None, str] = UNSET,
    address_postal_code: Union[Unset, None, str] = UNSET,
    address_postal_code_icontains: Union[Unset, None, str] = UNSET,
    address_postal_code_in: Union[Unset, None, str] = UNSET,
    address_postal_code_iregex: Union[Unset, None, str] = UNSET,
    address_postal_code_istartswith: Union[Unset, None, str] = UNSET,
    address_postal_code_search: Union[Unset, None, str] = UNSET,
    address_raw_address: Union[Unset, None, str] = UNSET,
    address_raw_address_icontains: Union[Unset, None, str] = UNSET,
    address_raw_address_in: Union[Unset, None, str] = UNSET,
    address_raw_address_iregex: Union[Unset, None, str] = UNSET,
    address_raw_address_istartswith: Union[Unset, None, str] = UNSET,
    address_raw_address_search: Union[Unset, None, str] = UNSET,
    address_state: Union[Unset, None, str] = UNSET,
    address_state_icontains: Union[Unset, None, str] = UNSET,
    address_state_in: Union[Unset, None, str] = UNSET,
    address_state_iregex: Union[Unset, None, str] = UNSET,
    address_state_istartswith: Union[Unset, None, str] = UNSET,
    address_state_search: Union[Unset, None, str] = UNSET,
    address_street: Union[Unset, None, str] = UNSET,
    address_street_icontains: Union[Unset, None, str] = UNSET,
    address_street_in: Union[Unset, None, str] = UNSET,
    address_street_iregex: Union[Unset, None, str] = UNSET,
    address_street_istartswith: Union[Unset, None, str] = UNSET,
    address_street_search: Union[Unset, None, str] = UNSET,
    address_id: Union[Unset, None, str] = UNSET,
    address_id_in: Union[Unset, None, str] = UNSET,
    address_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_email: Union[Unset, None, str] = UNSET,
    assignee_email_icontains: Union[Unset, None, str] = UNSET,
    assignee_email_iregex: Union[Unset, None, str] = UNSET,
    assignee_email_isnull: Union[Unset, None, str] = UNSET,
    assignee_email_istartswith: Union[Unset, None, str] = UNSET,
    assignee_email_search: Union[Unset, None, str] = UNSET,
    assignee_first_name: Union[Unset, None, str] = UNSET,
    assignee_first_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_first_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_first_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_first_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_first_name_search: Union[Unset, None, str] = UNSET,
    assignee_last_name: Union[Unset, None, str] = UNSET,
    assignee_last_name_icontains: Union[Unset, None, str] = UNSET,
    assignee_last_name_iregex: Union[Unset, None, str] = UNSET,
    assignee_last_name_isnull: Union[Unset, None, str] = UNSET,
    assignee_last_name_istartswith: Union[Unset, None, str] = UNSET,
    assignee_last_name_search: Union[Unset, None, str] = UNSET,
    assignee_phone: Union[Unset, None, str] = UNSET,
    assignee_phone_icontains: Union[Unset, None, str] = UNSET,
    assignee_phone_iregex: Union[Unset, None, str] = UNSET,
    assignee_phone_isnull: Union[Unset, None, str] = UNSET,
    assignee_phone_istartswith: Union[Unset, None, str] = UNSET,
    assignee_phone_search: Union[Unset, None, str] = UNSET,
    assignee_id: Union[Unset, None, str] = UNSET,
    assignee_id_in: Union[Unset, None, str] = UNSET,
    assignee_id_isnull: Union[Unset, None, str] = UNSET,
    assignee_proximity: Union[Unset, None, TaskExportsListAssigneeProximity] = UNSET,
    assignee_proximity_in: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskExportsListCategory] = UNSET,
    category_in: Union[Unset, None, str] = UNSET,
    contact_company_icontains: Union[Unset, None, str] = UNSET,
    contact_company_in: Union[Unset, None, str] = UNSET,
    contact_company_iregex: Union[Unset, None, str] = UNSET,
    contact_company_istartswith: Union[Unset, None, str] = UNSET,
    contact_company_search: Union[Unset, None, str] = UNSET,
    contact_email: Union[Unset, None, str] = UNSET,
    contact_email_icontains: Union[Unset, None, str] = UNSET,
    contact_email_in: Union[Unset, None, str] = UNSET,
    contact_email_iregex: Union[Unset, None, str] = UNSET,
    contact_email_istartswith: Union[Unset, None, str] = UNSET,
    contact_email_search: Union[Unset, None, str] = UNSET,
    contact_name: Union[Unset, None, str] = UNSET,
    contact_name_icontains: Union[Unset, None, str] = UNSET,
    contact_name_in: Union[Unset, None, str] = UNSET,
    contact_name_iregex: Union[Unset, None, str] = UNSET,
    contact_name_istartswith: Union[Unset, None, str] = UNSET,
    contact_name_search: Union[Unset, None, str] = UNSET,
    contact_notes: Union[Unset, None, str] = UNSET,
    contact_notes_icontains: Union[Unset, None, str] = UNSET,
    contact_notes_in: Union[Unset, None, str] = UNSET,
    contact_notes_iregex: Union[Unset, None, str] = UNSET,
    contact_notes_istartswith: Union[Unset, None, str] = UNSET,
    contact_notes_search: Union[Unset, None, str] = UNSET,
    contact_phone: Union[Unset, None, str] = UNSET,
    contact_phone_icontains: Union[Unset, None, str] = UNSET,
    contact_phone_in: Union[Unset, None, str] = UNSET,
    contact_phone_iregex: Union[Unset, None, str] = UNSET,
    contact_phone_istartswith: Union[Unset, None, str] = UNSET,
    contact_phone_search: Union[Unset, None, str] = UNSET,
    contact_id: Union[Unset, None, str] = UNSET,
    contact_id_in: Union[Unset, None, str] = UNSET,
    contact_id_isnull: Union[Unset, None, str] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    created_by_in: Union[Unset, None, str] = UNSET,
    created_by_isnull: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    description_icontains: Union[Unset, None, str] = UNSET,
    description_iregex: Union[Unset, None, str] = UNSET,
    description_istartswith: Union[Unset, None, str] = UNSET,
    description_search: Union[Unset, None, str] = UNSET,
    duration: Union[Unset, None, str] = UNSET,
    duration_gt: Union[Unset, None, str] = UNSET,
    duration_gte: Union[Unset, None, str] = UNSET,
    duration_lt: Union[Unset, None, str] = UNSET,
    duration_lte: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    external_id_in: Union[Unset, None, str] = UNSET,
    external_id_iregex: Union[Unset, None, str] = UNSET,
    external_id_isnull: Union[Unset, None, str] = UNSET,
    external_id_istartswith: Union[Unset, None, str] = UNSET,
    external_id_search: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, TaskExportsListFormat] = TaskExportsListFormat.JSON,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    is_optimal: Union[Unset, None, str] = UNSET,
    is_optimal_isnull: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_accepted_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_active_distance: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_active_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_active_duration: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_active_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_assigned_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_cancelled_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_completed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_documents_count: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_gte: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lt: Union[Unset, None, str] = UNSET,
    metadata_documents_count_lte: Union[Unset, None, str] = UNSET,
    metadata_events_count: Union[Unset, None, str] = UNSET,
    metadata_events_count_gt: Union[Unset, None, str] = UNSET,
    metadata_events_count_gte: Union[Unset, None, str] = UNSET,
    metadata_events_count_lt: Union[Unset, None, str] = UNSET,
    metadata_events_count_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_failed_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_completed_count_lte: Union[Unset, None, str] = UNSET,
    metadata_forms_count: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_gte: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lt: Union[Unset, None, str] = UNSET,
    metadata_forms_count_lte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_gte: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lt: Union[Unset, None, str] = UNSET,
    metadata_signatures_count_lte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_gte: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lt: Union[Unset, None, str] = UNSET,
    metadata_task_event_notes_count_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_transit_duration_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_distance_lte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_gte: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lt: Union[Unset, None, str] = UNSET,
    metadata_unassigned_duration_lte: Union[Unset, None, str] = UNSET,
    order_auto_assign: Union[Unset, None, str] = UNSET,
    order_created_by: Union[Unset, None, str] = UNSET,
    order_created_by_in: Union[Unset, None, str] = UNSET,
    order_created_by_isnull: Union[Unset, None, str] = UNSET,
    order_external_id: Union[Unset, None, str] = UNSET,
    order_external_id_icontains: Union[Unset, None, str] = UNSET,
    order_external_id_in: Union[Unset, None, str] = UNSET,
    order_external_id_iregex: Union[Unset, None, str] = UNSET,
    order_external_id_isnull: Union[Unset, None, str] = UNSET,
    order_external_id_istartswith: Union[Unset, None, str] = UNSET,
    order_external_id_search: Union[Unset, None, str] = UNSET,
    order_reference: Union[Unset, None, str] = UNSET,
    order_reference_icontains: Union[Unset, None, str] = UNSET,
    order_reference_in: Union[Unset, None, str] = UNSET,
    order_reference_iregex: Union[Unset, None, str] = UNSET,
    order_reference_istartswith: Union[Unset, None, str] = UNSET,
    order_reference_search: Union[Unset, None, str] = UNSET,
    order_id: Union[Unset, None, str] = UNSET,
    order_id_in: Union[Unset, None, str] = UNSET,
    order_id_isnull: Union[Unset, None, str] = UNSET,
    orderer_id: Union[Unset, None, str] = UNSET,
    orderer_id_in: Union[Unset, None, str] = UNSET,
    orderer_id_isnull: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    owner_id: Union[Unset, None, str] = UNSET,
    owner_id_in: Union[Unset, None, str] = UNSET,
    owner_id_isnull: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    priority_gt: Union[Unset, None, str] = UNSET,
    priority_gte: Union[Unset, None, str] = UNSET,
    priority_in: Union[Unset, None, str] = UNSET,
    priority_lt: Union[Unset, None, str] = UNSET,
    priority_lte: Union[Unset, None, str] = UNSET,
    receiver_id: Union[Unset, None, str] = UNSET,
    receiver_id_in: Union[Unset, None, str] = UNSET,
    receiver_id_isnull: Union[Unset, None, str] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    reference_icontains: Union[Unset, None, str] = UNSET,
    reference_in: Union[Unset, None, str] = UNSET,
    reference_iregex: Union[Unset, None, str] = UNSET,
    reference_istartswith: Union[Unset, None, str] = UNSET,
    reference_search: Union[Unset, None, str] = UNSET,
    route_id: Union[Unset, None, str] = UNSET,
    route_id_in: Union[Unset, None, str] = UNSET,
    route_id_isnull: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, TaskExportsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    unassignee_id: Union[Unset, None, str] = UNSET,
    unassignee_id_in: Union[Unset, None, str] = UNSET,
    unassignee_id_isnull: Union[Unset, None, str] = UNSET,
) -> Optional[List[TaskExport]]:
    """This view has multiple renderer classes available: `json` and `xlsx`. In order to export the data as
    an excel file, just set query argument `format` to `xlsx`.When downloading `xlsx` format, use Accept
    header `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; version=...`

    The user can request what fields and in what order will be rendered using query argument `fields`.
    This is a comma separated list of field names used in the API. Available fields are visible in the
    example.
    Also metafields can be added to the response. For this just add them as fields, using structure
    `metafields__{metafield.namespace}__{metafield.key}`.

    When exporting to **excel**, the column names may be changed based on account metafield names or
    pre-defined field name and width mapping.

    Changes in version 2.2.1:
     * field names have been updated to reflect the Task fields schema and filters.
     * Invalid fields in fields request will return a ValidationError.
     * Account filter is required.
     * AccountRole display name is annotated to user objects.
     * 'task_event_notes' is dropped.
     * 'contact_phone' and 'contact_email' is replaced with 'contact_phones' and 'contact_emails'.

    Args:
        address_apartment_number (Union[Unset, None, str]):
        address_apartment_number_icontains (Union[Unset, None, str]):
        address_apartment_number_in (Union[Unset, None, str]):
        address_apartment_number_iregex (Union[Unset, None, str]):
        address_apartment_number_istartswith (Union[Unset, None, str]):
        address_apartment_number_search (Union[Unset, None, str]):
        address_city (Union[Unset, None, str]):
        address_city_icontains (Union[Unset, None, str]):
        address_city_in (Union[Unset, None, str]):
        address_city_iregex (Union[Unset, None, str]):
        address_city_istartswith (Union[Unset, None, str]):
        address_city_search (Union[Unset, None, str]):
        address_country (Union[Unset, None, str]):
        address_country_icontains (Union[Unset, None, str]):
        address_country_in (Union[Unset, None, str]):
        address_country_iregex (Union[Unset, None, str]):
        address_country_istartswith (Union[Unset, None, str]):
        address_country_search (Union[Unset, None, str]):
        address_country_code (Union[Unset, None, str]):
        address_country_code_icontains (Union[Unset, None, str]):
        address_country_code_in (Union[Unset, None, str]):
        address_country_code_iregex (Union[Unset, None, str]):
        address_country_code_istartswith (Union[Unset, None, str]):
        address_country_code_search (Union[Unset, None, str]):
        address_formatted_address (Union[Unset, None, str]):
        address_formatted_address_icontains (Union[Unset, None, str]):
        address_formatted_address_in (Union[Unset, None, str]):
        address_formatted_address_iregex (Union[Unset, None, str]):
        address_formatted_address_istartswith (Union[Unset, None, str]):
        address_formatted_address_search (Union[Unset, None, str]):
        address_google_place_id (Union[Unset, None, str]):
        address_google_place_id_icontains (Union[Unset, None, str]):
        address_google_place_id_in (Union[Unset, None, str]):
        address_google_place_id_iregex (Union[Unset, None, str]):
        address_google_place_id_istartswith (Union[Unset, None, str]):
        address_google_place_id_search (Union[Unset, None, str]):
        address_house_number (Union[Unset, None, str]):
        address_house_number_icontains (Union[Unset, None, str]):
        address_house_number_in (Union[Unset, None, str]):
        address_house_number_iregex (Union[Unset, None, str]):
        address_house_number_istartswith (Union[Unset, None, str]):
        address_house_number_search (Union[Unset, None, str]):
        address_point_of_interest (Union[Unset, None, str]):
        address_point_of_interest_icontains (Union[Unset, None, str]):
        address_point_of_interest_in (Union[Unset, None, str]):
        address_point_of_interest_iregex (Union[Unset, None, str]):
        address_point_of_interest_istartswith (Union[Unset, None, str]):
        address_point_of_interest_search (Union[Unset, None, str]):
        address_postal_code (Union[Unset, None, str]):
        address_postal_code_icontains (Union[Unset, None, str]):
        address_postal_code_in (Union[Unset, None, str]):
        address_postal_code_iregex (Union[Unset, None, str]):
        address_postal_code_istartswith (Union[Unset, None, str]):
        address_postal_code_search (Union[Unset, None, str]):
        address_raw_address (Union[Unset, None, str]):
        address_raw_address_icontains (Union[Unset, None, str]):
        address_raw_address_in (Union[Unset, None, str]):
        address_raw_address_iregex (Union[Unset, None, str]):
        address_raw_address_istartswith (Union[Unset, None, str]):
        address_raw_address_search (Union[Unset, None, str]):
        address_state (Union[Unset, None, str]):
        address_state_icontains (Union[Unset, None, str]):
        address_state_in (Union[Unset, None, str]):
        address_state_iregex (Union[Unset, None, str]):
        address_state_istartswith (Union[Unset, None, str]):
        address_state_search (Union[Unset, None, str]):
        address_street (Union[Unset, None, str]):
        address_street_icontains (Union[Unset, None, str]):
        address_street_in (Union[Unset, None, str]):
        address_street_iregex (Union[Unset, None, str]):
        address_street_istartswith (Union[Unset, None, str]):
        address_street_search (Union[Unset, None, str]):
        address_id (Union[Unset, None, str]):
        address_id_in (Union[Unset, None, str]):
        address_id_isnull (Union[Unset, None, str]):
        assignee_email (Union[Unset, None, str]):
        assignee_email_icontains (Union[Unset, None, str]):
        assignee_email_iregex (Union[Unset, None, str]):
        assignee_email_isnull (Union[Unset, None, str]):
        assignee_email_istartswith (Union[Unset, None, str]):
        assignee_email_search (Union[Unset, None, str]):
        assignee_first_name (Union[Unset, None, str]):
        assignee_first_name_icontains (Union[Unset, None, str]):
        assignee_first_name_iregex (Union[Unset, None, str]):
        assignee_first_name_isnull (Union[Unset, None, str]):
        assignee_first_name_istartswith (Union[Unset, None, str]):
        assignee_first_name_search (Union[Unset, None, str]):
        assignee_last_name (Union[Unset, None, str]):
        assignee_last_name_icontains (Union[Unset, None, str]):
        assignee_last_name_iregex (Union[Unset, None, str]):
        assignee_last_name_isnull (Union[Unset, None, str]):
        assignee_last_name_istartswith (Union[Unset, None, str]):
        assignee_last_name_search (Union[Unset, None, str]):
        assignee_phone (Union[Unset, None, str]):
        assignee_phone_icontains (Union[Unset, None, str]):
        assignee_phone_iregex (Union[Unset, None, str]):
        assignee_phone_isnull (Union[Unset, None, str]):
        assignee_phone_istartswith (Union[Unset, None, str]):
        assignee_phone_search (Union[Unset, None, str]):
        assignee_id (Union[Unset, None, str]):
        assignee_id_in (Union[Unset, None, str]):
        assignee_id_isnull (Union[Unset, None, str]):
        assignee_proximity (Union[Unset, None, TaskExportsListAssigneeProximity]):
        assignee_proximity_in (Union[Unset, None, str]):
        category (Union[Unset, None, TaskExportsListCategory]):
        category_in (Union[Unset, None, str]):
        contact_company_icontains (Union[Unset, None, str]):
        contact_company_in (Union[Unset, None, str]):
        contact_company_iregex (Union[Unset, None, str]):
        contact_company_istartswith (Union[Unset, None, str]):
        contact_company_search (Union[Unset, None, str]):
        contact_email (Union[Unset, None, str]):
        contact_email_icontains (Union[Unset, None, str]):
        contact_email_in (Union[Unset, None, str]):
        contact_email_iregex (Union[Unset, None, str]):
        contact_email_istartswith (Union[Unset, None, str]):
        contact_email_search (Union[Unset, None, str]):
        contact_name (Union[Unset, None, str]):
        contact_name_icontains (Union[Unset, None, str]):
        contact_name_in (Union[Unset, None, str]):
        contact_name_iregex (Union[Unset, None, str]):
        contact_name_istartswith (Union[Unset, None, str]):
        contact_name_search (Union[Unset, None, str]):
        contact_notes (Union[Unset, None, str]):
        contact_notes_icontains (Union[Unset, None, str]):
        contact_notes_in (Union[Unset, None, str]):
        contact_notes_iregex (Union[Unset, None, str]):
        contact_notes_istartswith (Union[Unset, None, str]):
        contact_notes_search (Union[Unset, None, str]):
        contact_phone (Union[Unset, None, str]):
        contact_phone_icontains (Union[Unset, None, str]):
        contact_phone_in (Union[Unset, None, str]):
        contact_phone_iregex (Union[Unset, None, str]):
        contact_phone_istartswith (Union[Unset, None, str]):
        contact_phone_search (Union[Unset, None, str]):
        contact_id (Union[Unset, None, str]):
        contact_id_in (Union[Unset, None, str]):
        contact_id_isnull (Union[Unset, None, str]):
        created_by (Union[Unset, None, str]):
        created_by_in (Union[Unset, None, str]):
        created_by_isnull (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        description_icontains (Union[Unset, None, str]):
        description_iregex (Union[Unset, None, str]):
        description_istartswith (Union[Unset, None, str]):
        description_search (Union[Unset, None, str]):
        duration (Union[Unset, None, str]):
        duration_gt (Union[Unset, None, str]):
        duration_gte (Union[Unset, None, str]):
        duration_lt (Union[Unset, None, str]):
        duration_lte (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        external_id_in (Union[Unset, None, str]):
        external_id_iregex (Union[Unset, None, str]):
        external_id_isnull (Union[Unset, None, str]):
        external_id_istartswith (Union[Unset, None, str]):
        external_id_search (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):
        format_ (Union[Unset, None, TaskExportsListFormat]):  Default: TaskExportsListFormat.JSON.
        id (Union[Unset, None, str]):
        id_in (Union[Unset, None, str]):
        is_optimal (Union[Unset, None, str]):
        is_optimal_isnull (Union[Unset, None, str]):
        metadata_accepted_distance (Union[Unset, None, str]):
        metadata_accepted_distance_gt (Union[Unset, None, str]):
        metadata_accepted_distance_gte (Union[Unset, None, str]):
        metadata_accepted_distance_lt (Union[Unset, None, str]):
        metadata_accepted_distance_lte (Union[Unset, None, str]):
        metadata_accepted_duration (Union[Unset, None, str]):
        metadata_accepted_duration_gt (Union[Unset, None, str]):
        metadata_accepted_duration_gte (Union[Unset, None, str]):
        metadata_accepted_duration_lt (Union[Unset, None, str]):
        metadata_accepted_duration_lte (Union[Unset, None, str]):
        metadata_active_distance (Union[Unset, None, str]):
        metadata_active_distance_gt (Union[Unset, None, str]):
        metadata_active_distance_gte (Union[Unset, None, str]):
        metadata_active_distance_lt (Union[Unset, None, str]):
        metadata_active_distance_lte (Union[Unset, None, str]):
        metadata_active_duration (Union[Unset, None, str]):
        metadata_active_duration_gt (Union[Unset, None, str]):
        metadata_active_duration_gte (Union[Unset, None, str]):
        metadata_active_duration_lt (Union[Unset, None, str]):
        metadata_active_duration_lte (Union[Unset, None, str]):
        metadata_assigned_distance (Union[Unset, None, str]):
        metadata_assigned_distance_gt (Union[Unset, None, str]):
        metadata_assigned_distance_gte (Union[Unset, None, str]):
        metadata_assigned_distance_lt (Union[Unset, None, str]):
        metadata_assigned_distance_lte (Union[Unset, None, str]):
        metadata_assigned_duration (Union[Unset, None, str]):
        metadata_assigned_duration_gt (Union[Unset, None, str]):
        metadata_assigned_duration_gte (Union[Unset, None, str]):
        metadata_assigned_duration_lt (Union[Unset, None, str]):
        metadata_assigned_duration_lte (Union[Unset, None, str]):
        metadata_cancelled_distance (Union[Unset, None, str]):
        metadata_cancelled_distance_gt (Union[Unset, None, str]):
        metadata_cancelled_distance_gte (Union[Unset, None, str]):
        metadata_cancelled_distance_lt (Union[Unset, None, str]):
        metadata_cancelled_distance_lte (Union[Unset, None, str]):
        metadata_cancelled_duration (Union[Unset, None, str]):
        metadata_cancelled_duration_gt (Union[Unset, None, str]):
        metadata_cancelled_duration_gte (Union[Unset, None, str]):
        metadata_cancelled_duration_lt (Union[Unset, None, str]):
        metadata_cancelled_duration_lte (Union[Unset, None, str]):
        metadata_completed_distance (Union[Unset, None, str]):
        metadata_completed_distance_gt (Union[Unset, None, str]):
        metadata_completed_distance_gte (Union[Unset, None, str]):
        metadata_completed_distance_lt (Union[Unset, None, str]):
        metadata_completed_distance_lte (Union[Unset, None, str]):
        metadata_completed_duration (Union[Unset, None, str]):
        metadata_completed_duration_gt (Union[Unset, None, str]):
        metadata_completed_duration_gte (Union[Unset, None, str]):
        metadata_completed_duration_lt (Union[Unset, None, str]):
        metadata_completed_duration_lte (Union[Unset, None, str]):
        metadata_documents_count (Union[Unset, None, str]):
        metadata_documents_count_gt (Union[Unset, None, str]):
        metadata_documents_count_gte (Union[Unset, None, str]):
        metadata_documents_count_lt (Union[Unset, None, str]):
        metadata_documents_count_lte (Union[Unset, None, str]):
        metadata_events_count (Union[Unset, None, str]):
        metadata_events_count_gt (Union[Unset, None, str]):
        metadata_events_count_gte (Union[Unset, None, str]):
        metadata_events_count_lt (Union[Unset, None, str]):
        metadata_events_count_lte (Union[Unset, None, str]):
        metadata_failed_distance (Union[Unset, None, str]):
        metadata_failed_distance_gt (Union[Unset, None, str]):
        metadata_failed_distance_gte (Union[Unset, None, str]):
        metadata_failed_distance_lt (Union[Unset, None, str]):
        metadata_failed_distance_lte (Union[Unset, None, str]):
        metadata_failed_duration (Union[Unset, None, str]):
        metadata_failed_duration_gt (Union[Unset, None, str]):
        metadata_failed_duration_gte (Union[Unset, None, str]):
        metadata_failed_duration_lt (Union[Unset, None, str]):
        metadata_failed_duration_lte (Union[Unset, None, str]):
        metadata_forms_completed_count (Union[Unset, None, str]):
        metadata_forms_completed_count_gt (Union[Unset, None, str]):
        metadata_forms_completed_count_gte (Union[Unset, None, str]):
        metadata_forms_completed_count_lt (Union[Unset, None, str]):
        metadata_forms_completed_count_lte (Union[Unset, None, str]):
        metadata_forms_count (Union[Unset, None, str]):
        metadata_forms_count_gt (Union[Unset, None, str]):
        metadata_forms_count_gte (Union[Unset, None, str]):
        metadata_forms_count_lt (Union[Unset, None, str]):
        metadata_forms_count_lte (Union[Unset, None, str]):
        metadata_signatures_count (Union[Unset, None, str]):
        metadata_signatures_count_gt (Union[Unset, None, str]):
        metadata_signatures_count_gte (Union[Unset, None, str]):
        metadata_signatures_count_lt (Union[Unset, None, str]):
        metadata_signatures_count_lte (Union[Unset, None, str]):
        metadata_task_event_notes_count (Union[Unset, None, str]):
        metadata_task_event_notes_count_gt (Union[Unset, None, str]):
        metadata_task_event_notes_count_gte (Union[Unset, None, str]):
        metadata_task_event_notes_count_lt (Union[Unset, None, str]):
        metadata_task_event_notes_count_lte (Union[Unset, None, str]):
        metadata_transit_distance (Union[Unset, None, str]):
        metadata_transit_distance_gt (Union[Unset, None, str]):
        metadata_transit_distance_gte (Union[Unset, None, str]):
        metadata_transit_distance_lt (Union[Unset, None, str]):
        metadata_transit_distance_lte (Union[Unset, None, str]):
        metadata_transit_duration (Union[Unset, None, str]):
        metadata_transit_duration_gt (Union[Unset, None, str]):
        metadata_transit_duration_gte (Union[Unset, None, str]):
        metadata_transit_duration_lt (Union[Unset, None, str]):
        metadata_transit_duration_lte (Union[Unset, None, str]):
        metadata_unassigned_distance (Union[Unset, None, str]):
        metadata_unassigned_distance_gt (Union[Unset, None, str]):
        metadata_unassigned_distance_gte (Union[Unset, None, str]):
        metadata_unassigned_distance_lt (Union[Unset, None, str]):
        metadata_unassigned_distance_lte (Union[Unset, None, str]):
        metadata_unassigned_duration (Union[Unset, None, str]):
        metadata_unassigned_duration_gt (Union[Unset, None, str]):
        metadata_unassigned_duration_gte (Union[Unset, None, str]):
        metadata_unassigned_duration_lt (Union[Unset, None, str]):
        metadata_unassigned_duration_lte (Union[Unset, None, str]):
        order_auto_assign (Union[Unset, None, str]):
        order_created_by (Union[Unset, None, str]):
        order_created_by_in (Union[Unset, None, str]):
        order_created_by_isnull (Union[Unset, None, str]):
        order_external_id (Union[Unset, None, str]):
        order_external_id_icontains (Union[Unset, None, str]):
        order_external_id_in (Union[Unset, None, str]):
        order_external_id_iregex (Union[Unset, None, str]):
        order_external_id_isnull (Union[Unset, None, str]):
        order_external_id_istartswith (Union[Unset, None, str]):
        order_external_id_search (Union[Unset, None, str]):
        order_reference (Union[Unset, None, str]):
        order_reference_icontains (Union[Unset, None, str]):
        order_reference_in (Union[Unset, None, str]):
        order_reference_iregex (Union[Unset, None, str]):
        order_reference_istartswith (Union[Unset, None, str]):
        order_reference_search (Union[Unset, None, str]):
        order_id (Union[Unset, None, str]):
        order_id_in (Union[Unset, None, str]):
        order_id_isnull (Union[Unset, None, str]):
        orderer_id (Union[Unset, None, str]):
        orderer_id_in (Union[Unset, None, str]):
        orderer_id_isnull (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        owner_id (Union[Unset, None, str]):
        owner_id_in (Union[Unset, None, str]):
        owner_id_isnull (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        priority (Union[Unset, None, str]):
        priority_gt (Union[Unset, None, str]):
        priority_gte (Union[Unset, None, str]):
        priority_in (Union[Unset, None, str]):
        priority_lt (Union[Unset, None, str]):
        priority_lte (Union[Unset, None, str]):
        receiver_id (Union[Unset, None, str]):
        receiver_id_in (Union[Unset, None, str]):
        receiver_id_isnull (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        reference_icontains (Union[Unset, None, str]):
        reference_in (Union[Unset, None, str]):
        reference_iregex (Union[Unset, None, str]):
        reference_istartswith (Union[Unset, None, str]):
        reference_search (Union[Unset, None, str]):
        route_id (Union[Unset, None, str]):
        route_id_in (Union[Unset, None, str]):
        route_id_isnull (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, TaskExportsListState]):
        state_in (Union[Unset, None, str]):
        unassignee_id (Union[Unset, None, str]):
        unassignee_id_in (Union[Unset, None, str]):
        unassignee_id_isnull (Union[Unset, None, str]):

    Returns:
        Response[List[TaskExport]]
    """

    return (
        await asyncio_detailed(
            client=client,
            address_apartment_number=address_apartment_number,
            address_apartment_number_icontains=address_apartment_number_icontains,
            address_apartment_number_in=address_apartment_number_in,
            address_apartment_number_iregex=address_apartment_number_iregex,
            address_apartment_number_istartswith=address_apartment_number_istartswith,
            address_apartment_number_search=address_apartment_number_search,
            address_city=address_city,
            address_city_icontains=address_city_icontains,
            address_city_in=address_city_in,
            address_city_iregex=address_city_iregex,
            address_city_istartswith=address_city_istartswith,
            address_city_search=address_city_search,
            address_country=address_country,
            address_country_icontains=address_country_icontains,
            address_country_in=address_country_in,
            address_country_iregex=address_country_iregex,
            address_country_istartswith=address_country_istartswith,
            address_country_search=address_country_search,
            address_country_code=address_country_code,
            address_country_code_icontains=address_country_code_icontains,
            address_country_code_in=address_country_code_in,
            address_country_code_iregex=address_country_code_iregex,
            address_country_code_istartswith=address_country_code_istartswith,
            address_country_code_search=address_country_code_search,
            address_formatted_address=address_formatted_address,
            address_formatted_address_icontains=address_formatted_address_icontains,
            address_formatted_address_in=address_formatted_address_in,
            address_formatted_address_iregex=address_formatted_address_iregex,
            address_formatted_address_istartswith=address_formatted_address_istartswith,
            address_formatted_address_search=address_formatted_address_search,
            address_google_place_id=address_google_place_id,
            address_google_place_id_icontains=address_google_place_id_icontains,
            address_google_place_id_in=address_google_place_id_in,
            address_google_place_id_iregex=address_google_place_id_iregex,
            address_google_place_id_istartswith=address_google_place_id_istartswith,
            address_google_place_id_search=address_google_place_id_search,
            address_house_number=address_house_number,
            address_house_number_icontains=address_house_number_icontains,
            address_house_number_in=address_house_number_in,
            address_house_number_iregex=address_house_number_iregex,
            address_house_number_istartswith=address_house_number_istartswith,
            address_house_number_search=address_house_number_search,
            address_point_of_interest=address_point_of_interest,
            address_point_of_interest_icontains=address_point_of_interest_icontains,
            address_point_of_interest_in=address_point_of_interest_in,
            address_point_of_interest_iregex=address_point_of_interest_iregex,
            address_point_of_interest_istartswith=address_point_of_interest_istartswith,
            address_point_of_interest_search=address_point_of_interest_search,
            address_postal_code=address_postal_code,
            address_postal_code_icontains=address_postal_code_icontains,
            address_postal_code_in=address_postal_code_in,
            address_postal_code_iregex=address_postal_code_iregex,
            address_postal_code_istartswith=address_postal_code_istartswith,
            address_postal_code_search=address_postal_code_search,
            address_raw_address=address_raw_address,
            address_raw_address_icontains=address_raw_address_icontains,
            address_raw_address_in=address_raw_address_in,
            address_raw_address_iregex=address_raw_address_iregex,
            address_raw_address_istartswith=address_raw_address_istartswith,
            address_raw_address_search=address_raw_address_search,
            address_state=address_state,
            address_state_icontains=address_state_icontains,
            address_state_in=address_state_in,
            address_state_iregex=address_state_iregex,
            address_state_istartswith=address_state_istartswith,
            address_state_search=address_state_search,
            address_street=address_street,
            address_street_icontains=address_street_icontains,
            address_street_in=address_street_in,
            address_street_iregex=address_street_iregex,
            address_street_istartswith=address_street_istartswith,
            address_street_search=address_street_search,
            address_id=address_id,
            address_id_in=address_id_in,
            address_id_isnull=address_id_isnull,
            assignee_email=assignee_email,
            assignee_email_icontains=assignee_email_icontains,
            assignee_email_iregex=assignee_email_iregex,
            assignee_email_isnull=assignee_email_isnull,
            assignee_email_istartswith=assignee_email_istartswith,
            assignee_email_search=assignee_email_search,
            assignee_first_name=assignee_first_name,
            assignee_first_name_icontains=assignee_first_name_icontains,
            assignee_first_name_iregex=assignee_first_name_iregex,
            assignee_first_name_isnull=assignee_first_name_isnull,
            assignee_first_name_istartswith=assignee_first_name_istartswith,
            assignee_first_name_search=assignee_first_name_search,
            assignee_last_name=assignee_last_name,
            assignee_last_name_icontains=assignee_last_name_icontains,
            assignee_last_name_iregex=assignee_last_name_iregex,
            assignee_last_name_isnull=assignee_last_name_isnull,
            assignee_last_name_istartswith=assignee_last_name_istartswith,
            assignee_last_name_search=assignee_last_name_search,
            assignee_phone=assignee_phone,
            assignee_phone_icontains=assignee_phone_icontains,
            assignee_phone_iregex=assignee_phone_iregex,
            assignee_phone_isnull=assignee_phone_isnull,
            assignee_phone_istartswith=assignee_phone_istartswith,
            assignee_phone_search=assignee_phone_search,
            assignee_id=assignee_id,
            assignee_id_in=assignee_id_in,
            assignee_id_isnull=assignee_id_isnull,
            assignee_proximity=assignee_proximity,
            assignee_proximity_in=assignee_proximity_in,
            category=category,
            category_in=category_in,
            contact_company_icontains=contact_company_icontains,
            contact_company_in=contact_company_in,
            contact_company_iregex=contact_company_iregex,
            contact_company_istartswith=contact_company_istartswith,
            contact_company_search=contact_company_search,
            contact_email=contact_email,
            contact_email_icontains=contact_email_icontains,
            contact_email_in=contact_email_in,
            contact_email_iregex=contact_email_iregex,
            contact_email_istartswith=contact_email_istartswith,
            contact_email_search=contact_email_search,
            contact_name=contact_name,
            contact_name_icontains=contact_name_icontains,
            contact_name_in=contact_name_in,
            contact_name_iregex=contact_name_iregex,
            contact_name_istartswith=contact_name_istartswith,
            contact_name_search=contact_name_search,
            contact_notes=contact_notes,
            contact_notes_icontains=contact_notes_icontains,
            contact_notes_in=contact_notes_in,
            contact_notes_iregex=contact_notes_iregex,
            contact_notes_istartswith=contact_notes_istartswith,
            contact_notes_search=contact_notes_search,
            contact_phone=contact_phone,
            contact_phone_icontains=contact_phone_icontains,
            contact_phone_in=contact_phone_in,
            contact_phone_iregex=contact_phone_iregex,
            contact_phone_istartswith=contact_phone_istartswith,
            contact_phone_search=contact_phone_search,
            contact_id=contact_id,
            contact_id_in=contact_id_in,
            contact_id_isnull=contact_id_isnull,
            created_by=created_by,
            created_by_in=created_by_in,
            created_by_isnull=created_by_isnull,
            description=description,
            description_icontains=description_icontains,
            description_iregex=description_iregex,
            description_istartswith=description_istartswith,
            description_search=description_search,
            duration=duration,
            duration_gt=duration_gt,
            duration_gte=duration_gte,
            duration_lt=duration_lt,
            duration_lte=duration_lte,
            external_id=external_id,
            external_id_icontains=external_id_icontains,
            external_id_in=external_id_in,
            external_id_iregex=external_id_iregex,
            external_id_isnull=external_id_isnull,
            external_id_istartswith=external_id_istartswith,
            external_id_search=external_id_search,
            fields=fields,
            format_=format_,
            id=id,
            id_in=id_in,
            is_optimal=is_optimal,
            is_optimal_isnull=is_optimal_isnull,
            metadata_accepted_distance=metadata_accepted_distance,
            metadata_accepted_distance_gt=metadata_accepted_distance_gt,
            metadata_accepted_distance_gte=metadata_accepted_distance_gte,
            metadata_accepted_distance_lt=metadata_accepted_distance_lt,
            metadata_accepted_distance_lte=metadata_accepted_distance_lte,
            metadata_accepted_duration=metadata_accepted_duration,
            metadata_accepted_duration_gt=metadata_accepted_duration_gt,
            metadata_accepted_duration_gte=metadata_accepted_duration_gte,
            metadata_accepted_duration_lt=metadata_accepted_duration_lt,
            metadata_accepted_duration_lte=metadata_accepted_duration_lte,
            metadata_active_distance=metadata_active_distance,
            metadata_active_distance_gt=metadata_active_distance_gt,
            metadata_active_distance_gte=metadata_active_distance_gte,
            metadata_active_distance_lt=metadata_active_distance_lt,
            metadata_active_distance_lte=metadata_active_distance_lte,
            metadata_active_duration=metadata_active_duration,
            metadata_active_duration_gt=metadata_active_duration_gt,
            metadata_active_duration_gte=metadata_active_duration_gte,
            metadata_active_duration_lt=metadata_active_duration_lt,
            metadata_active_duration_lte=metadata_active_duration_lte,
            metadata_assigned_distance=metadata_assigned_distance,
            metadata_assigned_distance_gt=metadata_assigned_distance_gt,
            metadata_assigned_distance_gte=metadata_assigned_distance_gte,
            metadata_assigned_distance_lt=metadata_assigned_distance_lt,
            metadata_assigned_distance_lte=metadata_assigned_distance_lte,
            metadata_assigned_duration=metadata_assigned_duration,
            metadata_assigned_duration_gt=metadata_assigned_duration_gt,
            metadata_assigned_duration_gte=metadata_assigned_duration_gte,
            metadata_assigned_duration_lt=metadata_assigned_duration_lt,
            metadata_assigned_duration_lte=metadata_assigned_duration_lte,
            metadata_cancelled_distance=metadata_cancelled_distance,
            metadata_cancelled_distance_gt=metadata_cancelled_distance_gt,
            metadata_cancelled_distance_gte=metadata_cancelled_distance_gte,
            metadata_cancelled_distance_lt=metadata_cancelled_distance_lt,
            metadata_cancelled_distance_lte=metadata_cancelled_distance_lte,
            metadata_cancelled_duration=metadata_cancelled_duration,
            metadata_cancelled_duration_gt=metadata_cancelled_duration_gt,
            metadata_cancelled_duration_gte=metadata_cancelled_duration_gte,
            metadata_cancelled_duration_lt=metadata_cancelled_duration_lt,
            metadata_cancelled_duration_lte=metadata_cancelled_duration_lte,
            metadata_completed_distance=metadata_completed_distance,
            metadata_completed_distance_gt=metadata_completed_distance_gt,
            metadata_completed_distance_gte=metadata_completed_distance_gte,
            metadata_completed_distance_lt=metadata_completed_distance_lt,
            metadata_completed_distance_lte=metadata_completed_distance_lte,
            metadata_completed_duration=metadata_completed_duration,
            metadata_completed_duration_gt=metadata_completed_duration_gt,
            metadata_completed_duration_gte=metadata_completed_duration_gte,
            metadata_completed_duration_lt=metadata_completed_duration_lt,
            metadata_completed_duration_lte=metadata_completed_duration_lte,
            metadata_documents_count=metadata_documents_count,
            metadata_documents_count_gt=metadata_documents_count_gt,
            metadata_documents_count_gte=metadata_documents_count_gte,
            metadata_documents_count_lt=metadata_documents_count_lt,
            metadata_documents_count_lte=metadata_documents_count_lte,
            metadata_events_count=metadata_events_count,
            metadata_events_count_gt=metadata_events_count_gt,
            metadata_events_count_gte=metadata_events_count_gte,
            metadata_events_count_lt=metadata_events_count_lt,
            metadata_events_count_lte=metadata_events_count_lte,
            metadata_failed_distance=metadata_failed_distance,
            metadata_failed_distance_gt=metadata_failed_distance_gt,
            metadata_failed_distance_gte=metadata_failed_distance_gte,
            metadata_failed_distance_lt=metadata_failed_distance_lt,
            metadata_failed_distance_lte=metadata_failed_distance_lte,
            metadata_failed_duration=metadata_failed_duration,
            metadata_failed_duration_gt=metadata_failed_duration_gt,
            metadata_failed_duration_gte=metadata_failed_duration_gte,
            metadata_failed_duration_lt=metadata_failed_duration_lt,
            metadata_failed_duration_lte=metadata_failed_duration_lte,
            metadata_forms_completed_count=metadata_forms_completed_count,
            metadata_forms_completed_count_gt=metadata_forms_completed_count_gt,
            metadata_forms_completed_count_gte=metadata_forms_completed_count_gte,
            metadata_forms_completed_count_lt=metadata_forms_completed_count_lt,
            metadata_forms_completed_count_lte=metadata_forms_completed_count_lte,
            metadata_forms_count=metadata_forms_count,
            metadata_forms_count_gt=metadata_forms_count_gt,
            metadata_forms_count_gte=metadata_forms_count_gte,
            metadata_forms_count_lt=metadata_forms_count_lt,
            metadata_forms_count_lte=metadata_forms_count_lte,
            metadata_signatures_count=metadata_signatures_count,
            metadata_signatures_count_gt=metadata_signatures_count_gt,
            metadata_signatures_count_gte=metadata_signatures_count_gte,
            metadata_signatures_count_lt=metadata_signatures_count_lt,
            metadata_signatures_count_lte=metadata_signatures_count_lte,
            metadata_task_event_notes_count=metadata_task_event_notes_count,
            metadata_task_event_notes_count_gt=metadata_task_event_notes_count_gt,
            metadata_task_event_notes_count_gte=metadata_task_event_notes_count_gte,
            metadata_task_event_notes_count_lt=metadata_task_event_notes_count_lt,
            metadata_task_event_notes_count_lte=metadata_task_event_notes_count_lte,
            metadata_transit_distance=metadata_transit_distance,
            metadata_transit_distance_gt=metadata_transit_distance_gt,
            metadata_transit_distance_gte=metadata_transit_distance_gte,
            metadata_transit_distance_lt=metadata_transit_distance_lt,
            metadata_transit_distance_lte=metadata_transit_distance_lte,
            metadata_transit_duration=metadata_transit_duration,
            metadata_transit_duration_gt=metadata_transit_duration_gt,
            metadata_transit_duration_gte=metadata_transit_duration_gte,
            metadata_transit_duration_lt=metadata_transit_duration_lt,
            metadata_transit_duration_lte=metadata_transit_duration_lte,
            metadata_unassigned_distance=metadata_unassigned_distance,
            metadata_unassigned_distance_gt=metadata_unassigned_distance_gt,
            metadata_unassigned_distance_gte=metadata_unassigned_distance_gte,
            metadata_unassigned_distance_lt=metadata_unassigned_distance_lt,
            metadata_unassigned_distance_lte=metadata_unassigned_distance_lte,
            metadata_unassigned_duration=metadata_unassigned_duration,
            metadata_unassigned_duration_gt=metadata_unassigned_duration_gt,
            metadata_unassigned_duration_gte=metadata_unassigned_duration_gte,
            metadata_unassigned_duration_lt=metadata_unassigned_duration_lt,
            metadata_unassigned_duration_lte=metadata_unassigned_duration_lte,
            order_auto_assign=order_auto_assign,
            order_created_by=order_created_by,
            order_created_by_in=order_created_by_in,
            order_created_by_isnull=order_created_by_isnull,
            order_external_id=order_external_id,
            order_external_id_icontains=order_external_id_icontains,
            order_external_id_in=order_external_id_in,
            order_external_id_iregex=order_external_id_iregex,
            order_external_id_isnull=order_external_id_isnull,
            order_external_id_istartswith=order_external_id_istartswith,
            order_external_id_search=order_external_id_search,
            order_reference=order_reference,
            order_reference_icontains=order_reference_icontains,
            order_reference_in=order_reference_in,
            order_reference_iregex=order_reference_iregex,
            order_reference_istartswith=order_reference_istartswith,
            order_reference_search=order_reference_search,
            order_id=order_id,
            order_id_in=order_id_in,
            order_id_isnull=order_id_isnull,
            orderer_id=orderer_id,
            orderer_id_in=orderer_id_in,
            orderer_id_isnull=orderer_id_isnull,
            ordering=ordering,
            owner_id=owner_id,
            owner_id_in=owner_id_in,
            owner_id_isnull=owner_id_isnull,
            page=page,
            page_size=page_size,
            priority=priority,
            priority_gt=priority_gt,
            priority_gte=priority_gte,
            priority_in=priority_in,
            priority_lt=priority_lt,
            priority_lte=priority_lte,
            receiver_id=receiver_id,
            receiver_id_in=receiver_id_in,
            receiver_id_isnull=receiver_id_isnull,
            reference=reference,
            reference_icontains=reference_icontains,
            reference_in=reference_in,
            reference_iregex=reference_iregex,
            reference_istartswith=reference_istartswith,
            reference_search=reference_search,
            route_id=route_id,
            route_id_in=route_id_in,
            route_id_isnull=route_id_isnull,
            search=search,
            state=state,
            state_in=state_in,
            unassignee_id=unassignee_id,
            unassignee_id_in=unassignee_id_in,
            unassignee_id_isnull=unassignee_id_isnull,
        )
    ).parsed

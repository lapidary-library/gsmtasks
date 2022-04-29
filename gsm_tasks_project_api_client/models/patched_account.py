import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.account_billing_method_enum import AccountBillingMethodEnum
from ..models.blank_enum import BlankEnum
from ..models.country_code_enum import CountryCodeEnum
from ..models.distance_units_enum import DistanceUnitsEnum
from ..models.feature_address_autosuggest_provider_enum import FeatureAddressAutosuggestProviderEnum
from ..models.feature_geocoding_country_code_enum import FeatureGeocodingCountryCodeEnum
from ..models.language_enum import LanguageEnum
from ..models.nested_address import NestedAddress
from ..models.optimization_objective_enum import OptimizationObjectiveEnum
from ..models.patched_account_default_task_duration import PatchedAccountDefaultTaskDuration
from ..models.patched_account_rotate_assignee import PatchedAccountRotateAssignee
from ..models.patched_account_task_expiry_duration import PatchedAccountTaskExpiryDuration
from ..models.task_expiry_state_enum import TaskExpiryStateEnum
from ..models.timezone_enum import TimezoneEnum
from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAccount")


@attr.s(auto_attribs=True)
class PatchedAccount:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        name (Union[Unset, str]):
        type (Union[BlankEnum, TypeEnum, Unset]):
        slug (Union[Unset, str]):
        owner (Union[Unset, str]):
        email (Union[Unset, str]):
        notification_emails (Union[Unset, List[str]]):
        review_emails (Union[Unset, List[str]]):
        website (Union[Unset, str]):
        registry_code (Union[Unset, str]):
        vatin (Union[Unset, str]):
        language (Union[Unset, LanguageEnum]):
        timezone (Union[Unset, TimezoneEnum]):
        country_code (Union[BlankEnum, CountryCodeEnum, Unset]):
        address (Union[Unset, None, NestedAddress]):
        phone_prefix (Union[Unset, str]):
        distance_units (Union[Unset, DistanceUnitsEnum]):
        task_duration (Union[Unset, PatchedAccountDefaultTaskDuration]):
        task_expiry_duration (Union[Unset, None, PatchedAccountTaskExpiryDuration]):
        task_expiry_state (Union[Unset, TaskExpiryStateEnum]):
        assignee_proximity_radius (Union[Unset, int]):
        optimize_after_create (Union[Unset, bool]):
        optimize_when_on_duty (Union[Unset, bool]):
        optimization_objective (Union[Unset, OptimizationObjectiveEnum]):
        reference_autogenerate (Union[Unset, bool]):
        reference_offset (Union[Unset, int]):
        reference_prefix (Union[Unset, str]):
        reference_length (Union[Unset, int]):
        feature_show_unassigned_to_workers (Union[Unset, bool]):
        feature_task_created_sound (Union[Unset, bool]):
        feature_change_task_account (Union[Unset, bool]):
        feature_show_tutorial (Union[Unset, bool]):
        feature_navigation_app_selection (Union[Unset, bool]):
        feature_navigation_use_address (Union[Unset, bool]):
        feature_task_accept (Union[Unset, bool]):
        feature_task_reject (Union[Unset, bool]):
        feature_app_task_search (Union[Unset, bool]):
        feature_address_autosuggest_provider (Union[Unset, FeatureAddressAutosuggestProviderEnum]):
        feature_geocoding_country_code (Union[BlankEnum, FeatureGeocodingCountryCodeEnum, Unset]): Limit geocoding to
            the selected country.
        feature_document_signing (Union[Unset, bool]): Allow choosing documents to sign.
        feature_tracker_reviews_allowed (Union[Unset, bool]):
        auto_assign_orders (Union[Unset, bool]):
        auto_assign_max_tasks (Union[Unset, None, int]): How many tasks can be auto assigned to a worker?
        auto_assign_max_distance (Union[Unset, None, int]): How far can a task be auto assigned to a worker in meters?
        auto_assign_time_before (Union[Unset, None, str]):
        auto_assign_rotate (Union[Unset, None, PatchedAccountRotateAssignee]): Time after non-accepted task assignees
            will be rotated. Leave empty in case the orders should not be rotated
        auto_assign_optimize (Union[Unset, bool]): Check the optimizer results before assignment?
        dashboard_task_template (Union[Unset, str]):
        dashboard_worker_limit (Union[Unset, int]):
        managers (Union[Unset, str]):
        workers (Union[Unset, str]):
        stripe_customer_id (Union[Unset, str]):
        stripe_payment_method_id (Union[Unset, str]): Reflects current default payment method. For reference only.
        billing_method (Union[Unset, AccountBillingMethodEnum]):
        billing_name (Union[Unset, str]):
        billing_company (Union[Unset, str]):
        billing_address (Union[Unset, str]):
        billing_country (Union[Unset, str]):
        billing_email (Union[Unset, str]):
        billing_phone (Union[Unset, str]):
        billing_vatin (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[BlankEnum, TypeEnum, Unset] = UNSET
    slug: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    notification_emails: Union[Unset, List[str]] = UNSET
    review_emails: Union[Unset, List[str]] = UNSET
    website: Union[Unset, str] = UNSET
    registry_code: Union[Unset, str] = UNSET
    vatin: Union[Unset, str] = UNSET
    language: Union[Unset, LanguageEnum] = UNSET
    timezone: Union[Unset, TimezoneEnum] = UNSET
    country_code: Union[BlankEnum, CountryCodeEnum, Unset] = UNSET
    address: Union[Unset, None, NestedAddress] = UNSET
    phone_prefix: Union[Unset, str] = UNSET
    distance_units: Union[Unset, DistanceUnitsEnum] = UNSET
    task_duration: Union[Unset, PatchedAccountDefaultTaskDuration] = UNSET
    task_expiry_duration: Union[Unset, None, PatchedAccountTaskExpiryDuration] = UNSET
    task_expiry_state: Union[Unset, TaskExpiryStateEnum] = UNSET
    assignee_proximity_radius: Union[Unset, int] = UNSET
    optimize_after_create: Union[Unset, bool] = UNSET
    optimize_when_on_duty: Union[Unset, bool] = UNSET
    optimization_objective: Union[Unset, OptimizationObjectiveEnum] = UNSET
    reference_autogenerate: Union[Unset, bool] = UNSET
    reference_offset: Union[Unset, int] = UNSET
    reference_prefix: Union[Unset, str] = UNSET
    reference_length: Union[Unset, int] = UNSET
    feature_show_unassigned_to_workers: Union[Unset, bool] = UNSET
    feature_task_created_sound: Union[Unset, bool] = UNSET
    feature_change_task_account: Union[Unset, bool] = UNSET
    feature_show_tutorial: Union[Unset, bool] = UNSET
    feature_navigation_app_selection: Union[Unset, bool] = UNSET
    feature_navigation_use_address: Union[Unset, bool] = UNSET
    feature_task_accept: Union[Unset, bool] = UNSET
    feature_task_reject: Union[Unset, bool] = UNSET
    feature_app_task_search: Union[Unset, bool] = UNSET
    feature_address_autosuggest_provider: Union[Unset, FeatureAddressAutosuggestProviderEnum] = UNSET
    feature_geocoding_country_code: Union[BlankEnum, FeatureGeocodingCountryCodeEnum, Unset] = UNSET
    feature_document_signing: Union[Unset, bool] = UNSET
    feature_tracker_reviews_allowed: Union[Unset, bool] = UNSET
    auto_assign_orders: Union[Unset, bool] = UNSET
    auto_assign_max_tasks: Union[Unset, None, int] = UNSET
    auto_assign_max_distance: Union[Unset, None, int] = UNSET
    auto_assign_time_before: Union[Unset, None, str] = UNSET
    auto_assign_rotate: Union[Unset, None, PatchedAccountRotateAssignee] = UNSET
    auto_assign_optimize: Union[Unset, bool] = UNSET
    dashboard_task_template: Union[Unset, str] = UNSET
    dashboard_worker_limit: Union[Unset, int] = UNSET
    managers: Union[Unset, str] = UNSET
    workers: Union[Unset, str] = UNSET
    stripe_customer_id: Union[Unset, str] = UNSET
    stripe_payment_method_id: Union[Unset, str] = UNSET
    billing_method: Union[Unset, AccountBillingMethodEnum] = UNSET
    billing_name: Union[Unset, str] = UNSET
    billing_company: Union[Unset, str] = UNSET
    billing_address: Union[Unset, str] = UNSET
    billing_country: Union[Unset, str] = UNSET
    billing_email: Union[Unset, str] = UNSET
    billing_phone: Union[Unset, str] = UNSET
    billing_vatin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        name = self.name
        type: Union[Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET

        elif isinstance(self.type, TypeEnum):
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.value

        else:
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.value

        slug = self.slug
        owner = self.owner
        email = self.email
        notification_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notification_emails, Unset):
            notification_emails = self.notification_emails

        review_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.review_emails, Unset):
            review_emails = self.review_emails

        website = self.website
        registry_code = self.registry_code
        vatin = self.vatin
        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        timezone: Union[Unset, str] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.value

        country_code: Union[Unset, str]
        if isinstance(self.country_code, Unset):
            country_code = UNSET

        elif isinstance(self.country_code, CountryCodeEnum):
            country_code = UNSET
            if not isinstance(self.country_code, Unset):
                country_code = self.country_code.value

        else:
            country_code = UNSET
            if not isinstance(self.country_code, Unset):
                country_code = self.country_code.value

        address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict() if self.address else None

        phone_prefix = self.phone_prefix
        distance_units: Union[Unset, str] = UNSET
        if not isinstance(self.distance_units, Unset):
            distance_units = self.distance_units.value

        task_duration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.task_duration, Unset):
            task_duration = self.task_duration.to_dict()

        task_expiry_duration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.task_expiry_duration, Unset):
            task_expiry_duration = self.task_expiry_duration.to_dict() if self.task_expiry_duration else None

        task_expiry_state: Union[Unset, str] = UNSET
        if not isinstance(self.task_expiry_state, Unset):
            task_expiry_state = self.task_expiry_state.value

        assignee_proximity_radius = self.assignee_proximity_radius
        optimize_after_create = self.optimize_after_create
        optimize_when_on_duty = self.optimize_when_on_duty
        optimization_objective: Union[Unset, str] = UNSET
        if not isinstance(self.optimization_objective, Unset):
            optimization_objective = self.optimization_objective.value

        reference_autogenerate = self.reference_autogenerate
        reference_offset = self.reference_offset
        reference_prefix = self.reference_prefix
        reference_length = self.reference_length
        feature_show_unassigned_to_workers = self.feature_show_unassigned_to_workers
        feature_task_created_sound = self.feature_task_created_sound
        feature_change_task_account = self.feature_change_task_account
        feature_show_tutorial = self.feature_show_tutorial
        feature_navigation_app_selection = self.feature_navigation_app_selection
        feature_navigation_use_address = self.feature_navigation_use_address
        feature_task_accept = self.feature_task_accept
        feature_task_reject = self.feature_task_reject
        feature_app_task_search = self.feature_app_task_search
        feature_address_autosuggest_provider: Union[Unset, str] = UNSET
        if not isinstance(self.feature_address_autosuggest_provider, Unset):
            feature_address_autosuggest_provider = self.feature_address_autosuggest_provider.value

        feature_geocoding_country_code: Union[Unset, str]
        if isinstance(self.feature_geocoding_country_code, Unset):
            feature_geocoding_country_code = UNSET

        elif isinstance(self.feature_geocoding_country_code, FeatureGeocodingCountryCodeEnum):
            feature_geocoding_country_code = UNSET
            if not isinstance(self.feature_geocoding_country_code, Unset):
                feature_geocoding_country_code = self.feature_geocoding_country_code.value

        else:
            feature_geocoding_country_code = UNSET
            if not isinstance(self.feature_geocoding_country_code, Unset):
                feature_geocoding_country_code = self.feature_geocoding_country_code.value

        feature_document_signing = self.feature_document_signing
        feature_tracker_reviews_allowed = self.feature_tracker_reviews_allowed
        auto_assign_orders = self.auto_assign_orders
        auto_assign_max_tasks = self.auto_assign_max_tasks
        auto_assign_max_distance = self.auto_assign_max_distance
        auto_assign_time_before = self.auto_assign_time_before
        auto_assign_rotate: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_assign_rotate, Unset):
            auto_assign_rotate = self.auto_assign_rotate.to_dict() if self.auto_assign_rotate else None

        auto_assign_optimize = self.auto_assign_optimize
        dashboard_task_template = self.dashboard_task_template
        dashboard_worker_limit = self.dashboard_worker_limit
        managers = self.managers
        workers = self.workers
        stripe_customer_id = self.stripe_customer_id
        stripe_payment_method_id = self.stripe_payment_method_id
        billing_method: Union[Unset, str] = UNSET
        if not isinstance(self.billing_method, Unset):
            billing_method = self.billing_method.value

        billing_name = self.billing_name
        billing_company = self.billing_company
        billing_address = self.billing_address
        billing_country = self.billing_country
        billing_email = self.billing_email
        billing_phone = self.billing_phone
        billing_vatin = self.billing_vatin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if slug is not UNSET:
            field_dict["slug"] = slug
        if owner is not UNSET:
            field_dict["owner"] = owner
        if email is not UNSET:
            field_dict["email"] = email
        if notification_emails is not UNSET:
            field_dict["notification_emails"] = notification_emails
        if review_emails is not UNSET:
            field_dict["review_emails"] = review_emails
        if website is not UNSET:
            field_dict["website"] = website
        if registry_code is not UNSET:
            field_dict["registry_code"] = registry_code
        if vatin is not UNSET:
            field_dict["vatin"] = vatin
        if language is not UNSET:
            field_dict["language"] = language
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if address is not UNSET:
            field_dict["address"] = address
        if phone_prefix is not UNSET:
            field_dict["phone_prefix"] = phone_prefix
        if distance_units is not UNSET:
            field_dict["distance_units"] = distance_units
        if task_duration is not UNSET:
            field_dict["task_duration"] = task_duration
        if task_expiry_duration is not UNSET:
            field_dict["task_expiry_duration"] = task_expiry_duration
        if task_expiry_state is not UNSET:
            field_dict["task_expiry_state"] = task_expiry_state
        if assignee_proximity_radius is not UNSET:
            field_dict["assignee_proximity_radius"] = assignee_proximity_radius
        if optimize_after_create is not UNSET:
            field_dict["optimize_after_create"] = optimize_after_create
        if optimize_when_on_duty is not UNSET:
            field_dict["optimize_when_on_duty"] = optimize_when_on_duty
        if optimization_objective is not UNSET:
            field_dict["optimization_objective"] = optimization_objective
        if reference_autogenerate is not UNSET:
            field_dict["reference_autogenerate"] = reference_autogenerate
        if reference_offset is not UNSET:
            field_dict["reference_offset"] = reference_offset
        if reference_prefix is not UNSET:
            field_dict["reference_prefix"] = reference_prefix
        if reference_length is not UNSET:
            field_dict["reference_length"] = reference_length
        if feature_show_unassigned_to_workers is not UNSET:
            field_dict["feature_show_unassigned_to_workers"] = feature_show_unassigned_to_workers
        if feature_task_created_sound is not UNSET:
            field_dict["feature_task_created_sound"] = feature_task_created_sound
        if feature_change_task_account is not UNSET:
            field_dict["feature_change_task_account"] = feature_change_task_account
        if feature_show_tutorial is not UNSET:
            field_dict["feature_show_tutorial"] = feature_show_tutorial
        if feature_navigation_app_selection is not UNSET:
            field_dict["feature_navigation_app_selection"] = feature_navigation_app_selection
        if feature_navigation_use_address is not UNSET:
            field_dict["feature_navigation_use_address"] = feature_navigation_use_address
        if feature_task_accept is not UNSET:
            field_dict["feature_task_accept"] = feature_task_accept
        if feature_task_reject is not UNSET:
            field_dict["feature_task_reject"] = feature_task_reject
        if feature_app_task_search is not UNSET:
            field_dict["feature_app_task_search"] = feature_app_task_search
        if feature_address_autosuggest_provider is not UNSET:
            field_dict["feature_address_autosuggest_provider"] = feature_address_autosuggest_provider
        if feature_geocoding_country_code is not UNSET:
            field_dict["feature_geocoding_country_code"] = feature_geocoding_country_code
        if feature_document_signing is not UNSET:
            field_dict["feature_document_signing"] = feature_document_signing
        if feature_tracker_reviews_allowed is not UNSET:
            field_dict["feature_tracker_reviews_allowed"] = feature_tracker_reviews_allowed
        if auto_assign_orders is not UNSET:
            field_dict["auto_assign_orders"] = auto_assign_orders
        if auto_assign_max_tasks is not UNSET:
            field_dict["auto_assign_max_tasks"] = auto_assign_max_tasks
        if auto_assign_max_distance is not UNSET:
            field_dict["auto_assign_max_distance"] = auto_assign_max_distance
        if auto_assign_time_before is not UNSET:
            field_dict["auto_assign_time_before"] = auto_assign_time_before
        if auto_assign_rotate is not UNSET:
            field_dict["auto_assign_rotate"] = auto_assign_rotate
        if auto_assign_optimize is not UNSET:
            field_dict["auto_assign_optimize"] = auto_assign_optimize
        if dashboard_task_template is not UNSET:
            field_dict["dashboard_task_template"] = dashboard_task_template
        if dashboard_worker_limit is not UNSET:
            field_dict["dashboard_worker_limit"] = dashboard_worker_limit
        if managers is not UNSET:
            field_dict["managers"] = managers
        if workers is not UNSET:
            field_dict["workers"] = workers
        if stripe_customer_id is not UNSET:
            field_dict["stripe_customer_id"] = stripe_customer_id
        if stripe_payment_method_id is not UNSET:
            field_dict["stripe_payment_method_id"] = stripe_payment_method_id
        if billing_method is not UNSET:
            field_dict["billing_method"] = billing_method
        if billing_name is not UNSET:
            field_dict["billing_name"] = billing_name
        if billing_company is not UNSET:
            field_dict["billing_company"] = billing_company
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if billing_country is not UNSET:
            field_dict["billing_country"] = billing_country
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email
        if billing_phone is not UNSET:
            field_dict["billing_phone"] = billing_phone
        if billing_vatin is not UNSET:
            field_dict["billing_vatin"] = billing_vatin

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        type: Union[Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET

        elif isinstance(self.type, TypeEnum):
            type = UNSET
            if not isinstance(self.type, Unset):
                type = (None, str(self.type.value).encode(), "text/plain")

        else:
            type = UNSET
            if not isinstance(self.type, Unset):
                type = (None, str(self.type.value).encode(), "text/plain")

        slug = self.slug if isinstance(self.slug, Unset) else (None, str(self.slug).encode(), "text/plain")
        owner = self.owner if isinstance(self.owner, Unset) else (None, str(self.owner).encode(), "text/plain")
        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")
        notification_emails: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.notification_emails, Unset):
            _temp_notification_emails = self.notification_emails
            notification_emails = (None, json.dumps(_temp_notification_emails).encode(), "application/json")

        review_emails: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.review_emails, Unset):
            _temp_review_emails = self.review_emails
            review_emails = (None, json.dumps(_temp_review_emails).encode(), "application/json")

        website = self.website if isinstance(self.website, Unset) else (None, str(self.website).encode(), "text/plain")
        registry_code = (
            self.registry_code
            if isinstance(self.registry_code, Unset)
            else (None, str(self.registry_code).encode(), "text/plain")
        )
        vatin = self.vatin if isinstance(self.vatin, Unset) else (None, str(self.vatin).encode(), "text/plain")
        language: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.language, Unset):
            language = (None, str(self.language.value).encode(), "text/plain")

        timezone: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = (None, str(self.timezone.value).encode(), "text/plain")

        country_code: Union[Unset, str]
        if isinstance(self.country_code, Unset):
            country_code = UNSET

        elif isinstance(self.country_code, CountryCodeEnum):
            country_code = UNSET
            if not isinstance(self.country_code, Unset):
                country_code = (None, str(self.country_code.value).encode(), "text/plain")

        else:
            country_code = UNSET
            if not isinstance(self.country_code, Unset):
                country_code = (None, str(self.country_code.value).encode(), "text/plain")

        address: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.address, Unset):
            address = (None, json.dumps(self.address.to_dict()).encode(), "application/json") if self.address else None

        phone_prefix = (
            self.phone_prefix
            if isinstance(self.phone_prefix, Unset)
            else (None, str(self.phone_prefix).encode(), "text/plain")
        )
        distance_units: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.distance_units, Unset):
            distance_units = (None, str(self.distance_units.value).encode(), "text/plain")

        task_duration: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.task_duration, Unset):
            task_duration = (None, json.dumps(self.task_duration.to_dict()).encode(), "application/json")

        task_expiry_duration: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.task_expiry_duration, Unset):
            task_expiry_duration = (
                (None, json.dumps(self.task_expiry_duration.to_dict()).encode(), "application/json")
                if self.task_expiry_duration
                else None
            )

        task_expiry_state: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.task_expiry_state, Unset):
            task_expiry_state = (None, str(self.task_expiry_state.value).encode(), "text/plain")

        assignee_proximity_radius = (
            self.assignee_proximity_radius
            if isinstance(self.assignee_proximity_radius, Unset)
            else (None, str(self.assignee_proximity_radius).encode(), "text/plain")
        )
        optimize_after_create = (
            self.optimize_after_create
            if isinstance(self.optimize_after_create, Unset)
            else (None, str(self.optimize_after_create).encode(), "text/plain")
        )
        optimize_when_on_duty = (
            self.optimize_when_on_duty
            if isinstance(self.optimize_when_on_duty, Unset)
            else (None, str(self.optimize_when_on_duty).encode(), "text/plain")
        )
        optimization_objective: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.optimization_objective, Unset):
            optimization_objective = (None, str(self.optimization_objective.value).encode(), "text/plain")

        reference_autogenerate = (
            self.reference_autogenerate
            if isinstance(self.reference_autogenerate, Unset)
            else (None, str(self.reference_autogenerate).encode(), "text/plain")
        )
        reference_offset = (
            self.reference_offset
            if isinstance(self.reference_offset, Unset)
            else (None, str(self.reference_offset).encode(), "text/plain")
        )
        reference_prefix = (
            self.reference_prefix
            if isinstance(self.reference_prefix, Unset)
            else (None, str(self.reference_prefix).encode(), "text/plain")
        )
        reference_length = (
            self.reference_length
            if isinstance(self.reference_length, Unset)
            else (None, str(self.reference_length).encode(), "text/plain")
        )
        feature_show_unassigned_to_workers = (
            self.feature_show_unassigned_to_workers
            if isinstance(self.feature_show_unassigned_to_workers, Unset)
            else (None, str(self.feature_show_unassigned_to_workers).encode(), "text/plain")
        )
        feature_task_created_sound = (
            self.feature_task_created_sound
            if isinstance(self.feature_task_created_sound, Unset)
            else (None, str(self.feature_task_created_sound).encode(), "text/plain")
        )
        feature_change_task_account = (
            self.feature_change_task_account
            if isinstance(self.feature_change_task_account, Unset)
            else (None, str(self.feature_change_task_account).encode(), "text/plain")
        )
        feature_show_tutorial = (
            self.feature_show_tutorial
            if isinstance(self.feature_show_tutorial, Unset)
            else (None, str(self.feature_show_tutorial).encode(), "text/plain")
        )
        feature_navigation_app_selection = (
            self.feature_navigation_app_selection
            if isinstance(self.feature_navigation_app_selection, Unset)
            else (None, str(self.feature_navigation_app_selection).encode(), "text/plain")
        )
        feature_navigation_use_address = (
            self.feature_navigation_use_address
            if isinstance(self.feature_navigation_use_address, Unset)
            else (None, str(self.feature_navigation_use_address).encode(), "text/plain")
        )
        feature_task_accept = (
            self.feature_task_accept
            if isinstance(self.feature_task_accept, Unset)
            else (None, str(self.feature_task_accept).encode(), "text/plain")
        )
        feature_task_reject = (
            self.feature_task_reject
            if isinstance(self.feature_task_reject, Unset)
            else (None, str(self.feature_task_reject).encode(), "text/plain")
        )
        feature_app_task_search = (
            self.feature_app_task_search
            if isinstance(self.feature_app_task_search, Unset)
            else (None, str(self.feature_app_task_search).encode(), "text/plain")
        )
        feature_address_autosuggest_provider: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.feature_address_autosuggest_provider, Unset):
            feature_address_autosuggest_provider = (
                None,
                str(self.feature_address_autosuggest_provider.value).encode(),
                "text/plain",
            )

        feature_geocoding_country_code: Union[Unset, str]
        if isinstance(self.feature_geocoding_country_code, Unset):
            feature_geocoding_country_code = UNSET

        elif isinstance(self.feature_geocoding_country_code, FeatureGeocodingCountryCodeEnum):
            feature_geocoding_country_code = UNSET
            if not isinstance(self.feature_geocoding_country_code, Unset):
                feature_geocoding_country_code = (
                    None,
                    str(self.feature_geocoding_country_code.value).encode(),
                    "text/plain",
                )

        else:
            feature_geocoding_country_code = UNSET
            if not isinstance(self.feature_geocoding_country_code, Unset):
                feature_geocoding_country_code = (
                    None,
                    str(self.feature_geocoding_country_code.value).encode(),
                    "text/plain",
                )

        feature_document_signing = (
            self.feature_document_signing
            if isinstance(self.feature_document_signing, Unset)
            else (None, str(self.feature_document_signing).encode(), "text/plain")
        )
        feature_tracker_reviews_allowed = (
            self.feature_tracker_reviews_allowed
            if isinstance(self.feature_tracker_reviews_allowed, Unset)
            else (None, str(self.feature_tracker_reviews_allowed).encode(), "text/plain")
        )
        auto_assign_orders = (
            self.auto_assign_orders
            if isinstance(self.auto_assign_orders, Unset)
            else (None, str(self.auto_assign_orders).encode(), "text/plain")
        )
        auto_assign_max_tasks = (
            self.auto_assign_max_tasks
            if isinstance(self.auto_assign_max_tasks, Unset)
            else (None, str(self.auto_assign_max_tasks).encode(), "text/plain")
        )
        auto_assign_max_distance = (
            self.auto_assign_max_distance
            if isinstance(self.auto_assign_max_distance, Unset)
            else (None, str(self.auto_assign_max_distance).encode(), "text/plain")
        )
        auto_assign_time_before = (
            self.auto_assign_time_before
            if isinstance(self.auto_assign_time_before, Unset)
            else (None, str(self.auto_assign_time_before).encode(), "text/plain")
        )
        auto_assign_rotate: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.auto_assign_rotate, Unset):
            auto_assign_rotate = (
                (None, json.dumps(self.auto_assign_rotate.to_dict()).encode(), "application/json")
                if self.auto_assign_rotate
                else None
            )

        auto_assign_optimize = (
            self.auto_assign_optimize
            if isinstance(self.auto_assign_optimize, Unset)
            else (None, str(self.auto_assign_optimize).encode(), "text/plain")
        )
        dashboard_task_template = (
            self.dashboard_task_template
            if isinstance(self.dashboard_task_template, Unset)
            else (None, str(self.dashboard_task_template).encode(), "text/plain")
        )
        dashboard_worker_limit = (
            self.dashboard_worker_limit
            if isinstance(self.dashboard_worker_limit, Unset)
            else (None, str(self.dashboard_worker_limit).encode(), "text/plain")
        )
        managers = (
            self.managers if isinstance(self.managers, Unset) else (None, str(self.managers).encode(), "text/plain")
        )
        workers = self.workers if isinstance(self.workers, Unset) else (None, str(self.workers).encode(), "text/plain")
        stripe_customer_id = (
            self.stripe_customer_id
            if isinstance(self.stripe_customer_id, Unset)
            else (None, str(self.stripe_customer_id).encode(), "text/plain")
        )
        stripe_payment_method_id = (
            self.stripe_payment_method_id
            if isinstance(self.stripe_payment_method_id, Unset)
            else (None, str(self.stripe_payment_method_id).encode(), "text/plain")
        )
        billing_method: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.billing_method, Unset):
            billing_method = (None, str(self.billing_method.value).encode(), "text/plain")

        billing_name = (
            self.billing_name
            if isinstance(self.billing_name, Unset)
            else (None, str(self.billing_name).encode(), "text/plain")
        )
        billing_company = (
            self.billing_company
            if isinstance(self.billing_company, Unset)
            else (None, str(self.billing_company).encode(), "text/plain")
        )
        billing_address = (
            self.billing_address
            if isinstance(self.billing_address, Unset)
            else (None, str(self.billing_address).encode(), "text/plain")
        )
        billing_country = (
            self.billing_country
            if isinstance(self.billing_country, Unset)
            else (None, str(self.billing_country).encode(), "text/plain")
        )
        billing_email = (
            self.billing_email
            if isinstance(self.billing_email, Unset)
            else (None, str(self.billing_email).encode(), "text/plain")
        )
        billing_phone = (
            self.billing_phone
            if isinstance(self.billing_phone, Unset)
            else (None, str(self.billing_phone).encode(), "text/plain")
        )
        billing_vatin = (
            self.billing_vatin
            if isinstance(self.billing_vatin, Unset)
            else (None, str(self.billing_vatin).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if slug is not UNSET:
            field_dict["slug"] = slug
        if owner is not UNSET:
            field_dict["owner"] = owner
        if email is not UNSET:
            field_dict["email"] = email
        if notification_emails is not UNSET:
            field_dict["notification_emails"] = notification_emails
        if review_emails is not UNSET:
            field_dict["review_emails"] = review_emails
        if website is not UNSET:
            field_dict["website"] = website
        if registry_code is not UNSET:
            field_dict["registry_code"] = registry_code
        if vatin is not UNSET:
            field_dict["vatin"] = vatin
        if language is not UNSET:
            field_dict["language"] = language
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if address is not UNSET:
            field_dict["address"] = address
        if phone_prefix is not UNSET:
            field_dict["phone_prefix"] = phone_prefix
        if distance_units is not UNSET:
            field_dict["distance_units"] = distance_units
        if task_duration is not UNSET:
            field_dict["task_duration"] = task_duration
        if task_expiry_duration is not UNSET:
            field_dict["task_expiry_duration"] = task_expiry_duration
        if task_expiry_state is not UNSET:
            field_dict["task_expiry_state"] = task_expiry_state
        if assignee_proximity_radius is not UNSET:
            field_dict["assignee_proximity_radius"] = assignee_proximity_radius
        if optimize_after_create is not UNSET:
            field_dict["optimize_after_create"] = optimize_after_create
        if optimize_when_on_duty is not UNSET:
            field_dict["optimize_when_on_duty"] = optimize_when_on_duty
        if optimization_objective is not UNSET:
            field_dict["optimization_objective"] = optimization_objective
        if reference_autogenerate is not UNSET:
            field_dict["reference_autogenerate"] = reference_autogenerate
        if reference_offset is not UNSET:
            field_dict["reference_offset"] = reference_offset
        if reference_prefix is not UNSET:
            field_dict["reference_prefix"] = reference_prefix
        if reference_length is not UNSET:
            field_dict["reference_length"] = reference_length
        if feature_show_unassigned_to_workers is not UNSET:
            field_dict["feature_show_unassigned_to_workers"] = feature_show_unassigned_to_workers
        if feature_task_created_sound is not UNSET:
            field_dict["feature_task_created_sound"] = feature_task_created_sound
        if feature_change_task_account is not UNSET:
            field_dict["feature_change_task_account"] = feature_change_task_account
        if feature_show_tutorial is not UNSET:
            field_dict["feature_show_tutorial"] = feature_show_tutorial
        if feature_navigation_app_selection is not UNSET:
            field_dict["feature_navigation_app_selection"] = feature_navigation_app_selection
        if feature_navigation_use_address is not UNSET:
            field_dict["feature_navigation_use_address"] = feature_navigation_use_address
        if feature_task_accept is not UNSET:
            field_dict["feature_task_accept"] = feature_task_accept
        if feature_task_reject is not UNSET:
            field_dict["feature_task_reject"] = feature_task_reject
        if feature_app_task_search is not UNSET:
            field_dict["feature_app_task_search"] = feature_app_task_search
        if feature_address_autosuggest_provider is not UNSET:
            field_dict["feature_address_autosuggest_provider"] = feature_address_autosuggest_provider
        if feature_geocoding_country_code is not UNSET:
            field_dict["feature_geocoding_country_code"] = feature_geocoding_country_code
        if feature_document_signing is not UNSET:
            field_dict["feature_document_signing"] = feature_document_signing
        if feature_tracker_reviews_allowed is not UNSET:
            field_dict["feature_tracker_reviews_allowed"] = feature_tracker_reviews_allowed
        if auto_assign_orders is not UNSET:
            field_dict["auto_assign_orders"] = auto_assign_orders
        if auto_assign_max_tasks is not UNSET:
            field_dict["auto_assign_max_tasks"] = auto_assign_max_tasks
        if auto_assign_max_distance is not UNSET:
            field_dict["auto_assign_max_distance"] = auto_assign_max_distance
        if auto_assign_time_before is not UNSET:
            field_dict["auto_assign_time_before"] = auto_assign_time_before
        if auto_assign_rotate is not UNSET:
            field_dict["auto_assign_rotate"] = auto_assign_rotate
        if auto_assign_optimize is not UNSET:
            field_dict["auto_assign_optimize"] = auto_assign_optimize
        if dashboard_task_template is not UNSET:
            field_dict["dashboard_task_template"] = dashboard_task_template
        if dashboard_worker_limit is not UNSET:
            field_dict["dashboard_worker_limit"] = dashboard_worker_limit
        if managers is not UNSET:
            field_dict["managers"] = managers
        if workers is not UNSET:
            field_dict["workers"] = workers
        if stripe_customer_id is not UNSET:
            field_dict["stripe_customer_id"] = stripe_customer_id
        if stripe_payment_method_id is not UNSET:
            field_dict["stripe_payment_method_id"] = stripe_payment_method_id
        if billing_method is not UNSET:
            field_dict["billing_method"] = billing_method
        if billing_name is not UNSET:
            field_dict["billing_name"] = billing_name
        if billing_company is not UNSET:
            field_dict["billing_company"] = billing_company
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if billing_country is not UNSET:
            field_dict["billing_country"] = billing_country
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email
        if billing_phone is not UNSET:
            field_dict["billing_phone"] = billing_phone
        if billing_vatin is not UNSET:
            field_dict["billing_vatin"] = billing_vatin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        name = d.pop("name", UNSET)

        def _parse_type(data: object) -> Union[BlankEnum, TypeEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_0 = data
                type_type_0: Union[Unset, TypeEnum]
                if isinstance(_type_type_0, Unset):
                    type_type_0 = UNSET
                else:
                    type_type_0 = TypeEnum(_type_type_0)

                return type_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _type_type_1 = data
            type_type_1: Union[Unset, BlankEnum]
            if isinstance(_type_type_1, Unset):
                type_type_1 = UNSET
            else:
                type_type_1 = BlankEnum(_type_type_1)

            return type_type_1

        type = _parse_type(d.pop("type", UNSET))

        slug = d.pop("slug", UNSET)

        owner = d.pop("owner", UNSET)

        email = d.pop("email", UNSET)

        notification_emails = cast(List[str], d.pop("notification_emails", UNSET))

        review_emails = cast(List[str], d.pop("review_emails", UNSET))

        website = d.pop("website", UNSET)

        registry_code = d.pop("registry_code", UNSET)

        vatin = d.pop("vatin", UNSET)

        _language = d.pop("language", UNSET)
        language: Union[Unset, LanguageEnum]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = LanguageEnum(_language)

        _timezone = d.pop("timezone", UNSET)
        timezone: Union[Unset, TimezoneEnum]
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = TimezoneEnum(_timezone)

        def _parse_country_code(data: object) -> Union[BlankEnum, CountryCodeEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _country_code_type_0 = data
                country_code_type_0: Union[Unset, CountryCodeEnum]
                if isinstance(_country_code_type_0, Unset):
                    country_code_type_0 = UNSET
                else:
                    country_code_type_0 = CountryCodeEnum(_country_code_type_0)

                return country_code_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _country_code_type_1 = data
            country_code_type_1: Union[Unset, BlankEnum]
            if isinstance(_country_code_type_1, Unset):
                country_code_type_1 = UNSET
            else:
                country_code_type_1 = BlankEnum(_country_code_type_1)

            return country_code_type_1

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        _address = d.pop("address", UNSET)
        address: Union[Unset, None, NestedAddress]
        if _address is None:
            address = None
        elif isinstance(_address, Unset):
            address = UNSET
        else:
            address = NestedAddress.from_dict(_address)

        phone_prefix = d.pop("phone_prefix", UNSET)

        _distance_units = d.pop("distance_units", UNSET)
        distance_units: Union[Unset, DistanceUnitsEnum]
        if isinstance(_distance_units, Unset):
            distance_units = UNSET
        else:
            distance_units = DistanceUnitsEnum(_distance_units)

        _task_duration = d.pop("task_duration", UNSET)
        task_duration: Union[Unset, PatchedAccountDefaultTaskDuration]
        if isinstance(_task_duration, Unset):
            task_duration = UNSET
        else:
            task_duration = PatchedAccountDefaultTaskDuration.from_dict(_task_duration)

        _task_expiry_duration = d.pop("task_expiry_duration", UNSET)
        task_expiry_duration: Union[Unset, None, PatchedAccountTaskExpiryDuration]
        if _task_expiry_duration is None:
            task_expiry_duration = None
        elif isinstance(_task_expiry_duration, Unset):
            task_expiry_duration = UNSET
        else:
            task_expiry_duration = PatchedAccountTaskExpiryDuration.from_dict(_task_expiry_duration)

        _task_expiry_state = d.pop("task_expiry_state", UNSET)
        task_expiry_state: Union[Unset, TaskExpiryStateEnum]
        if isinstance(_task_expiry_state, Unset):
            task_expiry_state = UNSET
        else:
            task_expiry_state = TaskExpiryStateEnum(_task_expiry_state)

        assignee_proximity_radius = d.pop("assignee_proximity_radius", UNSET)

        optimize_after_create = d.pop("optimize_after_create", UNSET)

        optimize_when_on_duty = d.pop("optimize_when_on_duty", UNSET)

        _optimization_objective = d.pop("optimization_objective", UNSET)
        optimization_objective: Union[Unset, OptimizationObjectiveEnum]
        if isinstance(_optimization_objective, Unset):
            optimization_objective = UNSET
        else:
            optimization_objective = OptimizationObjectiveEnum(_optimization_objective)

        reference_autogenerate = d.pop("reference_autogenerate", UNSET)

        reference_offset = d.pop("reference_offset", UNSET)

        reference_prefix = d.pop("reference_prefix", UNSET)

        reference_length = d.pop("reference_length", UNSET)

        feature_show_unassigned_to_workers = d.pop("feature_show_unassigned_to_workers", UNSET)

        feature_task_created_sound = d.pop("feature_task_created_sound", UNSET)

        feature_change_task_account = d.pop("feature_change_task_account", UNSET)

        feature_show_tutorial = d.pop("feature_show_tutorial", UNSET)

        feature_navigation_app_selection = d.pop("feature_navigation_app_selection", UNSET)

        feature_navigation_use_address = d.pop("feature_navigation_use_address", UNSET)

        feature_task_accept = d.pop("feature_task_accept", UNSET)

        feature_task_reject = d.pop("feature_task_reject", UNSET)

        feature_app_task_search = d.pop("feature_app_task_search", UNSET)

        _feature_address_autosuggest_provider = d.pop("feature_address_autosuggest_provider", UNSET)
        feature_address_autosuggest_provider: Union[Unset, FeatureAddressAutosuggestProviderEnum]
        if isinstance(_feature_address_autosuggest_provider, Unset):
            feature_address_autosuggest_provider = UNSET
        else:
            feature_address_autosuggest_provider = FeatureAddressAutosuggestProviderEnum(
                _feature_address_autosuggest_provider
            )

        def _parse_feature_geocoding_country_code(
            data: object,
        ) -> Union[BlankEnum, FeatureGeocodingCountryCodeEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _feature_geocoding_country_code_type_0 = data
                feature_geocoding_country_code_type_0: Union[Unset, FeatureGeocodingCountryCodeEnum]
                if isinstance(_feature_geocoding_country_code_type_0, Unset):
                    feature_geocoding_country_code_type_0 = UNSET
                else:
                    feature_geocoding_country_code_type_0 = FeatureGeocodingCountryCodeEnum(
                        _feature_geocoding_country_code_type_0
                    )

                return feature_geocoding_country_code_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _feature_geocoding_country_code_type_1 = data
            feature_geocoding_country_code_type_1: Union[Unset, BlankEnum]
            if isinstance(_feature_geocoding_country_code_type_1, Unset):
                feature_geocoding_country_code_type_1 = UNSET
            else:
                feature_geocoding_country_code_type_1 = BlankEnum(_feature_geocoding_country_code_type_1)

            return feature_geocoding_country_code_type_1

        feature_geocoding_country_code = _parse_feature_geocoding_country_code(
            d.pop("feature_geocoding_country_code", UNSET)
        )

        feature_document_signing = d.pop("feature_document_signing", UNSET)

        feature_tracker_reviews_allowed = d.pop("feature_tracker_reviews_allowed", UNSET)

        auto_assign_orders = d.pop("auto_assign_orders", UNSET)

        auto_assign_max_tasks = d.pop("auto_assign_max_tasks", UNSET)

        auto_assign_max_distance = d.pop("auto_assign_max_distance", UNSET)

        auto_assign_time_before = d.pop("auto_assign_time_before", UNSET)

        _auto_assign_rotate = d.pop("auto_assign_rotate", UNSET)
        auto_assign_rotate: Union[Unset, None, PatchedAccountRotateAssignee]
        if _auto_assign_rotate is None:
            auto_assign_rotate = None
        elif isinstance(_auto_assign_rotate, Unset):
            auto_assign_rotate = UNSET
        else:
            auto_assign_rotate = PatchedAccountRotateAssignee.from_dict(_auto_assign_rotate)

        auto_assign_optimize = d.pop("auto_assign_optimize", UNSET)

        dashboard_task_template = d.pop("dashboard_task_template", UNSET)

        dashboard_worker_limit = d.pop("dashboard_worker_limit", UNSET)

        managers = d.pop("managers", UNSET)

        workers = d.pop("workers", UNSET)

        stripe_customer_id = d.pop("stripe_customer_id", UNSET)

        stripe_payment_method_id = d.pop("stripe_payment_method_id", UNSET)

        _billing_method = d.pop("billing_method", UNSET)
        billing_method: Union[Unset, AccountBillingMethodEnum]
        if isinstance(_billing_method, Unset):
            billing_method = UNSET
        else:
            billing_method = AccountBillingMethodEnum(_billing_method)

        billing_name = d.pop("billing_name", UNSET)

        billing_company = d.pop("billing_company", UNSET)

        billing_address = d.pop("billing_address", UNSET)

        billing_country = d.pop("billing_country", UNSET)

        billing_email = d.pop("billing_email", UNSET)

        billing_phone = d.pop("billing_phone", UNSET)

        billing_vatin = d.pop("billing_vatin", UNSET)

        patched_account = cls(
            id=id,
            url=url,
            name=name,
            type=type,
            slug=slug,
            owner=owner,
            email=email,
            notification_emails=notification_emails,
            review_emails=review_emails,
            website=website,
            registry_code=registry_code,
            vatin=vatin,
            language=language,
            timezone=timezone,
            country_code=country_code,
            address=address,
            phone_prefix=phone_prefix,
            distance_units=distance_units,
            task_duration=task_duration,
            task_expiry_duration=task_expiry_duration,
            task_expiry_state=task_expiry_state,
            assignee_proximity_radius=assignee_proximity_radius,
            optimize_after_create=optimize_after_create,
            optimize_when_on_duty=optimize_when_on_duty,
            optimization_objective=optimization_objective,
            reference_autogenerate=reference_autogenerate,
            reference_offset=reference_offset,
            reference_prefix=reference_prefix,
            reference_length=reference_length,
            feature_show_unassigned_to_workers=feature_show_unassigned_to_workers,
            feature_task_created_sound=feature_task_created_sound,
            feature_change_task_account=feature_change_task_account,
            feature_show_tutorial=feature_show_tutorial,
            feature_navigation_app_selection=feature_navigation_app_selection,
            feature_navigation_use_address=feature_navigation_use_address,
            feature_task_accept=feature_task_accept,
            feature_task_reject=feature_task_reject,
            feature_app_task_search=feature_app_task_search,
            feature_address_autosuggest_provider=feature_address_autosuggest_provider,
            feature_geocoding_country_code=feature_geocoding_country_code,
            feature_document_signing=feature_document_signing,
            feature_tracker_reviews_allowed=feature_tracker_reviews_allowed,
            auto_assign_orders=auto_assign_orders,
            auto_assign_max_tasks=auto_assign_max_tasks,
            auto_assign_max_distance=auto_assign_max_distance,
            auto_assign_time_before=auto_assign_time_before,
            auto_assign_rotate=auto_assign_rotate,
            auto_assign_optimize=auto_assign_optimize,
            dashboard_task_template=dashboard_task_template,
            dashboard_worker_limit=dashboard_worker_limit,
            managers=managers,
            workers=workers,
            stripe_customer_id=stripe_customer_id,
            stripe_payment_method_id=stripe_payment_method_id,
            billing_method=billing_method,
            billing_name=billing_name,
            billing_company=billing_company,
            billing_address=billing_address,
            billing_country=billing_country,
            billing_email=billing_email,
            billing_phone=billing_phone,
            billing_vatin=billing_vatin,
        )

        patched_account.additional_properties = d
        return patched_account

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

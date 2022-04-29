import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.account_role_state_enum import AccountRoleStateEnum
from ..models.nested_address import NestedAddress
from ..models.vehicle_profile_enum import VehicleProfileEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAccountRole")


@attr.s(auto_attribs=True)
class PatchedAccountRole:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        user (Union[Unset, str]):
        state (Union[Unset, AccountRoleStateEnum]):
        email (Union[Unset, str]):
        display_name (Union[Unset, None, str]):
        phone (Union[Unset, str]):
        vehicle_registration_number (Union[Unset, str]):
        vehicle_profile (Union[Unset, VehicleProfileEnum]):
        vehicle_capacity (Union[Unset, None, List[int]]):
        vehicle_speed_factor (Union[Unset, str]):
        vehicle_service_time_factor (Union[Unset, str]):
        route_start_address (Union[Unset, NestedAddress]):
        route_end_address (Union[Unset, NestedAddress]):
        signature_image (Union[Unset, str]):
        is_manager (Union[Unset, bool]):
        is_worker (Union[Unset, bool]):
        is_integration (Union[Unset, bool]):
        is_active (Union[Unset, str]):
        is_on_duty (Union[Unset, str]):
        show_unassigned (Union[Unset, bool]):
        last_time_location (Union[Unset, str]):
        activated_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    state: Union[Unset, AccountRoleStateEnum] = UNSET
    email: Union[Unset, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    phone: Union[Unset, str] = UNSET
    vehicle_registration_number: Union[Unset, str] = UNSET
    vehicle_profile: Union[Unset, VehicleProfileEnum] = UNSET
    vehicle_capacity: Union[Unset, None, List[int]] = UNSET
    vehicle_speed_factor: Union[Unset, str] = UNSET
    vehicle_service_time_factor: Union[Unset, str] = UNSET
    route_start_address: Union[Unset, NestedAddress] = UNSET
    route_end_address: Union[Unset, NestedAddress] = UNSET
    signature_image: Union[Unset, str] = UNSET
    is_manager: Union[Unset, bool] = UNSET
    is_worker: Union[Unset, bool] = UNSET
    is_integration: Union[Unset, bool] = UNSET
    is_active: Union[Unset, str] = UNSET
    is_on_duty: Union[Unset, str] = UNSET
    show_unassigned: Union[Unset, bool] = UNSET
    last_time_location: Union[Unset, str] = UNSET
    activated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        user = self.user
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        email = self.email
        display_name = self.display_name
        phone = self.phone
        vehicle_registration_number = self.vehicle_registration_number
        vehicle_profile: Union[Unset, str] = UNSET
        if not isinstance(self.vehicle_profile, Unset):
            vehicle_profile = self.vehicle_profile.value

        vehicle_capacity: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.vehicle_capacity, Unset):
            if self.vehicle_capacity is None:
                vehicle_capacity = None
            else:
                vehicle_capacity = self.vehicle_capacity

        vehicle_speed_factor = self.vehicle_speed_factor
        vehicle_service_time_factor = self.vehicle_service_time_factor
        route_start_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.route_start_address, Unset):
            route_start_address = self.route_start_address.to_dict()

        route_end_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.route_end_address, Unset):
            route_end_address = self.route_end_address.to_dict()

        signature_image = self.signature_image
        is_manager = self.is_manager
        is_worker = self.is_worker
        is_integration = self.is_integration
        is_active = self.is_active
        is_on_duty = self.is_on_duty
        show_unassigned = self.show_unassigned
        last_time_location = self.last_time_location
        activated_at: Union[Unset, str] = UNSET
        if not isinstance(self.activated_at, Unset):
            activated_at = self.activated_at.isoformat()

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

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
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if user is not UNSET:
            field_dict["user"] = user
        if state is not UNSET:
            field_dict["state"] = state
        if email is not UNSET:
            field_dict["email"] = email
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if vehicle_registration_number is not UNSET:
            field_dict["vehicle_registration_number"] = vehicle_registration_number
        if vehicle_profile is not UNSET:
            field_dict["vehicle_profile"] = vehicle_profile
        if vehicle_capacity is not UNSET:
            field_dict["vehicle_capacity"] = vehicle_capacity
        if vehicle_speed_factor is not UNSET:
            field_dict["vehicle_speed_factor"] = vehicle_speed_factor
        if vehicle_service_time_factor is not UNSET:
            field_dict["vehicle_service_time_factor"] = vehicle_service_time_factor
        if route_start_address is not UNSET:
            field_dict["route_start_address"] = route_start_address
        if route_end_address is not UNSET:
            field_dict["route_end_address"] = route_end_address
        if signature_image is not UNSET:
            field_dict["signature_image"] = signature_image
        if is_manager is not UNSET:
            field_dict["is_manager"] = is_manager
        if is_worker is not UNSET:
            field_dict["is_worker"] = is_worker
        if is_integration is not UNSET:
            field_dict["is_integration"] = is_integration
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_on_duty is not UNSET:
            field_dict["is_on_duty"] = is_on_duty
        if show_unassigned is not UNSET:
            field_dict["show_unassigned"] = show_unassigned
        if last_time_location is not UNSET:
            field_dict["last_time_location"] = last_time_location
        if activated_at is not UNSET:
            field_dict["activated_at"] = activated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        account = d.pop("account", UNSET)

        user = d.pop("user", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, AccountRoleStateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = AccountRoleStateEnum(_state)

        email = d.pop("email", UNSET)

        display_name = d.pop("display_name", UNSET)

        phone = d.pop("phone", UNSET)

        vehicle_registration_number = d.pop("vehicle_registration_number", UNSET)

        _vehicle_profile = d.pop("vehicle_profile", UNSET)
        vehicle_profile: Union[Unset, VehicleProfileEnum]
        if isinstance(_vehicle_profile, Unset):
            vehicle_profile = UNSET
        else:
            vehicle_profile = VehicleProfileEnum(_vehicle_profile)

        vehicle_capacity = cast(List[int], d.pop("vehicle_capacity", UNSET))

        vehicle_speed_factor = d.pop("vehicle_speed_factor", UNSET)

        vehicle_service_time_factor = d.pop("vehicle_service_time_factor", UNSET)

        _route_start_address = d.pop("route_start_address", UNSET)
        route_start_address: Union[Unset, NestedAddress]
        if isinstance(_route_start_address, Unset):
            route_start_address = UNSET
        else:
            route_start_address = NestedAddress.from_dict(_route_start_address)

        _route_end_address = d.pop("route_end_address", UNSET)
        route_end_address: Union[Unset, NestedAddress]
        if isinstance(_route_end_address, Unset):
            route_end_address = UNSET
        else:
            route_end_address = NestedAddress.from_dict(_route_end_address)

        signature_image = d.pop("signature_image", UNSET)

        is_manager = d.pop("is_manager", UNSET)

        is_worker = d.pop("is_worker", UNSET)

        is_integration = d.pop("is_integration", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_on_duty = d.pop("is_on_duty", UNSET)

        show_unassigned = d.pop("show_unassigned", UNSET)

        last_time_location = d.pop("last_time_location", UNSET)

        _activated_at = d.pop("activated_at", UNSET)
        activated_at: Union[Unset, datetime.datetime]
        if isinstance(_activated_at, Unset):
            activated_at = UNSET
        else:
            activated_at = isoparse(_activated_at)

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

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

        patched_account_role = cls(
            id=id,
            url=url,
            account=account,
            user=user,
            state=state,
            email=email,
            display_name=display_name,
            phone=phone,
            vehicle_registration_number=vehicle_registration_number,
            vehicle_profile=vehicle_profile,
            vehicle_capacity=vehicle_capacity,
            vehicle_speed_factor=vehicle_speed_factor,
            vehicle_service_time_factor=vehicle_service_time_factor,
            route_start_address=route_start_address,
            route_end_address=route_end_address,
            signature_image=signature_image,
            is_manager=is_manager,
            is_worker=is_worker,
            is_integration=is_integration,
            is_active=is_active,
            is_on_duty=is_on_duty,
            show_unassigned=show_unassigned,
            last_time_location=last_time_location,
            activated_at=activated_at,
            deleted_at=deleted_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_account_role.additional_properties = d
        return patched_account_role

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.timezone_enum import TimezoneEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Device")


@attr.s(auto_attribs=True)
class Device:
    """
    Attributes:
        id (str):
        url (str):
        user (str):
        created_at (datetime.datetime):
        brand (Union[Unset, None, str]):
        build_number (Union[Unset, None, str]):
        device_country (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        device_locale (Union[Unset, None, str]):
        free_disk_storage (Union[Unset, None, int]):
        manufacturer (Union[Unset, None, str]):
        model (Union[Unset, None, str]):
        readable_version (Union[Unset, None, str]):
        system_name (Union[Unset, None, str]):
        system_version (Union[Unset, None, str]):
        timezone (Union[BlankEnum, TimezoneEnum, Unset]):
        version (Union[Unset, None, str]):
        location_permission (Union[Unset, None, str]):
        notification_permission (Union[Unset, None, str]):
        motion_permission (Union[Unset, None, str]):
        ios_app_tracking_permission (Union[Unset, None, str]):
        battery_level (Union[Unset, None, int]):
        is_charging (Union[Unset, None, bool]):
    """

    id: str
    url: str
    user: str
    created_at: datetime.datetime
    brand: Union[Unset, None, str] = UNSET
    build_number: Union[Unset, None, str] = UNSET
    device_country: Union[Unset, None, str] = UNSET
    device_id: Union[Unset, None, str] = UNSET
    device_locale: Union[Unset, None, str] = UNSET
    free_disk_storage: Union[Unset, None, int] = UNSET
    manufacturer: Union[Unset, None, str] = UNSET
    model: Union[Unset, None, str] = UNSET
    readable_version: Union[Unset, None, str] = UNSET
    system_name: Union[Unset, None, str] = UNSET
    system_version: Union[Unset, None, str] = UNSET
    timezone: Union[BlankEnum, TimezoneEnum, Unset] = UNSET
    version: Union[Unset, None, str] = UNSET
    location_permission: Union[Unset, None, str] = UNSET
    notification_permission: Union[Unset, None, str] = UNSET
    motion_permission: Union[Unset, None, str] = UNSET
    ios_app_tracking_permission: Union[Unset, None, str] = UNSET
    battery_level: Union[Unset, None, int] = UNSET
    is_charging: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        user = self.user
        created_at = self.created_at.isoformat()

        brand = self.brand
        build_number = self.build_number
        device_country = self.device_country
        device_id = self.device_id
        device_locale = self.device_locale
        free_disk_storage = self.free_disk_storage
        manufacturer = self.manufacturer
        model = self.model
        readable_version = self.readable_version
        system_name = self.system_name
        system_version = self.system_version
        timezone: Union[Unset, str]
        if isinstance(self.timezone, Unset):
            timezone = UNSET

        elif isinstance(self.timezone, TimezoneEnum):
            timezone = UNSET
            if not isinstance(self.timezone, Unset):
                timezone = self.timezone.value

        else:
            timezone = UNSET
            if not isinstance(self.timezone, Unset):
                timezone = self.timezone.value

        version = self.version
        location_permission = self.location_permission
        notification_permission = self.notification_permission
        motion_permission = self.motion_permission
        ios_app_tracking_permission = self.ios_app_tracking_permission
        battery_level = self.battery_level
        is_charging = self.is_charging

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "user": user,
                "created_at": created_at,
            }
        )
        if brand is not UNSET:
            field_dict["brand"] = brand
        if build_number is not UNSET:
            field_dict["build_number"] = build_number
        if device_country is not UNSET:
            field_dict["device_country"] = device_country
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if device_locale is not UNSET:
            field_dict["device_locale"] = device_locale
        if free_disk_storage is not UNSET:
            field_dict["free_disk_storage"] = free_disk_storage
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if readable_version is not UNSET:
            field_dict["readable_version"] = readable_version
        if system_name is not UNSET:
            field_dict["system_name"] = system_name
        if system_version is not UNSET:
            field_dict["system_version"] = system_version
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if version is not UNSET:
            field_dict["version"] = version
        if location_permission is not UNSET:
            field_dict["location_permission"] = location_permission
        if notification_permission is not UNSET:
            field_dict["notification_permission"] = notification_permission
        if motion_permission is not UNSET:
            field_dict["motion_permission"] = motion_permission
        if ios_app_tracking_permission is not UNSET:
            field_dict["ios_app_tracking_permission"] = ios_app_tracking_permission
        if battery_level is not UNSET:
            field_dict["battery_level"] = battery_level
        if is_charging is not UNSET:
            field_dict["is_charging"] = is_charging

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        brand = self.brand if isinstance(self.brand, Unset) else (None, str(self.brand).encode(), "text/plain")
        build_number = (
            self.build_number
            if isinstance(self.build_number, Unset)
            else (None, str(self.build_number).encode(), "text/plain")
        )
        device_country = (
            self.device_country
            if isinstance(self.device_country, Unset)
            else (None, str(self.device_country).encode(), "text/plain")
        )
        device_id = (
            self.device_id if isinstance(self.device_id, Unset) else (None, str(self.device_id).encode(), "text/plain")
        )
        device_locale = (
            self.device_locale
            if isinstance(self.device_locale, Unset)
            else (None, str(self.device_locale).encode(), "text/plain")
        )
        free_disk_storage = (
            self.free_disk_storage
            if isinstance(self.free_disk_storage, Unset)
            else (None, str(self.free_disk_storage).encode(), "text/plain")
        )
        manufacturer = (
            self.manufacturer
            if isinstance(self.manufacturer, Unset)
            else (None, str(self.manufacturer).encode(), "text/plain")
        )
        model = self.model if isinstance(self.model, Unset) else (None, str(self.model).encode(), "text/plain")
        readable_version = (
            self.readable_version
            if isinstance(self.readable_version, Unset)
            else (None, str(self.readable_version).encode(), "text/plain")
        )
        system_name = (
            self.system_name
            if isinstance(self.system_name, Unset)
            else (None, str(self.system_name).encode(), "text/plain")
        )
        system_version = (
            self.system_version
            if isinstance(self.system_version, Unset)
            else (None, str(self.system_version).encode(), "text/plain")
        )
        timezone: Union[Unset, str]
        if isinstance(self.timezone, Unset):
            timezone = UNSET

        elif isinstance(self.timezone, TimezoneEnum):
            timezone = UNSET
            if not isinstance(self.timezone, Unset):
                timezone = (None, str(self.timezone.value).encode(), "text/plain")

        else:
            timezone = UNSET
            if not isinstance(self.timezone, Unset):
                timezone = (None, str(self.timezone.value).encode(), "text/plain")

        version = self.version if isinstance(self.version, Unset) else (None, str(self.version).encode(), "text/plain")
        location_permission = (
            self.location_permission
            if isinstance(self.location_permission, Unset)
            else (None, str(self.location_permission).encode(), "text/plain")
        )
        notification_permission = (
            self.notification_permission
            if isinstance(self.notification_permission, Unset)
            else (None, str(self.notification_permission).encode(), "text/plain")
        )
        motion_permission = (
            self.motion_permission
            if isinstance(self.motion_permission, Unset)
            else (None, str(self.motion_permission).encode(), "text/plain")
        )
        ios_app_tracking_permission = (
            self.ios_app_tracking_permission
            if isinstance(self.ios_app_tracking_permission, Unset)
            else (None, str(self.ios_app_tracking_permission).encode(), "text/plain")
        )
        battery_level = (
            self.battery_level
            if isinstance(self.battery_level, Unset)
            else (None, str(self.battery_level).encode(), "text/plain")
        )
        is_charging = (
            self.is_charging
            if isinstance(self.is_charging, Unset)
            else (None, str(self.is_charging).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "user": user,
                "created_at": created_at,
            }
        )
        if brand is not UNSET:
            field_dict["brand"] = brand
        if build_number is not UNSET:
            field_dict["build_number"] = build_number
        if device_country is not UNSET:
            field_dict["device_country"] = device_country
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if device_locale is not UNSET:
            field_dict["device_locale"] = device_locale
        if free_disk_storage is not UNSET:
            field_dict["free_disk_storage"] = free_disk_storage
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model is not UNSET:
            field_dict["model"] = model
        if readable_version is not UNSET:
            field_dict["readable_version"] = readable_version
        if system_name is not UNSET:
            field_dict["system_name"] = system_name
        if system_version is not UNSET:
            field_dict["system_version"] = system_version
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if version is not UNSET:
            field_dict["version"] = version
        if location_permission is not UNSET:
            field_dict["location_permission"] = location_permission
        if notification_permission is not UNSET:
            field_dict["notification_permission"] = notification_permission
        if motion_permission is not UNSET:
            field_dict["motion_permission"] = motion_permission
        if ios_app_tracking_permission is not UNSET:
            field_dict["ios_app_tracking_permission"] = ios_app_tracking_permission
        if battery_level is not UNSET:
            field_dict["battery_level"] = battery_level
        if is_charging is not UNSET:
            field_dict["is_charging"] = is_charging

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        user = d.pop("user")

        created_at = isoparse(d.pop("created_at"))

        brand = d.pop("brand", UNSET)

        build_number = d.pop("build_number", UNSET)

        device_country = d.pop("device_country", UNSET)

        device_id = d.pop("device_id", UNSET)

        device_locale = d.pop("device_locale", UNSET)

        free_disk_storage = d.pop("free_disk_storage", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        model = d.pop("model", UNSET)

        readable_version = d.pop("readable_version", UNSET)

        system_name = d.pop("system_name", UNSET)

        system_version = d.pop("system_version", UNSET)

        def _parse_timezone(data: object) -> Union[BlankEnum, TimezoneEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _timezone_type_0 = data
                timezone_type_0: Union[Unset, TimezoneEnum]
                if isinstance(_timezone_type_0, Unset):
                    timezone_type_0 = UNSET
                else:
                    timezone_type_0 = TimezoneEnum(_timezone_type_0)

                return timezone_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _timezone_type_1 = data
            timezone_type_1: Union[Unset, BlankEnum]
            if isinstance(_timezone_type_1, Unset):
                timezone_type_1 = UNSET
            else:
                timezone_type_1 = BlankEnum(_timezone_type_1)

            return timezone_type_1

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        version = d.pop("version", UNSET)

        location_permission = d.pop("location_permission", UNSET)

        notification_permission = d.pop("notification_permission", UNSET)

        motion_permission = d.pop("motion_permission", UNSET)

        ios_app_tracking_permission = d.pop("ios_app_tracking_permission", UNSET)

        battery_level = d.pop("battery_level", UNSET)

        is_charging = d.pop("is_charging", UNSET)

        device = cls(
            id=id,
            url=url,
            user=user,
            created_at=created_at,
            brand=brand,
            build_number=build_number,
            device_country=device_country,
            device_id=device_id,
            device_locale=device_locale,
            free_disk_storage=free_disk_storage,
            manufacturer=manufacturer,
            model=model,
            readable_version=readable_version,
            system_name=system_name,
            system_version=system_version,
            timezone=timezone,
            version=version,
            location_permission=location_permission,
            notification_permission=notification_permission,
            motion_permission=motion_permission,
            ios_app_tracking_permission=ios_app_tracking_permission,
            battery_level=battery_level,
            is_charging=is_charging,
        )

        device.additional_properties = d
        return device

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

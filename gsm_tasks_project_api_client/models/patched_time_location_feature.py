import datetime
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.state_29f_enum import State29FEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedTimeLocationFeature")


@attr.s(auto_attribs=True)
class PatchedTimeLocationFeature:
    """A subclass of ModelSerializer
    that outputs geojson-ready data as
    features and feature collections

        Attributes:
            model (Union[Unset, str]):
            id (Union[Unset, str]):
            source (Union[Unset, str]):
            user (Union[Unset, str]):
            time (Union[Unset, datetime.datetime]):
            state (Union[Unset, State29FEnum]):
            heading (Union[Unset, None, int]):
            speed (Union[Unset, None, int]):
            altitude (Union[Unset, None, int]):
            accuracy (Union[Unset, None, int]):
            battery_level (Union[Unset, None, str]):
            created_at (Union[Unset, datetime.datetime]):
            updated_at (Union[Unset, datetime.datetime]):
            location (Union[Unset, str]):
    """

    model: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, State29FEnum] = UNSET
    heading: Union[Unset, None, int] = UNSET
    speed: Union[Unset, None, int] = UNSET
    altitude: Union[Unset, None, int] = UNSET
    accuracy: Union[Unset, None, int] = UNSET
    battery_level: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model = self.model
        id = self.id
        source = self.source
        user = self.user
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        heading = self.heading
        speed = self.speed
        altitude = self.altitude
        accuracy = self.accuracy
        battery_level = self.battery_level
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if id is not UNSET:
            field_dict["id"] = id
        if source is not UNSET:
            field_dict["source"] = source
        if user is not UNSET:
            field_dict["user"] = user
        if time is not UNSET:
            field_dict["time"] = time
        if state is not UNSET:
            field_dict["state"] = state
        if heading is not UNSET:
            field_dict["heading"] = heading
        if speed is not UNSET:
            field_dict["speed"] = speed
        if altitude is not UNSET:
            field_dict["altitude"] = altitude
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy
        if battery_level is not UNSET:
            field_dict["battery_level"] = battery_level
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        model = self.model if isinstance(self.model, Unset) else (None, str(self.model).encode(), "text/plain")
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        source = self.source if isinstance(self.source, Unset) else (None, str(self.source).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        time: Union[Unset, bytes] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat().encode()

        state: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.state, Unset):
            state = (None, str(self.state.value).encode(), "text/plain")

        heading = self.heading if isinstance(self.heading, Unset) else (None, str(self.heading).encode(), "text/plain")
        speed = self.speed if isinstance(self.speed, Unset) else (None, str(self.speed).encode(), "text/plain")
        altitude = (
            self.altitude if isinstance(self.altitude, Unset) else (None, str(self.altitude).encode(), "text/plain")
        )
        accuracy = (
            self.accuracy if isinstance(self.accuracy, Unset) else (None, str(self.accuracy).encode(), "text/plain")
        )
        battery_level = (
            self.battery_level
            if isinstance(self.battery_level, Unset)
            else (None, str(self.battery_level).encode(), "text/plain")
        )
        created_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        location = (
            self.location if isinstance(self.location, Unset) else (None, str(self.location).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if id is not UNSET:
            field_dict["id"] = id
        if source is not UNSET:
            field_dict["source"] = source
        if user is not UNSET:
            field_dict["user"] = user
        if time is not UNSET:
            field_dict["time"] = time
        if state is not UNSET:
            field_dict["state"] = state
        if heading is not UNSET:
            field_dict["heading"] = heading
        if speed is not UNSET:
            field_dict["speed"] = speed
        if altitude is not UNSET:
            field_dict["altitude"] = altitude
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy
        if battery_level is not UNSET:
            field_dict["battery_level"] = battery_level
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model = d.pop("model", UNSET)

        id = d.pop("id", UNSET)

        source = d.pop("source", UNSET)

        user = d.pop("user", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        _state = d.pop("state", UNSET)
        state: Union[Unset, State29FEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = State29FEnum(_state)

        heading = d.pop("heading", UNSET)

        speed = d.pop("speed", UNSET)

        altitude = d.pop("altitude", UNSET)

        accuracy = d.pop("accuracy", UNSET)

        battery_level = d.pop("battery_level", UNSET)

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

        location = d.pop("location", UNSET)

        patched_time_location_feature = cls(
            model=model,
            id=id,
            source=source,
            user=user,
            time=time,
            state=state,
            heading=heading,
            speed=speed,
            altitude=altitude,
            accuracy=accuracy,
            battery_level=battery_level,
            created_at=created_at,
            updated_at=updated_at,
            location=location,
        )

        patched_time_location_feature.additional_properties = d
        return patched_time_location_feature

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

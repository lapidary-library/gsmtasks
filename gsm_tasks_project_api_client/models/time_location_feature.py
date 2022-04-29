import datetime
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.state_29f_enum import State29FEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeLocationFeature")


@attr.s(auto_attribs=True)
class TimeLocationFeature:
    """A subclass of ModelSerializer
    that outputs geojson-ready data as
    features and feature collections

        Attributes:
            model (str):
            id (str):
            source (str):
            user (str):
            time (datetime.datetime):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            location (str):
            state (Union[Unset, State29FEnum]):
            heading (Union[Unset, None, int]):
            speed (Union[Unset, None, int]):
            altitude (Union[Unset, None, int]):
            accuracy (Union[Unset, None, int]):
            battery_level (Union[Unset, None, str]):
    """

    model: str
    id: str
    source: str
    user: str
    time: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    location: str
    state: Union[Unset, State29FEnum] = UNSET
    heading: Union[Unset, None, int] = UNSET
    speed: Union[Unset, None, int] = UNSET
    altitude: Union[Unset, None, int] = UNSET
    accuracy: Union[Unset, None, int] = UNSET
    battery_level: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model = self.model
        id = self.id
        source = self.source
        user = self.user
        time = self.time.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        location = self.location
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        heading = self.heading
        speed = self.speed
        altitude = self.altitude
        accuracy = self.accuracy
        battery_level = self.battery_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "id": id,
                "source": source,
                "user": user,
                "time": time,
                "created_at": created_at,
                "updated_at": updated_at,
                "location": location,
            }
        )
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

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        model = self.model if isinstance(self.model, Unset) else (None, str(self.model).encode(), "text/plain")
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        source = self.source if isinstance(self.source, Unset) else (None, str(self.source).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        time = self.time.isoformat().encode()

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        location = (
            self.location if isinstance(self.location, Unset) else (None, str(self.location).encode(), "text/plain")
        )
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "model": model,
                "id": id,
                "source": source,
                "user": user,
                "time": time,
                "created_at": created_at,
                "updated_at": updated_at,
                "location": location,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model = d.pop("model")

        id = d.pop("id")

        source = d.pop("source")

        user = d.pop("user")

        time = isoparse(d.pop("time"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        location = d.pop("location")

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

        time_location_feature = cls(
            model=model,
            id=id,
            source=source,
            user=user,
            time=time,
            created_at=created_at,
            updated_at=updated_at,
            location=location,
            state=state,
            heading=heading,
            speed=speed,
            altitude=altitude,
            accuracy=accuracy,
            battery_level=battery_level,
        )

        time_location_feature.additional_properties = d
        return time_location_feature

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

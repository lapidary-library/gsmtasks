import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="WorkerTrack")


@attr.s(auto_attribs=True)
class WorkerTrack:
    """A subclass of ModelSerializer
    that outputs geojson-ready data as
    features and feature collections

        Attributes:
            id (str):
            track (str):
            user (str):
            start_time (datetime.datetime):
            end_time (datetime.datetime):
    """

    id: str
    track: str
    user: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        track = self.track
        user = self.user
        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "track": track,
                "user": user,
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        track = d.pop("track")

        user = d.pop("user")

        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        worker_track = cls(
            id=id,
            track=track,
            user=user,
            start_time=start_time,
            end_time=end_time,
        )

        worker_track.additional_properties = d
        return worker_track

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

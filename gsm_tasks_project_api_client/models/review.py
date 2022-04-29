import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Review")


@attr.s(auto_attribs=True)
class Review:
    """
    Attributes:
        id (str):
        tracker (str):
        rating (int):
        last_task (str):
        last_assignee (str):
        created_at (datetime.datetime):
        comment (Union[Unset, str]):
    """

    id: str
    tracker: str
    rating: int
    last_task: str
    last_assignee: str
    created_at: datetime.datetime
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        tracker = self.tracker
        rating = self.rating
        last_task = self.last_task
        last_assignee = self.last_assignee
        created_at = self.created_at.isoformat()

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tracker": tracker,
                "rating": rating,
                "last_task": last_task,
                "last_assignee": last_assignee,
                "created_at": created_at,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        tracker = self.tracker if isinstance(self.tracker, Unset) else (None, str(self.tracker).encode(), "text/plain")
        rating = self.rating if isinstance(self.rating, Unset) else (None, str(self.rating).encode(), "text/plain")
        last_task = (
            self.last_task if isinstance(self.last_task, Unset) else (None, str(self.last_task).encode(), "text/plain")
        )
        last_assignee = (
            self.last_assignee
            if isinstance(self.last_assignee, Unset)
            else (None, str(self.last_assignee).encode(), "text/plain")
        )
        created_at = self.created_at.isoformat().encode()

        comment = self.comment if isinstance(self.comment, Unset) else (None, str(self.comment).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "tracker": tracker,
                "rating": rating,
                "last_task": last_task,
                "last_assignee": last_assignee,
                "created_at": created_at,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        tracker = d.pop("tracker")

        rating = d.pop("rating")

        last_task = d.pop("last_task")

        last_assignee = d.pop("last_assignee")

        created_at = isoparse(d.pop("created_at"))

        comment = d.pop("comment", UNSET)

        review = cls(
            id=id,
            tracker=tracker,
            rating=rating,
            last_task=last_task,
            last_assignee=last_assignee,
            created_at=created_at,
            comment=comment,
        )

        review.additional_properties = d
        return review

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.objective_enum import ObjectiveEnum
from ..models.route_optimization_serializer_v2_end_location import RouteOptimizationSerializerV2EndLocation
from ..models.route_optimization_serializer_v2_start_location import RouteOptimizationSerializerV2StartLocation
from ..models.route_optimization_serializer_v2_state_enum import RouteOptimizationSerializerV2StateEnum
from ..models.route_optimization_serializer_v2_total_duration import RouteOptimizationSerializerV2TotalDuration
from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteOptimizationSerializerV2")


@attr.s(auto_attribs=True)
class RouteOptimizationSerializerV2:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        assignees (List[str]):
        state (RouteOptimizationSerializerV2StateEnum):
        tasks (List[str]):
        total_distance (int):
        total_duration (RouteOptimizationSerializerV2TotalDuration):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        objective (Union[None, ObjectiveEnum, Unset]):
        start_time (Union[Unset, None, datetime.datetime]):
        start_location (Union[Unset, None, RouteOptimizationSerializerV2StartLocation]):
        end_location (Union[Unset, None, RouteOptimizationSerializerV2EndLocation]):
        unassign_not_optimal (Union[Unset, bool]):
        commit (Union[Unset, bool]):
        created_by (Union[Unset, str]):
    """

    id: str
    url: str
    account: str
    assignees: List[str]
    state: RouteOptimizationSerializerV2StateEnum
    tasks: List[str]
    total_distance: int
    total_duration: RouteOptimizationSerializerV2TotalDuration
    created_at: datetime.datetime
    updated_at: datetime.datetime
    objective: Union[None, ObjectiveEnum, Unset] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    start_location: Union[Unset, None, RouteOptimizationSerializerV2StartLocation] = UNSET
    end_location: Union[Unset, None, RouteOptimizationSerializerV2EndLocation] = UNSET
    unassign_not_optimal: Union[Unset, bool] = UNSET
    commit: Union[Unset, bool] = UNSET
    created_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        assignees = self.assignees

        state = self.state.value

        tasks = self.tasks

        total_distance = self.total_distance
        total_duration = self.total_duration.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        objective: Union[None, Unset, str]
        if isinstance(self.objective, Unset):
            objective = UNSET
        elif self.objective is None:
            objective = None

        elif isinstance(self.objective, ObjectiveEnum):
            objective = UNSET
            if not isinstance(self.objective, Unset):
                objective = self.objective.value

        else:
            objective = self.objective

        start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat() if self.start_time else None

        start_location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.start_location, Unset):
            start_location = self.start_location.to_dict() if self.start_location else None

        end_location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.end_location, Unset):
            end_location = self.end_location.to_dict() if self.end_location else None

        unassign_not_optimal = self.unassign_not_optimal
        commit = self.commit
        created_by = self.created_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "assignees": assignees,
                "state": state,
                "tasks": tasks,
                "total_distance": total_distance,
                "total_duration": total_duration,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if objective is not UNSET:
            field_dict["objective"] = objective
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if start_location is not UNSET:
            field_dict["start_location"] = start_location
        if end_location is not UNSET:
            field_dict["end_location"] = end_location
        if unassign_not_optimal is not UNSET:
            field_dict["unassign_not_optimal"] = unassign_not_optimal
        if commit is not UNSET:
            field_dict["commit"] = commit
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        assignees = cast(List[str], d.pop("assignees"))

        state = RouteOptimizationSerializerV2StateEnum(d.pop("state"))

        tasks = cast(List[str], d.pop("tasks"))

        total_distance = d.pop("total_distance")

        total_duration = RouteOptimizationSerializerV2TotalDuration.from_dict(d.pop("total_duration"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_objective(data: object) -> Union[None, ObjectiveEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _objective_type_0 = data
                objective_type_0: Union[Unset, ObjectiveEnum]
                if isinstance(_objective_type_0, Unset):
                    objective_type_0 = UNSET
                else:
                    objective_type_0 = ObjectiveEnum(_objective_type_0)

                return objective_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ObjectiveEnum, Unset], data)

        objective = _parse_objective(d.pop("objective", UNSET))

        _start_time = d.pop("start_time", UNSET)
        start_time: Union[Unset, None, datetime.datetime]
        if _start_time is None:
            start_time = None
        elif isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _start_location = d.pop("start_location", UNSET)
        start_location: Union[Unset, None, RouteOptimizationSerializerV2StartLocation]
        if _start_location is None:
            start_location = None
        elif isinstance(_start_location, Unset):
            start_location = UNSET
        else:
            start_location = RouteOptimizationSerializerV2StartLocation.from_dict(_start_location)

        _end_location = d.pop("end_location", UNSET)
        end_location: Union[Unset, None, RouteOptimizationSerializerV2EndLocation]
        if _end_location is None:
            end_location = None
        elif isinstance(_end_location, Unset):
            end_location = UNSET
        else:
            end_location = RouteOptimizationSerializerV2EndLocation.from_dict(_end_location)

        unassign_not_optimal = d.pop("unassign_not_optimal", UNSET)

        commit = d.pop("commit", UNSET)

        created_by = d.pop("created_by", UNSET)

        route_optimization_serializer_v2 = cls(
            id=id,
            url=url,
            account=account,
            assignees=assignees,
            state=state,
            tasks=tasks,
            total_distance=total_distance,
            total_duration=total_duration,
            created_at=created_at,
            updated_at=updated_at,
            objective=objective,
            start_time=start_time,
            start_location=start_location,
            end_location=end_location,
            unassign_not_optimal=unassign_not_optimal,
            commit=commit,
            created_by=created_by,
        )

        route_optimization_serializer_v2.additional_properties = d
        return route_optimization_serializer_v2

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

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import lapidary_base.absent
import uuid


class TaskMetadataUnassignedDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TaskMetadataAssignedDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TaskMetadataAcceptedDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TaskMetadataTransitDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TaskMetadataActiveDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TaskMetadataCompletedDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TaskMetadataFailedDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TaskMetadataCancelledDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TaskMetadata(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    url: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    task: typing.Annotated[str, pydantic.Field()]

    events_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    task_event_notes_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    documents_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    signatures_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    forms_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    forms_completed_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    last_task_event_notes: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    unassigned_duration: typing.Annotated[
        typing.Union[
            TaskMetadataUnassignedDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    assigned_duration: typing.Annotated[
        typing.Union[
            TaskMetadataAssignedDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    accepted_duration: typing.Annotated[
        typing.Union[
            TaskMetadataAcceptedDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    transit_duration: typing.Annotated[
        typing.Union[
            TaskMetadataTransitDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    active_duration: typing.Annotated[
        typing.Union[
            TaskMetadataActiveDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    completed_duration: typing.Annotated[
        typing.Union[
            TaskMetadataCompletedDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    failed_duration: typing.Annotated[
        typing.Union[
            TaskMetadataFailedDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    cancelled_duration: typing.Annotated[
        typing.Union[
            TaskMetadataCancelledDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    unassigned_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    assigned_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    accepted_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    transit_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    active_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    completed_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    failed_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    cancelled_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    last_unassigned_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_assigned_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_accepted_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_transit_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_active_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_completed_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_failed_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_cancelled_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TaskMetadataUnassignedDuration.update_forward_refs()
TaskMetadataAssignedDuration.update_forward_refs()
TaskMetadataAcceptedDuration.update_forward_refs()
TaskMetadataTransitDuration.update_forward_refs()
TaskMetadataActiveDuration.update_forward_refs()
TaskMetadataCompletedDuration.update_forward_refs()
TaskMetadataFailedDuration.update_forward_refs()
TaskMetadataCancelledDuration.update_forward_refs()
TaskMetadata.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent
import uuid


class TasksAcceptCreateFormat(enum.Enum):
    json = "json"
    xml = "xml"


class TasksAcceptCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            TasksAcceptCreateFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="format",
        ),
    ] = lapidary_base.absent.ABSENT

    p_id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.path,
            alias="id",
        ),
    ]

    q_order__orderer__company: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__company",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__company__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__company__icontains",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__company__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__company__iexact",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__company__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__company__istartswith",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__emails__contained_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__emails__contained_by",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__emails__contains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__emails__contains",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__emails__overlap: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__emails__overlap",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__name: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__name",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__name__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__name__icontains",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__name__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__name__iexact",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__name__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__name__istartswith",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__notes: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__notes",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__notes__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__notes__icontains",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__notes__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__notes__iexact",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__notes__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__notes__istartswith",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__phones__contained_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__phones__contained_by",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__phones__contains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__phones__contains",
        ),
    ] = lapidary_base.absent.ABSENT

    q_order__orderer__phones__overlap: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="order__orderer__phones__overlap",
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TasksAcceptCreate.update_forward_refs()

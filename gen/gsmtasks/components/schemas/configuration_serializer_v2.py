from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.configuration_notification
import lapidary_base.absent
class ConfigurationSerializerV2Auth(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class ConfigurationSerializerV2Features(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class ConfigurationSerializerV2Templates(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class ConfigurationSerializerV2Tracking(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class ConfigurationSerializerV2Permissions(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class ConfigurationSerializerV2LegacyViews(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class ConfigurationSerializerV2(pydantic.BaseModel):
    id: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    account: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    user: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    is_staff: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    app: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    version: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    auth: typing.Annotated[
        ConfigurationSerializerV2Auth,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    settings: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    defaults: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    features: typing.Annotated[
        ConfigurationSerializerV2Features,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    templates: typing.Annotated[
        ConfigurationSerializerV2Templates,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    tracking: typing.Annotated[
        ConfigurationSerializerV2Tracking,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    notifications: typing.Annotated[
        list[
            gsmtasks.components.schemas.configuration_notification.ConfigurationNotification,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    permissions: typing.Annotated[
        ConfigurationSerializerV2Permissions,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    legacy_views: typing.Annotated[
        ConfigurationSerializerV2LegacyViews,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    location: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    is_client_role: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

ConfigurationSerializerV2Auth.update_forward_refs()
ConfigurationSerializerV2Features.update_forward_refs()
ConfigurationSerializerV2Templates.update_forward_refs()
ConfigurationSerializerV2Tracking.update_forward_refs()
ConfigurationSerializerV2Permissions.update_forward_refs()
ConfigurationSerializerV2LegacyViews.update_forward_refs()
ConfigurationSerializerV2.update_forward_refs()

from enum import Enum


class RouteOptimizationSerializerV2StateEnum(str, Enum):
    PENDING = "pending"
    STARTED = "started"
    READY = "ready"
    COMPLETED = "completed"
    OVER_QUOTA = "over_quota"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)

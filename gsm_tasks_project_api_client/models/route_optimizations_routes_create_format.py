from enum import Enum


class RouteOptimizationsRoutesCreateFormat(str, Enum):
    JSON = "json"
    XML = "xml"

    def __str__(self) -> str:
        return str(self.value)

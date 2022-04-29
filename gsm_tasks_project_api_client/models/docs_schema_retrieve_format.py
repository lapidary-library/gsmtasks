from enum import Enum


class DocsSchemaRetrieveFormat(str, Enum):
    JSON = "json"
    YAML = "yaml"

    def __str__(self) -> str:
        return str(self.value)

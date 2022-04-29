from enum import Enum


class FeatureAddressAutosuggestProviderEnum(str, Enum):
    GOOGLE = "google"
    HEREMAPS = "heremaps"
    REGIO = "regio"
    JANASETA = "janaseta"

    def __str__(self) -> str:
        return str(self.value)

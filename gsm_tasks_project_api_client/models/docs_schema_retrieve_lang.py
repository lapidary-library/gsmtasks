from enum import Enum


class DocsSchemaRetrieveLang(str, Enum):
    DE = "de"
    EN = "en"
    ES = "es"
    ET = "et"
    FI = "fi"
    FR = "fr"
    IT = "it"
    LT = "lt"
    LV = "lv"
    PL = "pl"
    RU = "ru"
    SV = "sv"

    def __str__(self) -> str:
        return str(self.value)

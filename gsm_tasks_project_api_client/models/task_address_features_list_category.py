from enum import Enum


class TaskAddressFeaturesListCategory(str, Enum):
    ASSIGNMENT = "assignment"
    PICK_UP = "pick_up"
    DROP_OFF = "drop_off"
    WAREHOUSE = "warehouse"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class VehicleProfileEnum(str, Enum):
    BIKE = "bike"
    BUS = "bus"
    CAR = "car"
    FOOT = "foot"
    SCOOTER = "scooter"
    SMALL_TRUCK = "small_truck"
    TRUCK = "truck"

    def __str__(self) -> str:
        return str(self.value)

# Import utility functions
import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__) + "/../")))
from Utils import UtilityFunctions, DataType


class CANPacketField:
    def __init__(
        self,
        name: str,
        address: str,
        type: str,
        frequency: int,
        bit_range: str,
        unit: str = "",
        value: str = "",
    ):
        self.field_name = UtilityFunctions.sanitize(name)
        self.address = UtilityFunctions.is_valid_address(address)
        self.type = DataType(type)
        self.frequency = frequency
        self.bit_range = UtilityFunctions.get_bit_range(bit_range)
        self.unit = unit
        self.value = value

    def __str__(self) -> str:
        return f"{self.field_name} {self.address} {self.type} {self.frequency} {self.bit_range} {self.unit} {self.value}"


class CANPacket:
    def __init__(self, packet_name: str):
        self.packet_name = UtilityFunctions.sanitize(packet_name)
        self.fields: List[CANPacketField] = []

    def add_field(self, row):
        address = row[2] if len(self.fields) == 0 else self.fields[0].address
        frequency = (
            int(row[3][:-2]) if len(self.fields) == 0 else self.fields[0].frequency
        )
        self.fields.append(
            CANPacketField(row[4], address, row[5], frequency, row[6], row[7], row[8])
        )

    def __str__(self) -> str:
        return f"{self.packet_name}\n" + "\n".join(
            [str(field) for field in self.fields]
        )

# Import utility functions
import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__) + "/../")))
from Utils import UtilityFunctions, DataType


class TELPacketField:
    def __init__(
        self,
        name: str,
        type: str,
        unit: str = "",
    ):
        self.field_name = UtilityFunctions.sanitize(name)
        self.type = DataType(type)
        self.unit = unit

    def __str__(self) -> str:
        return f"{self.field_name} {self.type} {self.unit}"


class TELPacket:
    def __init__(self, packet_name: str):
        self.packet_name = UtilityFunctions.sanitize(packet_name)
        self.fields: List[TELPacketField] = []
        self.is_array = None

    def add_field(self, row):
        if row[10].lower() == 'yes' or row[10].lower() == 'true' or row[10].lower() == 'y':
            self.is_array = True
        self.fields.append(TELPacketField(row[4], row[5], row[7]))

    def __str__(self) -> str:
        return f"{self.packet_name}\n" + "\n".join(
            [str(field) for field in self.fields]
        )

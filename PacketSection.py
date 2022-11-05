from Utils import ValidTypes

# Data Type class
# This class is used to store the data type of a packet section
# It is used to validate the data type of a packet section
# It is also used to help generate the different classes
class DataType:
    def __init__(self, type: str):
        if not self._is_valid_type(type):
            raise ValueError(f"Invalid type: {type}")
        self.base_type = type

    def _is_valid_type(self, type) -> bool:
        return type in ValidTypes

    def size(self) -> int:
        return ValidTypes[self.base_type]

    def typescript(self) -> str:
        if (
            self.base_type == "uchar"
            or self.base_type == "float"
            or self.base_type == "short uint"
            or self.base_type == "uint"
        ):
            return "number"
        elif self.base_type == "boolean":
            return "boolean"

    def __str__(self) -> str:
        return self.base_type


class DataField:
    def __init__(self, name: str, offset: int, type: str):
        self.name = name
        self.offset = offset
        self.type = DataType(type)

    def __str__(self) -> str:
        return f"{self.name} {self.offset} {self.type}"


class PacketSection:
    def __init__(self, section_name: str):
        self.section_name = section_name
        self.section_data = []

    def __str__(self):
        return f"{self.section_name}\n" + "\n".join(
            [str(field) for field in self.section_data]
        )

    def _is_valid_offset(self, offset: int) -> bool:
        return (
            offset == self.section_data[-1].offset + self.section_data[-1].type.size()
            if self.section_data
            else True
        )

    def add_field(self, row: list):
        field_name = row[1]
        field_offset = int(row[2])
        field_type = row[3] if row[4] != "boolean" else row[4]
        if not self._is_valid_offset(field_offset):
            raise ValueError(f"Invalid offset: {field_offset}")
        self.section_data.append(DataField(field_name, field_offset, field_type))

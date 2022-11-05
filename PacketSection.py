from Utils import ValidTypes, UtilityFunctions

# Data Type class
# This class is used to store the data type of a packet section
# It is used to validate the data type of a packet section
# It is also used to help generate the different classes


class DataField:
    def __init__(self, name: str, offset: int, type: str):
        self.name = name
        self.offset = offset
        self.type = DataType(type)

    def __str__(self) -> str:
        return f"{self.name} {self.offset} {self.type}"


class PacketSection:
    def __init__(self, section_name: str):
        self.section_name = UtilityFunctions.sanitize(section_name)
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
        field_name = UtilityFunctions.sanitize(row[4])
        field_offset = int(row[2])
        field_type = row[3] if row[4] != "boolean" else row[4]
        if not self._is_valid_offset(field_offset):
            raise ValueError(f"Invalid offset: {field_offset}")
        self.section_data.append(DataField(field_name, field_offset, field_type))

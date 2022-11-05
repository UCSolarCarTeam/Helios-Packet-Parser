import re
from typing import List

# Dictionary of valid types and their sizes
# i.e. uchar is a valid type of size 1 byte
ValidTypes = {
    "uchar": 1,
    "float": 4,
    "uint8": 1,
    "boolean": 1,
    "uint32": 4,
    "uint16": 2,
    "-": 0
}

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

    def c(self) -> str:
        if self.base_type == "uchar":
            return "uint8_t"
        elif self.base_type == "float":
            return "float"
        elif self.base_type == "uint8":
            return "uint8_t"
        elif self.base_type == "boolean":
            return "bool"
        elif self.base_type == "uint32":
            return "uint32_t"
        elif self.base_type == "uint16":
            return "uint16_t"

    def __str__(self) -> str:
        return self.base_type

class UtilityFunctions:
    def _camelCase(string) -> str:
        return "".join(x for x in string.title() if not x.isspace())

    def _remove_spaces(string) -> str:
        return "".join(x for x in string if not x.isspace())

    def _remove_invalid_chars(string) -> str:
        string.replace(".", "_")
        return "".join(x for x in string if x.isalnum() or x == "_")

    def _handle_number_prefix(string) -> str:
        if string[0].isdigit() or "." in string:
            raise ValueError(f"Invalid string: {string}")
        return string

    def is_valid_address(address: str) -> str:
        pattern = re.compile(r"0x[0-9a-fA-F]{3}")
        if not pattern.match(address):
            raise ValueError(f"Invalid address: {address}")
        return address

    def is_valid_type(type: str) -> str:
        if type not in ValidTypes:
            raise ValueError(f"Invalid type: {type}")
        return type

    def get_bit_range(bit_range: str) -> List:
        if bit_range == "-":
            return []
        return [int(x) for x in bit_range.split("-")]

    def sanitize(string) -> str:
        string = UtilityFunctions._remove_spaces(string)
        string = UtilityFunctions._remove_invalid_chars(string)
        return UtilityFunctions._handle_number_prefix(string)

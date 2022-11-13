import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__) + "/../")))
from Utils import UtilityFunctions


class CGen:
    def __init__(self, sections):
        self.sections = sections

    def generate(self, output_folderpath) -> None:
        # Generate paths for header and source files
        header_filepaths = [
            os.path.join(output_folderpath, file)
            for file in [f"{section.section_name}.h" for section in self.sections]
        ]

        # Create folders for header files
        for header_filepath in header_filepaths:
            os.makedirs(os.path.dirname(header_filepath), exist_ok=True)

        # Generate header files
        for section, header_filepath in zip(self.sections, header_filepaths):
            with open(header_filepath, "w") as f:
                f.write("#pragma once\n\n")
                f.write(f"#include <stdint.h>\n\n")
                # Write defines for packed addresses
                for packet in section.packets:
                    for field in packet.fields:
                        f.write(
                            f"#define {UtilityFunctions.sanitize(field.field_name).upper()}_CAN_ID {field.address}\n"
                        )
                f.write("\n")

                # Generate packet structs
                for packet in section.packets:
                    f.write(f"typedef struct {packet.packet_name}\n{{\n")
                    for field in packet.fields:
                        if field.field_name.lower() == "reserved":
                            continue
                        f.write(
                            f"    {field.type.c()} {UtilityFunctions.sanitize(field.field_name)};\n"
                        )
                    f.write("} " + packet.packet_name + ";\n")

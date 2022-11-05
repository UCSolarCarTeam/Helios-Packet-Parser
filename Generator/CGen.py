import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__) + "/../")))
from Utils import UtilityFunctions

class CGen:
    def __init__(self, packets):
        self.packets = packets
    
    def generate(self, output_folderpath) -> None:
        # Generate paths for header and source files
        header_filepaths = [os.path.join(output_folderpath, file) for file in [f"{packet.packet_name}.h" for packet in self.packets]]

        # Create folders for header files
        for header_filepath in header_filepaths:
            os.makedirs(os.path.dirname(header_filepath), exist_ok=True)
        
        # Generate header files
        for packet, header_filepath in zip(self.packets, header_filepaths):
            with open(header_filepath, "w") as f:
                f.write(f"#ifndef {packet.packet_name.upper()}_H\n")
                f.write(f"#define {packet.packet_name.upper()}_H\n\n")
                f.write(f"#include <stdint.h>\n\n")
                f.write(f"typedef struct {packet.packet_name} {{\n")
                for field in packet.fields:
                    if field.field_name.lower() == 'reserved':
                        continue
                    f.write(f"    {field.type.c()} {UtilityFunctions.sanitize(field.field_name)};\n")
                f.write("} " + packet.packet_name + ";\n\n")
                f.write(f"#endif // {packet.packet_name.upper()}_H\n")

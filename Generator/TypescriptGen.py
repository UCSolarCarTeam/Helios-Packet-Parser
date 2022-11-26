import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__) + "/../")))
from Utils import UtilityFunctions

class TypescriptGen:
    def __init__(self, sections):
        self.sections = sections
    
    def generate(self, output_folderpath) -> None:
        file_path = os.path.join(os.path.join(output_folderpath, 'TS'), "ITelemetryData.ts")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as f:
            f.write("export interface ITelemetryData {\n")
            for section in self.sections:
                for packet in section.packets:
                    name = UtilityFunctions.sanitize(packet.packet_name)
                    dtype = UtilityFunctions.ts_interface_name(packet.packet_name)
                    if packet.is_array:
                        f.write(f"    {name}: {dtype}[];\n")
                    else:
                        f.write(f"    {name}: {dtype};\n")
            f.write("}\n")

            for section in self.sections:
                for packet in section.packets:
                    f.write(f"\nexport interface {UtilityFunctions.ts_interface_name(packet.packet_name)} {{\n")
                    for field in packet.fields:
                        f.write(f"    {UtilityFunctions.sanitize(field.field_name)}: {field.type.ts()};\n")
                    f.write("}\n")


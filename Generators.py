from Utils import *


class TypescriptGenerator:
    def __init__(self, packet_sections):
        self.packet_sections = packet_sections

    def generate(self, output_filepath) -> None:
        with open(output_filepath, "w") as f:
            for section in self.packet_sections:
                f.write(
                    f"export interface {self._camelCase(section.section_name)} {{\n"
                )
                for field in section.section_data:
                    f.write(
                        f"  {self.sanitize(field.name)}: {field.type.typescript()};\n"
                    )
                f.write("}\n\n")

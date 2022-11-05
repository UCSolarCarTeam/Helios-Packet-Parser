class TypescriptGenerator:
    def __init__(self, packet_sections):
        self.packet_sections = packet_sections

    def _camelCase(self, string) -> str:
        return "".join(x for x in string.title() if not x.isspace())

    def _remove_spaces(self, string) -> str:
        return "".join(x for x in string if not x.isspace())

    def _remove_invalid_chars(self, string) -> str:
        return "".join(x for x in string if x.isalnum() or x == "_" or x == ".")

    def _handle_number_prefix(self, string) -> str:
        if string[0].isdigit() or "." in string:
            return f"'{string}'"
        return string

    def _sanitize(self, string) -> str:
        string = self._remove_spaces(string)
        string = self._remove_invalid_chars(string)
        return self._handle_number_prefix(string)

    def generate(self, output_filepath) -> None:
        with open(output_filepath, "w") as f:
            for section in self.packet_sections:
                f.write(
                    f"export interface {self._camelCase(section.section_name)} {{\n"
                )
                for field in section.section_data:
                    f.write(
                        f"  {self._sanitize(field.name)}: {field.type.typescript()};\n"
                    )
                f.write("}\n\n")

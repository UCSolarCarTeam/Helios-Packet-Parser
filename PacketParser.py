import csv

from PacketSection import PacketSection


class PacketParser:
    def __init__(self, filename):
        self.filename = filename
        self.packet_sections = []

    def parse(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "Section":
                    continue
                if row[0] != "":
                    self.packet_sections.append(PacketSection(row[0]))
                self.packet_sections[-1].add_field(row)

    def get_pakcet_sections(self):
        return self.packet_sections

    def __str__(self):
        return "\n".join([str(section) + "\n" for section in self.packet_sections])

import csv

from Packet.CANPacket import CANPacket
from PacketSection import PacketSection


class PacketParser:
    def __init__(self, filename):
        self.filename = filename
        self.sections = []

    def _parse_row(self, row):
        if row[0] != "":
            self.sections.append(PacketSection(row[0]))
        if row[1] != "":
            # Check that the protocol is specified
            if row[-1] == "":
                raise ValueError("Protocol not specified")
            # Check if the protocol is CAN
            if row[-1] == "CAN":
                self.sections[-1].add_packet(CANPacket(row[1]))
        self.sections[-1].get_last_packet().add_field(row)

    def parse(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "Section":
                    continue
                self._parse_row(row)

    def get_sections(self):
        return self.sections

    def __str__(self):
        return "\n".join([str(section) + "\n" for section in self.sections])

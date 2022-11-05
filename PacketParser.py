import csv
from PacketSection import PacketSection
from Packet.CANPacket import CANPacket

class PacketParser:
    def __init__(self, filename):
        self.filename = filename
        self.packets = []

    def _parse_row(self, row):
        if row[1] != "":
            # Check that the protocol is specified
            if row[-1] == "":
                raise ValueError("Protocol not specified")
            # Check if the protocol is CAN
            if row[-1] == "CAN":
                self.packets.append(CANPacket(row[1]))
        self.packets[-1].add_field(row)

    def parse(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "Section":
                    continue
                if row[]
                self._parse_row(row)

    def get_packets(self):
        return self.packets

    def __str__(self):
        return "\n".join([str(section) + "\n" for section in self.packets])

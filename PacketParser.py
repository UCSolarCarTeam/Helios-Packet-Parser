import csv

from Packet.CANPacket import CANPacket
from Packet.TELPacket import TELPacket
from PacketSection import PacketSection
from Utils import PacketType

class PacketParser:
    def __init__(self, filename):
        self.filename = filename
        self.sections = []
    
    def _parse_row_tel(self, row):
        if row[0] != "":
            if row[-1] == "TEL":
                self.sections.append(PacketSection(row[0], PacketType.TEL))
            else:
                raise ValueError("Protocol not TEL")
        if row[1] != "":
            if row[-1] == "TEL":
               self.sections[-1].add_packet(TELPacket(row[1]))
        self.sections[-1].get_last_packet().add_field(row)
    
    def _parse_row_can(self, row):
        if row[0] != "":
            if row[-1] == "CAN":
                self.sections.append(PacketSection(row[0], PacketType.CAN))
            else:
                raise ValueError("Protocol not CAN")
        if row[1] != "":
            if row[-1] == "CAN":
                self.sections[-1].add_packet(CANPacket(row[1]))
        self.sections[-1].get_last_packet().add_field(row)
    
    def parse(self,dtype):
        with open(self.filename) as f:
            reader = csv.reader(f)
            if dtype == "CAN":
                for row in reader:
                    if row[0] == "Section":
                        continue
                    self._parse_row_can(row)
            if dtype == "TEL":
                for row in reader:
                    self._parse_row_tel(row)


    def get_sections(self, dtype):
        return [section for section in self.sections if section.type == dtype]

    def __str__(self):
        return "\n".join([str(section) + "\n" for section in self.sections])

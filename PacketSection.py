from Utils import UtilityFunctions, PacketType

class PacketSection:
    def __init__(self, section_name: str, section_type: int):
        self.section_name = UtilityFunctions.sanitize(section_name)
        self.packets = []
        self.type = section_type

    def __str__(self):
        return f"{self.section_name}\n" + "\n".join(
            [str(packet) for packet in self.packets]
        )

    def add_packet(self, packet):
        self.packets.append(packet)

    def get_last_packet(self):
        return self.packets[-1]

from Utils import UtilityFunctions


class PacketSection:
    def __init__(self, section_name: str):
        self.section_name = UtilityFunctions.sanitize(section_name)
        self.packets = []

    def __str__(self):
        return f"{self.section_name}\n" + "\n".join(
            [str(packet) for packet in self.packets]
        )

    def add_packet(self, packet):
        self.packets.append(packet)

    def get_last_packet(self):
        return self.packets[-1]

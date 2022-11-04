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
                if row[0] == 'Section':
                    continue
                if row[0] != '':
                    self.packet_sections.append(PacketSection(row[0]))
                self.packet_sections[-1].add_field(row[1], int(row[2]), row[3])
    
    def __str__(self):
        return '\n'.join([str(section) for section in self.packet_sections])

if __name__ == '__main__':
    parser = PacketParser('test_packet.csv')
    parser.parse()
    print(parser)
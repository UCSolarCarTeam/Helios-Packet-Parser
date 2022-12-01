import os

from Generator.CGen import CGen
from Generator.TypescriptGen import TypescriptGen
from PacketParser import PacketParser
from Utils import PacketType

if __name__ == "__main__":
    for file in os.listdir('.'):
        if ".csv" in file:
            if "CAN" in file:
                parser = PacketParser(file)
                parser.parse('CAN')
                CGen(parser.get_sections(PacketType.CAN)).generate(file[:-4] + "_output")
            if "TEL" in file:
                parser = PacketParser(file)
                parser.parse('TEL')
                TypescriptGen(parser.get_sections(PacketType.TEL)).generate(file[:-4] + "_output")
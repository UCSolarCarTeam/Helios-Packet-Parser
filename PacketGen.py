import os
import argparse

from Generator.CGen import CGen
from Generator.TypescriptGen import TypescriptGen
from PacketParser import PacketParser
from Utils import PacketType

if __name__ == "__main__":
    # Parse the command line arguments
    arg_parser = argparse.ArgumentParser(description="Packet Generator")
    arg_parser.add_argument(
        "-d",
        "--directory",
        help="The directory of files to parse",
        required=False,
        default=".",
    )
    arg_parser.add_argument(
        "-o",
        "--output",
        help="The name of the output folder",
        required=False,
        default="output",
    )
    args = arg_parser.parse_args()

    if os.path.isdir(args.directory):
        for file in os.listdir(args.directory):
            if file[-4:] == ".csv":
                if "CAN" in file:
                    parser = PacketParser(file)
                    parser.parse('CAN')
                    CGen(parser.get_sections(PacketType.CAN)).generate(args.output)
                if "TEL" in file:
                    parser = PacketParser(file)
                    parser.parse('TEL')
                    TypescriptGen(parser.get_sections(PacketType.TEL)).generate(args.output)
    else:
        raise ValueError("Invalid directory chosen")
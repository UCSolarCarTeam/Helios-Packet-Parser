import argparse

from Generator.CGen import CGen
from Generator.TypescriptGen import TypescriptGen
from PacketParser import PacketParser
from Utils import PacketType

if __name__ == "__main__":
    # Parse the command line arguments
    arg_parser = argparse.ArgumentParser(description="Packet Generator")
    arg_parser.add_argument(
        "-f", "--filename", help="The name of the file to parse", required=True
    )
    arg_parser.add_argument(
        "-o",
        "--output",
        help="The name of the output folder",
        required=False,
        default="output",
    )
    args = arg_parser.parse_args()

    parser = PacketParser(args.filename)
    parser.parse()
    CGen(parser.get_sections(PacketType.CAN)).generate(args.output)
    TypescriptGen(parser.get_sections(PacketType.TEL)).generate(args.output)

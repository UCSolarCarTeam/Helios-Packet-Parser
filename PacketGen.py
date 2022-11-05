import argparse

from Generators import TypescriptGenerator
from PacketParser import PacketParser

if __name__ == "__main__":
    # Parse the command line arguments
    arg_parser = argparse.ArgumentParser(description="Packet Generator")
    arg_parser.add_argument("filename", help="The name of the file to parse")
    args = arg_parser.parse_args()

    parser = PacketParser(args.filename)
    parser.parse()
    print(parser)
    ts_gen = TypescriptGenerator(parser.get_pakcet_sections())
    ts_gen.generate("telemetry-data.interface.ts")

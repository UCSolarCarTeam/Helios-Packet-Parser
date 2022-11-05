import argparse

from Generator.CGen import CGen
from PacketParser import PacketParser

if __name__ == "__main__":
    # Parse the command line arguments
    arg_parser = argparse.ArgumentParser(description="Packet Generator")
    arg_parser.add_argument("filename", help="The name of the file to parse")
    args = arg_parser.parse_args()

    parser = PacketParser(args.filename)
    parser.parse()
    print(parser)
    CGen(parser.get_packets()).generate('output')
"""
Generates a gcode file to set your 3D printer's bed or enclosure temperature to a
fixed temperature for a set amount of time in order to dry spools of filament.
"""

import argparse
import os
import sys

from filament_dryer_script_generator import create_file


def main():
    """
    Generates a gcode file to set your 3D printer's bed or enclosure temperature to a
    fixed temperature for a set amount of time in order to dry spools of filament.
    """

    parser = argparse.ArgumentParser(
        prog="filament_dryer_script_generator", description=__doc__
    )

    parser.add_argument("filename", type=str, help="(str) output filename")
    parser.add_argument("time", type=int, help="(int) drying time, in minutes")
    parser.add_argument(
        "temperature",
        type=int,
        help="(int) drying temperature, in degrees Celsius",
    )
    parser.add_argument(
        "--bed", action="store_true", help="use the bed heater for drying"
    )
    parser.add_argument(
        "--chamber", action="store_true", help="use the chamber heater for drying"
    )

    args = parser.parse_args()

    print("Generating Dryer Script")
    print("  File:    %s" % os.path.split(args.filename)[1])
    print("  Time:    %d mins" % args.time)
    print("  Temp:    %d deg C" % args.temperature)
    print("  Bed:     %r" % args.bed)
    print("  Chamber: %r" % args.chamber)

    create_file(args.filename, args.time, args.temperature, args.bed, args.chamber)

    print("Done.")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

#!/usr/bin/env python
"""
Convert a file from minutes and seconds to seconds.

Take a filepath as input to a file in the format:
start_time end_time other data...
(time values in the format minutes.seconds)
and convert all time values to seconds

Arguments:
    input file
    output file
"""

import argparse


def mins2secs(labfile, outfile):
    """Run the conversion between minutes to seconds on the file."""
    with open(labfile, 'r') as labfile, open(outfile, 'w') as outfile:
        output = ''
        for entry in labfile:
            entry = entry.split()
            n = 2
            i = 0
            while i < 2:
                time = entry[i].split('.')
                time = int(time[0])*60 + int(time[1])
                output = ''.join((output, str(time) + ' '))
                i += 1
            output = ''.join((output, ' '.join(entry[n:]), '\n'))
        print output
        outfile.write(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert time of entries in '
                                     'minute.seconds format to seconds')
    parser.add_argument('labfile', type=str,
                        help='Location of file to convert')
    parser.add_argument('outfile', type=str,
                        help='Location of file to output')
    args = parser.parse_args()

    mins2secs(args.labfile, args.outfile)

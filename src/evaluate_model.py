import argparse
import os

def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('DEVDIR', help='The directory where unlabeled CSV files are')
    parser.add_argument('OUTPUTFILE', help='The file contains output labels')

    args = parser.parse_args()
    dev_dir = args.DEVDIR
    output_file = args.OUTPUTFILE

    print()


__main__()
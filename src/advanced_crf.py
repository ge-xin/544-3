import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUTDIR', help='reads in a directory of CSV files (INPUTDIR), train a CRFsuite model')
    parser.add_argument('TESTDIR', help='tag the CSV files in (TESTDIR)')
    parser.add_argument('OUTPUTFILE', help='print the output labels to OUTPUTFILE')

    args = parser.parse_args()
    input_dir = args.INPUTDIR
    test_dir = args.TESTDIR
    output_file = args.OUTPUTFILE

    print()
    print()

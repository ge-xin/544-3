import hw3_corpus_tool
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUTDIR', help='reads in a directory of CSV files (INPUTDIR), train a CRFsuite model')
    parser.add_argument('TESTDIR', help='tag the CSV files in (TESTDIR)')
    parser.add_argument('OUTPUTFILE', help='print the output labels to OUTPUTFILE')

    args = parser.parse_args()
    input_dir = args.INPUTDIR
    test_dir = args.TESTDIR
    output_file = args.OUTPUTFILE

    du_dict = hw3_corpus_tool.get_data(input_dir)

    for d in du_dict:
        # print(d)
        for i in d:
            act_tag = i.act_tag
            speaker = i.speaker
            pos = i.pos
            for p in pos:
                a = p.token
                b = p.posß
            text = i.text

            print(i)

    print()

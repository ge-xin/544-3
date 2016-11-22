import argparse
import os
import src.baseline_crf
import hw3_corpus_tool
from src.baseline_crf import dialog_feature

if __name__ == '__main__':
    parser1 = argparse.ArgumentParser()
    parser1.add_argument('DEVDIR', help='The directory where unlabeled CSV files are')
    parser1.add_argument('OUTPUTFILE', help='The file contains output labels')

    args = parser1.parse_args()
    dev_dir = args.DEVDIR
    output_file = args.OUTPUTFILE

    # output = open(output_file, 'r')

    du_dict = hw3_corpus_tool.get_data(dev_dir)

    feature_list_x = []
    feature_list_y = []
    for dialog in du_dict:
        dialog_x = []
        dialog_y = []
        dialog_feature(dialog, dialog_x, dialog_y)
        for x in dialog_x:
            feature_list_x.append(x)
        for y in dialog_y:
            feature_list_y.append(y)



    print()


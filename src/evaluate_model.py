import argparse
from src.baseline_crf import extract_feature

if __name__ == '__main__':
    parser1 = argparse.ArgumentParser()
    parser1.add_argument('DEVDIR', help='The directory where unlabeled CSV files are')
    parser1.add_argument('OUTPUTFILE', help='The file contains output labels')

    args = parser1.parse_args()
    dev_dir = args.DEVDIR
    output_file = args.OUTPUTFILE

    feature_list_x = []
    feature_list_y = []
    dialog_filenames = extract_feature(dev_dir, feature_list_x, feature_list_y)

    output = open(output_file, 'r')
    total = 0
    correct = 0
    for actual_dialog_y in feature_list_y:
        output.readline()
        for actual_utterance_tag in actual_dialog_y:
            total += 1
            # utterance_tag = output.readline().strip()
            if output.readline().strip() == actual_utterance_tag : correct += 1
        output.readline()

    precision = correct / total
    print(precision)


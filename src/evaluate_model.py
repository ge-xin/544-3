import argparse
from src.baseline_crf import extract_feature

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('DEVDIR', help='The directory where unlabeled CSV files are')
    parser.add_argument('OUTPUTFILE', help='The file contains output labels')
    parser.add_argument('--OTHEROUTPUTFILE')

    args = parser.parse_args()
    dev_dir = args.DEVDIR
    output_file = args.OUTPUTFILE

    if args.OTHEROUTPUTFILE:
        other_output_file = args.OTHEROUTPUTFILE
    else: other_output_file = None

    feature_list_x = []
    feature_list_y = []
    dialog_filenames = extract_feature(dev_dir, feature_list_x, feature_list_y)

    output = open(output_file, 'r')
    total = 0
    correct = 0
    other_correct = 0
    other_output = None
    if args.OTHEROUTPUTFILE:
        other_output = open(other_output_file, 'r')

    for actual_dialog_y in feature_list_y:
        output.readline()
        if args.OTHEROUTPUTFILE:
            other_output.readline()
        for actual_utterance_tag in actual_dialog_y:
            total += 1
            # utterance_tag = output.readline().strip()
            if output.readline().strip() == actual_utterance_tag : correct += 1

            if args.OTHEROUTPUTFILE:
                if other_output.readline().strip() == actual_utterance_tag: other_correct += 1

        output.readline()
        if args.OTHEROUTPUTFILE:
            other_output.readline()

    precision = correct / total
    print('{0:20} : {1:100}'.format('output: ', str(precision)))
    # print('output: ' + str(precision))
    if args.OTHEROUTPUTFILE:
        print('{0:20} : {1:100}'.format('advanced_output: ', str(other_correct/total)))
        # print('advanced_output: ' + str(other_correct/total))


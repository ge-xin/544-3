import argparse
import os
import hw3_corpus_tool
import pycrfsuite

# def utterance_feature(utterance, utterance_x, utterance_y):
#     act_tag = utterance.act_tag
#     speaker = utterance.speaker
#     pos = utterance.pos
#     for p in pos:
#         a = p.token
#         b = p.pos
#     text = utterance.text

def dialog_feature(dialog, dialog_x, dialog_y):

    for i in range(0, len(dialog)):
        cur_utterance = dialog[i]
        dialog_y.append(cur_utterance.act_tag)
        cur_utterance_x = []
        '''
            a feature for whether or not the speaker has changed in comparison with the previous utterance.
            a feature marking the first utterance of the dialogue.
        '''
        if(i == 0):
            cur_utterance_x.append('speaker_change:' + 'False')
            cur_utterance_x.append('first_utterance:' + 'True')
        else:
            pre_utterance = dialog[i - 1]
            if(pre_utterance.speaker != cur_utterance.speaker): cur_utterance_x.append('speaker_change:' + 'True')
            else: cur_utterance_x.append('speaker_change:' + 'False')
            cur_utterance_x.append('first_utterance:' + 'False')
        '''
        when pos = None, e.g. text = '<Laughter>', continue;, to avoid nullptr issue
        '''
        if cur_utterance.pos == None:
            dialog_x.append(cur_utterance_x)
            continue

        '''
            a feature for every token in the utterance (see the description of CRFsuite for an example).
        '''
        for j in range(0, len(cur_utterance.pos)):
            p = cur_utterance.pos[j]
            cur_utterance_x.append('token_'+str(j)+':'+p.token)

        '''
            a feature for every part of speech tag in the utterance (e.g., POS_PRP POS_RB POS_VBP POS_.).
        '''
        for j in range(0, len(cur_utterance.pos)):
            p = cur_utterance.pos[j]
            cur_utterance_x.append('pos_'+str(j)+':'+p.pos)
        '''
            push the cur_utterance_x into list_x
        '''
        dialog_x.append(cur_utterance_x)


    # for x in utterance_x:
    #     dialog_x.append(x)
    # for y in utterance_y:
    #     dialog_y.append(y)

    # print()

def extract_feature(input_dir, feature_list_x, feature_list_y):
    du_dict = hw3_corpus_tool.get_data(input_dir)

    for dialog in du_dict:
        dialog_x = []
        dialog_y = []
        dialog_feature(dialog, dialog_x, dialog_y)
        feature_list_x.append(dialog_x)
        feature_list_y.append(dialog_y)

def learn(input_dir):
    '''
    :param input_dir:
    :return:
    '''
    '''
        Feature extraction
    '''
    feature_list_x = []
    feature_list_y = []
    extract_feature(input_dir, feature_list_x, feature_list_y)

    '''
        Begin Fitting the model
    '''
    trainer = pycrfsuite.Trainer(verbose=True)
    # trainer.append(feature_list_x, feature_list_y)
    for xseq, yseq in zip(feature_list_x, feature_list_y):
        trainer.append(xseq, yseq)

    trainer.set_params({
        'c1': 1.0,   # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 100,  # stop earlier

        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })

    trainer.train('baseline_crf_model.crfsuite')

    print(trainer.logparser.last_iteration)
    print(len(trainer.logparser.iterations), end=' ')
    print(trainer.logparser.iterations[-1])
    # print()

def classify(test_dir, output_file):


    '''
       Feature extraction
    '''
    feature_list_x = []
    feature_list_y = []
    extract_feature(test_dir, feature_list_x, feature_list_y)

    '''
        classification/tagging
    '''
    tagger = pycrfsuite.Tagger()
    tagger.open('baseline_crf_model.crfsuite')

    for x in feature_list_x:
        print(tagger.tag(x))


    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUTDIR', help='reads in a directory of CSV files (INPUTDIR), train a CRFsuite model')
    parser.add_argument('TESTDIR', help='tag the CSV files in (TESTDIR)')
    parser.add_argument('OUTPUTFILE', help='print the output labels to OUTPUTFILE')

    args = parser.parse_args()
    input_dir = args.INPUTDIR
    test_dir = args.TESTDIR
    output_file = args.OUTPUTFILE

    # learn(input_dir)
    classify(test_dir, output_file)

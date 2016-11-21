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
    utterance_x = []
    utterance_y = []
    for i in range(0, len(dialog)):
        cur_utterance = dialog[i]
        utterance_y.append(cur_utterance.act_tag)
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
            utterance_x.append(cur_utterance_x)
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
        utterance_x.append(cur_utterance_x)

    # dialog_x.append(utterance_x)
    # dialog_y.append(utterance_y)
    for x in utterance_x:
        dialog_x.append(x)
    for y in utterance_y:
        dialog_y.append(y)

    print()

def learn(input_dir):
    '''
    :param input_dir:
    :return:
    '''
    '''
        Feature extraction
    '''
    du_dict = hw3_corpus_tool.get_data(input_dir)

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
    '''
        Begin Fitting the model
    '''
    trainer = pycrfsuite.Trainer(verbose=True)
    trainer.append(feature_list_x, feature_list_y)

    trainer.set_params({
        'c1': 1.0,   # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 250,  # stop earlier

        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })

    trainer.train('baseline_crf_model.crfsuite')

    print(trainer.logparser.last_iteration)
    print(len(trainer.logparser.iterations), end=' ')
    print(trainer.logparser.iterations[-1])
    print()

def classify():
    print()

def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUTDIR', help='reads in a directory of CSV files (INPUTDIR), train a CRFsuite model')
    parser.add_argument('TESTDIR', help='tag the CSV files in (TESTDIR)')
    parser.add_argument('OUTPUTFILE', help='print the output labels to OUTPUTFILE')

    args = parser.parse_args()
    input_dir = args.INPUTDIR
    test_dir = args.TESTDIR
    output_file = args.OUTPUTFILE

    learn(input_dir)


__main__()
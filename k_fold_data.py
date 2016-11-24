import os
import random
import shutil

k_dev_directory = 1


k_fold = 5
source = '/Users/Xin/Desktop/544_3_k_folded/'
dest = '/Users/Xin/Desktop/544_3_labeled_data_splited/'
train_directory = dest+'train/'
dev_directory = dest+'dev/'

if __name__ == '__main__':
    dirs = []
    for i in range(1, k_fold + 1):
        if i == k_dev_directory: continue
        dirs.append(source + str(i) + '/')

    data_lst = []
    data_name = []

    for d in dirs:
        for root, dirs, files in os.walk(d):
            for file in files:
                if file.endswith('.csv'):
                    abs_path = os.path.join(root, file)
                    data_lst.append(abs_path)
                    data_name.append(file)
                else: continue

    data_size = len(data_lst)

    '''
        combine train_directory data
    '''

    try:
        shutil.rmtree(dest)
    except:
        print('No dest directory for dev and train, continue')

    dirs = [dest, train_directory, dev_directory]
    for dir in dirs:
        try:
            os.stat(dir)
        except:
            os.mkdir(dir)

    for i in range(len(data_name)):
        shutil.copyfile(data_lst[i], train_directory + data_name[i])


    '''
        combine dev_directory data
    '''

    dirs = []
    for i in range(1, k_fold + 1):
        if i != k_dev_directory: continue
        dirs.append(source + str(i) + '/')

    data_lst = []
    data_name = []

    for d in dirs:
        for root, dirs, files in os.walk(d):
            for file in files:
                if file.endswith('.csv'):
                    abs_path = os.path.join(root, file)
                    data_lst.append(abs_path)
                    data_name.append(file)
                else: continue

    data_size = len(data_lst)

    train_directory_fetch = round(data_size / 5)

    '''
        combine dev_directory data
    '''

    for i in range(len(data_name)):
        shutil.copyfile(data_lst[i], dev_directory + data_name[i])

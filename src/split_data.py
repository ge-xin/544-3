import os
import random
import shutil

source = '/Users/Xin/Desktop/544-3/labeled_data'
split_for_train = 0.75
dest = '/Users/Xin/Desktop/544_3_labeled_data_splited/'
train_directory = dest+'train/'
dev_directory = dest+'dev/'

def __main():
    data_lst = []
    data_name = []
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith('.csv'):
                abs_path = os.path.join(root, file)
                data_lst.append(abs_path)
                data_name.append(file)
            else: continue

    train_size = len(data_lst)

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

    train_fetch = round(split_for_train * train_size)
    while train_fetch > 0:
        i = random.randint(0, (len(data_lst) - 1))
        shutil.copyfile(data_lst[i], train_directory + data_name[i])
        data_lst.remove(data_lst[i])
        data_name.remove(data_name[i])
        train_fetch -= 1

    '''
       copy rest of file as dev data
    '''
    for i in range(0, len(data_lst)):
        shutil.copyfile(data_lst[i], dev_directory + data_name[i])


__main()
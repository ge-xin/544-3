import os
import random
import shutil

source = '/Users/Xin/Desktop/544-3/labeled_data'
k_fold = 5
dest = '/Users/Xin/Desktop/544_3_k_folded/'


if __name__ == '__main__':
    data_lst = []
    data_name = []
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith('.csv'):
                abs_path = os.path.join(root, file)
                data_lst.append(abs_path)
                data_name.append(file)
            else: continue

    data_size = len(data_lst)

    try:
        shutil.rmtree(dest)
    except:
        print('No dest directory for dev and train, continue')


    dirs = [dest]
    for i in range(1, k_fold + 1):
        dirs.append(dest + str(i) + '/')
    for dir in dirs:
        try:
            os.stat(dir)
        except:
            os.mkdir(dir)

    train_fetch = round(data_size / 5)

    for i in range(1, k_fold):
        fetch = train_fetch
        while fetch > 0:
            k = random.randint(0, (len(data_lst) - 1))
            new_dest = dest + str(i) + '/' + data_name[k]
            shutil.copyfile(data_lst[k], new_dest)
            data_lst.remove(data_lst[k])
            data_name.remove(data_name[k])
            fetch -= 1
    '''
       copy rest of file to folder k
    '''
    for i in range(len(data_name)):
        shutil.copyfile(data_lst[i], dest+ str(k_fold) + '/' + data_name[i])

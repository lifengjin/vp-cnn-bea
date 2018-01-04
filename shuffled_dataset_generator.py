import os
import re

from chatscript_file_generator import *
import random

def shuffle_data(dataset_list, dialogues, shuffled_data_file, indices_file):
    len_dataset = len(dataset_list)
    if os.path.exists(indices_file):
        indices = open(indices_file).readlines()
        indices = [eval(x) for x in indices]
    else:
        indices = list(range(len_dataset))
        random.shuffle(indices)
    shuffled_data_file_handle = open(shuffled_data_file, 'w', encoding='utf8')
    indices_file_handle = open(indices_file, 'w', encoding='utf8')
    for index in indices:
        if isinstance(index, tuple):
            index = dialogues.index(index)
        print(dataset_list[index].strip(), file=shuffled_data_file_handle)
        print(dialogues[index], file=indices_file_handle)
    indices_file_handle.close()
    indices_file_handle.close()

def generate_simple_dataset(dialogue_file, data_file):
    new_data_file = 'wilkins_' + dialogue_file
    with open(dialogue_file, encoding='utf8') as di, open(data_file) as da, open(new_data_file,
                                                                          'w', encoding='utf8') as \
            out:
        dialogues = []
        for line in di:
            if line.startswith('#S'):
                pass
            else:
                dialogues.append(line.split('\t')[0])
        data_lines = da.readlines()
        assert len(dialogues) == len(data_lines)
        for index, sent in enumerate(dialogues):
            label = data_lines[index].split('\t')[0]
            print('\t'.join([label, sent]), file=out)
    return new_data_file

def main(data_file, dialogue_file, shuffled_data_file, indices_file):
    dialogues = read_in_dialogues(dialogue_file)
    data_list = open(data_file, encoding='utf8').readlines()
    shuffle_data(data_list, dialogues, shuffled_data_file, indices_file)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-dialogue', type=str, default='corrected.tsv')
    parser.add_argument('-data', type=str, default='wilkins_corrected.tsv')
    parser.add_argument('-indices', type=str, default=None)
    args = parser.parse_args()
    dialogue_file = args.dialogue
    data_file = args.data
    a = random.randint(0, 100)
    if dialogue_file.replace('.tsv', '') not in data_file:
        data_file = generate_simple_dataset(dialogue_file, data_file)

    if args.indices is None:
        indices_file = dialogue_file.replace('tsv', '') + 'shuffled.'+str(a)+'.indices'
    else:
        indices_file = args.indices
        a = re.search('\d+', indices_file).group()
    shuffled_data_file = dialogue_file.replace('tsv', '') + 'shuffled.'+str(
        a)+'.txt'
    main(data_file, dialogue_file,shuffled_data_file, indices_file)
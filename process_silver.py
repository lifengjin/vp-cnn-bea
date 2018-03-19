import torchtext

def get_silver_dataset(silver_fn, word_fields, char_fields, labels, test_iter_word, rare_labels):
    test_examples = test_iter_word.data()
    i = 0
    with open(silver_fn) as sfn:
        word_examples = []
        char_examples = []
        sfn_lines = sfn.readlines()
        for index, line in enumerate(sfn_lines):
            if line.startswith('paraphrase'):
                split_line = line.split('\t')
                para = split_line[0].split(' ')
                para = ' '.join(para[1:])
                label_string = '_'.join(split_line[1].split(' '))
                if label_string not in rare_labels:
                    continue
                label = labels.index(label_string)
                j = 1
                while True:
                    prev_sent = sfn_lines[index-j]
                    prev_para = prev_sent.split('\t')[0].split(' ')
                    if prev_para[0] != 'paraphrase':
                        break
                    else:
                        j += 1
                prev_para_sent = ' '.join(prev_para)
                this_prev_example = torchtext.data.Example.fromlist([prev_para_sent,'0'], word_fields)
                for test_example in test_examples:
                    if this_prev_example.text == test_example.text:
                        i += 1
                        break
                    # else:
                    #     if index == 68:
                    #         print('test',test_example.text)
                    #         print('para',this_prev_example.text)
                else:
                    this_example = torchtext.data.Example.fromlist([para, label], word_fields)
                    word_examples.append(this_example)
                    this_example = torchtext.data.Example.fromlist([para, label], char_fields)
                    char_examples.append(this_example)
    return word_examples, char_examples
    #     print("filtering out {}".format(i))
    #
    #     dataset = torchtext.data.Dataset(examples, fields)
    #     print("total number of training silver examples: {}".format(len(examples)))
    #
    # iterator = torchtext.data.Iterator(dataset, len(dataset), repeat=False, device=-1)
    # for batch in iterator:
    #     pass
    # else:
    #     print(batch.label.data.numpy())
    #     return batch.text.data.numpy().T, batch.label.data.numpy()
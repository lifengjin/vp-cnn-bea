## Introduction

This is the CNN ensemble system used in the paper [Combining CNNs and Pattern Matching for 
Question Interpretation in a Virtual Patient Dialogue System](http://aclweb.org/anthology/W17-5002) 
published at the Building Educational Applications workshop in 2017.

## Requirement
* python 3.5+
* pytorch > 3.0
* torchtext > 0.2
* numpy

## Parameters

If you want to reproduce the results in the BEA17 paper, run
```bash
python -u main.py -word-vector w2v -word-embed-dim 300 -emb-path ../vp-mem/vector_cache/ 
-eval-on-test -ensemble vot -prediction-file-handle predictions.txt
```

with the word2vec vectors in text format in the cache folder. For details of converting word2vec 
into text format, please see documentation of Torchtext.

The system performs 10-fold cross validation on a hard-coded dataset. To use a custom dataset, 
please make changes to the `vpdataset.py` script.

## Result
You should see something like this when the system finishes training:
```bash
CHAR mean accuracy is 77.20554272517322, std is 1.5004439603492636
WORD mean accuracy is 77.75981524249424, std is 2.088888697230668
LOGIT mean accuracy is 78.47575057736721, std is 1.7763403716424395
```
which gives you accuracies of the character-based CNN ensemble, word-based CNN ensemble and the 
final stacked model.

## Usage
```
./main.py -h
```
or 

```
python3 main.py -h
```

You will get:

```
CNN text classificer

optional arguments:
  -h, --help            show this help message and exit
  -lr LR                initial learning rate [default: 1.0]
  -word-lr WORD_LR      initial learning rate [default: 1.0]
  -char-lr CHAR_LR      initial learning rate [default: 1.0]
  -l2 L2                l2 regularization strength [default: 0.0]
  -word-l2 WORD_L2      l2 regularization strength [default: 0.0]
  -char-l2 CHAR_L2      l2 regularization strength [default: 0.0]
  -epochs EPOCHS        number of epochs for train [default: 25]
  -word-epochs WORD_EPOCHS
                        number of epochs for train [default: 25]
  -char-epochs CHAR_EPOCHS
                        number of epochs for train [default: 25]
  -batch-size BATCH_SIZE
                        batch size for training [default: 50]
  -word-batch-size WORD_BATCH_SIZE
                        batch size for training [default: 50]
  -char-batch-size CHAR_BATCH_SIZE
                        batch size for training [default: 50]
  -log-interval LOG_INTERVAL
                        how many steps to wait before logging training status
                        [default: 1]
  -log-file LOG_FILE    the name of the file to store results
  -verbose              logging verbose info of training process
  -test-interval TEST_INTERVAL
                        how many steps to wait before testing [default: 100]
  -eval-on-test         run evaluation on test data?
  -save-interval SAVE_INTERVAL
                        how many steps to wait before saving [default:500]
  -save-dir SAVE_DIR    where to save the snapshot
  -shuffle              shuffle the data every epoch
  -dropout DROPOUT      the probability for dropout [default: 0.5]
  -char-dropout CHAR_DROPOUT
                        the probability for dropout [default: 0.5]
  -word-dropout WORD_DROPOUT
                        the probability for dropout [default: 0.5]
  -max-norm MAX_NORM    l2 constraint of parameters [default: 3.0]
  -word-max-norm WORD_MAX_NORM
                        l2 constraint of parameters [default: 3.0]
  -char-max-norm CHAR_MAX_NORM
                        l2 constraint of parameters [default: 3.0]
  -char-embed-dim CHAR_EMBED_DIM
                        number of char embedding dimension [default: 128]
  -word-embed-dim WORD_EMBED_DIM
                        number of word embedding dimension [default: 300]
  -kernel-num KERNEL_NUM
                        number of each kind of kernel
  -word-kernel-num WORD_KERNEL_NUM
                        number of each kind of kernel
  -char-kernel-num CHAR_KERNEL_NUM
                        number of each kind of kernel
  -char-kernel-sizes CHAR_KERNEL_SIZES
                        comma-separated kernel size to use for char
                        convolution
  -word-kernel-sizes WORD_KERNEL_SIZES
                        comma-separated kernel size to use for word
                        convolution
  -static               fix the embedding
  -device DEVICE        device to use for iterate data, -1 mean cpu [default:
                        -1]
  -yes-cuda             disable the gpu
  -snapshot SNAPSHOT    filename of model snapshot [default: None]
  -predict PREDICT      predict the sentence given
  -test                 train or test
  -xfolds XFOLDS        number of folds for cross-validation
  -layer-num LAYER_NUM  the number of layers in the final MLP
  -word-vector WORD_VECTOR
                        use of vectors [default: w2v. options: 'glove' or
                        'w2v']
  -emb-path EMB_PATH    the path to the w2v file
  -min-freq MIN_FREQ    minimal frequency to be added to vocab
  -optimizer OPTIMIZER  optimizer for all the models [default: SGD. options:
                        'sgd' or 'adam' or 'adadelta]
  -word-optimizer WORD_OPTIMIZER
                        optimizer for all the models [default: SGD. options:
                        'sgd' or 'adam' or 'adadelta]
  -char-optimizer CHAR_OPTIMIZER
                        optimizer for all the models [default: SGD. options:
                        'sgd' or 'adam' or 'adadelta]
  -fine-tune            whether to fine tune the final ensembled model
  -ortho-init           use orthogonalization to improve weight matrix random
                        initialization
  -ensemble ENSEMBLE    ensemble methods [default: poe. options: poe, avg,
                        vot]
  -num-experts NUM_EXPERTS
                        number of experts if poe is enabled [default: 5]
  -prediction-file-handle PREDICTION_FILE_HANDLE
                        the file to output the test predictions
  -no-always-norm       always max norm the weights
  -silver-set SILVER_SET
                        the silver dataset for training and evaluation
```
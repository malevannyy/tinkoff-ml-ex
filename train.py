import argparse
from os import walk


def train(fn):
    with open(fn) as f:
        contents = f.read()
        # todo: parse text


parser = argparse.ArgumentParser(description='Train script',
                                 usage='train.py --model model.pkl [--input-dir ~/some/date/path]')
parser.add_argument('--model',
                    dest='modelFilename',
                    help='model file name',
                    required=True)
parser.add_argument('--input-dir',
                    dest='inputPath',
                    help='input folder path')

args = parser.parse_args()
# mandatory
modelFilename = args.modelFilename
# optional, can be None => use STDIN instead
inputPath = args.inputPath

if inputPath is None:
    train('STDIN')

else:
    filenames = next(walk(inputPath), (None, None, []))[2]
    for filename in filenames:
        # todo: less ugly
        train(inputPath + '/' + filename)

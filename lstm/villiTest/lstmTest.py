import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils


# load ascii text and covert to lowercase
filename = "/Users/villiarnar/Library/Mobile Documents/com~apple~CloudDocs/UNI 1/Cogito/memeAI/lstm/villiTest/wonderland.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()

# Map unique characters in the file
chars = sorted(list(set(raw_text)))
char_to_int = dict((character, i) for i, character in enumerate(chars))#

# Total characters
n_chars = len(raw_text)
#Total vocab
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)


if __name__ == "__main__":
    for key in char_to_int:
        print(key)


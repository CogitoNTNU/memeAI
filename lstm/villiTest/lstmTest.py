import numpy as np
import tensorflow as tf
import keras

print("hello")

# load ascii text and covert to lowercase
filename = "wonderland.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()

# Map unique characters in the file
chars = sorted(list(set(raw_text)))
char_to_int = dict((character, i) for i, character in enumerate(chars))


print("hello, world")


if __name__ == "__main__":
    for key, value in char_to_int:
        print(key, value)
    print("HELLO")

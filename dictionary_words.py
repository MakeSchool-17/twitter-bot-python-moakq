import sys
# load method from the anagram module
from anagram import load_dictionary
from random import randint


def random_sentence(length, dictionary):
    dict_length = len(dictionary)
    sentence = []
    for i in range(int(length)):
        sentence.append(dictionary[randint(0, dict_length)])
    print(" ".join(sentence) + ".")

if __name__ == '__main__':
    my_dictionary = load_dictionary()
    random_sentence(sys.argv[1], my_dictionary)

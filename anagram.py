import sys


# explain split?
# how to improve load_dictionary?
# how to benchmark in python?
# method to to load dictionary
def load_dictionary():
    with open("/usr/share/dict/words") as dictionary:
        dictionary_list = dictionary.readlines()
        my_dictionary = []
        for word in dictionary_list:
            # explain split?
            word = word.split()[0]
            my_dictionary.append(word)
        return my_dictionary


# method to check anagrams in dictionary
def check_anagram(word, dictionary):
    for element in dictionary:
        if len(word) == len(element):
            if sorted(word.lower()) == sorted(element.lower()):
                print(element)

# entry point
if __name__ == '__main__':
    the_dictionary = load_dictionary()
    check_anagram(sys.argv[1], the_dictionary)

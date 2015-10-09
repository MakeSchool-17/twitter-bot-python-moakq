import text_analyzer
from random import randint


# returns a random word
def select_noweight(histogram_data):
    print(histogram_structure[randint(0, len(histogram_data)-1)][0])


# returns a random word depending on weight
# OPTIMIZE
def select_weight(histogram_data):
    # number of words in the whole text
    number_words = len(source_list)
    print(number_words)
    random_int = randint(0, number_words)
    for item in histogram_data:
        random_int -= item[1]
        print(random_int)
        if random_int <= 0:
            return item[0]


if __name__ == '__main__':
    file_name = text_analyzer.string_or_file()
    source_list = text_analyzer.load_text(file_name)
    histogram_structure = text_analyzer.histogram(source_list)
    # frequency_weighted(histogram_structure)
    with open("write_to.txt", "w") as text:
        for i in range(10000):
            word = select_weight(histogram_structure)
            text.write(word + "\n")

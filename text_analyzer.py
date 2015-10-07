# OPTIMIZE
# use regular expressions to get better results


# loads a text file into a list
def load_text(source_file):
    with open(source_file) as text:
        string = text.read()
        text_list = string.split()
        return text_list


# checks if a word exists in a list of lists
def exists(word, histogram):
    exists = False
    for item in histogram:
        if item[0].lower() == word.lower():
            exists = True
    return exists


# checks the prefered type of input
def string_or_file():
    file_location = input("Enter a file: ")
    return file_location


# returns a list of lists with word frequencies
def histogram(source_text):
    # using lists of lists
    histogram = []
    for word in source_text:
        if exists(word, histogram):
            for item in histogram:
                if item[0].lower() == word.lower():
                    item[1] += 1
        else:
            histogram.append([word, 1])
    print(histogram)
    return histogram


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    for item in histogram:
        if item[0] == word:
            return item[1]

if __name__ == '__main__':
    file_name = string_or_file()
    source_list = load_text(file_name)
    histogram_structure = histogram(source_list)
    unique_data = unique_words(histogram_structure)
    # word frequency function is not used

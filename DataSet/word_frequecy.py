from os import listdir
from os.path import join


def wordFrequencyCalculator(file_path):
    open_file = open(file_path, "r", encoding="utf8")

    word_count_dict = {}

    for word_tokenized_sentences in open_file.readlines():
        words_in_sentences = word_tokenized_sentences.split()

        for word in words_in_sentences:
            if word_count_dict.get(word) is None:
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

    return word_count_dict


if __name__ == "__main__":
    word_count_dict = wordFrequencyCalculator("word_tokenized_output.txt")

    sorted_dict_list = list()

    sorted_dict_list = [(k,v)for k,v in sorted(word_count_dict.items(),key=lambda item : item[1])]

    print(word_count_dict)
    for word_count in sorted_dict_list:
        print(word_count)
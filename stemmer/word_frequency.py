from os import listdir
from os.path import join


def wordFrequencyCalculator(file_path):
    """

    :param file_path: takes complete file path
    :return: reversed sorted dictionary of word and it's frequency in a given file
    """

    open_file = open(file_path, "r", encoding="utf8")

    word_count_dict = {}

    for word_tokenized_sentences in open_file.readlines():
        words_in_sentences = word_tokenized_sentences.split()

        for word in words_in_sentences:
            if word_count_dict.get(word) is None:
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

    sorted_dict_list = [(k, v) for k, v in sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)]
    file = open("word_frequency.txt","w",encoding="utf8")

    for word_count in sorted_dict_list:
        file.write(str(word_count))
        file.write("\n")
    file.close()

    return sorted_dict_list


if __name__ == "__main__":
    word_count_dict = wordFrequencyCalculator("word_tokenized_output.txt")

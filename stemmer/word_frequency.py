from tokenizer import Tokenizer


def wordFrequencyCalculator(file_path):
    """

    :param file_path: takes complete file path any file ( without tokenized too )
    :return: reversed sorted dictionary of word and it's frequency in a given file
    """
    word_count_dict = {}
    tokenize = Tokenizer()
    tokenized_sentences = tokenize.sentenceTokenizer(file=file_path)
    tokenized_words = tokenize.wordTokenizer(tokenized_sentences)

    for word_tokenized_sentence in tokenized_words:
        for word in word_tokenized_sentence:
            if word_count_dict.get(word) is None:
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

    sorted_dict_list = [(k, v) for k, v in sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)]
    file = open("word_frequency.txt", "w", encoding="utf8")

    for word_count in sorted_dict_list:
        file.write(str(word_count))
        file.write("\n")
    file.close()

    return sorted_dict_list


def uniqueWords(file_path, want_return_data=False):
    """

    :param want_return_data: if True want data else want to save file
    :param file_path: takes complete file path ( without or with tokenized sentences file)
    :return: sorted dictionary of word
    """
    tokenizer = Tokenizer()
    tokenized_sentences = tokenizer.sentenceTokenizer(file=file_path)
    tokenized_words = tokenizer.wordTokenizer(tokenized_sentences)
    unique_words = set()

    for word_tokenized_sentence in tokenized_words:
        unique_words.update(word_tokenized_sentence)

    # sorting the words
    unique_words = list(unique_words)
    unique_words.sort()
    if want_return_data:
        return unique_words
    else:
        # save the unique words in file
        file = open('../StemmingOutput/unique_words.txt', 'wt', encoding='utf-8')

        for word in unique_words:
            file.write(word + '\n')
        file.close()


if __name__ == "__main__":
    # word_count_dicts = wordFrequencyCalculator(
    # r'D:\MY\GIT\Gujarati-Stemming\StemmingOutput\word_tokenized_output.txt')
    print((uniqueWords('../StemmingOutput/word_tokenized_output.txt', want_return_data=False)))

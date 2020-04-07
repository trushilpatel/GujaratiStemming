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

    return sorted_dict_list

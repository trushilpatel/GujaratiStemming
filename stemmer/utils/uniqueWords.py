from tokenizer import Tokenizer


def uniqueWords(file_path):
    """

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

    return unique_words

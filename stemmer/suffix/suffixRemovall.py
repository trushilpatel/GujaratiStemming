from stopWords import stop_words
from tokenizer import Tokenizer


def prepareDictionaryOfWords(dictionary_file):
    file = open(dictionary_file, 'rt', encoding='utf-8')
    tokenizer = Tokenizer()

    # getting all the sentences in sentences
    sentences = ''
    for i in file.readlines():
        sentences += i

    # here we are passing the string because we want the tokenized sentences output for further processing
    tokenized_sentences = tokenizer.sentenceTokenizer(paragraph=sentences)
    tokenized_words = tokenizer.wordTokenizer(sentences=tokenized_sentences)

    print(tokenized_words)


def createDictionary(tokenized_words):
    letters_dict = dict()
    for sentence_words in tokenized_words:
        for word in sentence_words:
            for letter in word:
                letter_exist = letters_dict.get(letter)

                # if letter exist the we have the letter's value else None is returned
                if letter is None:
                    letter[]



if __name__ == '__main__':
    prepareDictionaryOfWords('../../corpus/helpingFiles/dictionary.txt')

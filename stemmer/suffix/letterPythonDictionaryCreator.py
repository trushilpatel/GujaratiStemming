from tokenizer import Tokenizer
from utils import readWriteJsonFile


def prepareDictionaryOfWords(gujarati_dictionary_file):
    file = open(gujarati_dictionary_file, 'rt', encoding='utf-8')
    tokenizer = Tokenizer()

    # getting all the sentences in sentences
    sentences = ''
    for i in file.readlines():
        sentences += i

    # here we are passing the string because we want the tokenized sentences output for further processing
    tokenized_sentences = tokenizer.sentenceTokenizer(paragraph=sentences)
    tokenized_words = tokenizer.wordTokenizer(sentences=tokenized_sentences)

    createDictionary(tokenized_words)


def createDictionary(tokenized_words):
    letters_dict = dict()
    for sentence_words in tokenized_words:
        for word in sentence_words:
            first_letter_of_word_exist = letters_dict.get(word[0])
            temp_dict = {}

            if first_letter_of_word_exist is None:
                letters_dict[word[0]] = {}

            temp_dict = letters_dict.get(word[0])

            for letter in word[1:]:
                letter_exist = temp_dict.get(letter)

                # if letter exist the we have the letter's value else None is returned
                if letter_exist is None:
                    temp_dict[letter] = {}

                temp_dict = temp_dict[letter]

            temp_dict['end'] = True

    readWriteJsonFile.writeJsonFile(letters_dict, file_name='letters_python_dictionary.json')


if __name__ == '__main__':
    prepareDictionaryOfWords('../../corpus/helpingFiles/dictionary.txt')

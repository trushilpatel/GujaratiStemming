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
    createDictionary(tokenized_words)


def createDictionary(tokenized_words):
    letters_dict = dict()
    for sentence_words in tokenized_words:
        for word in sentence_words:
            print(letters_dict)
            first_letter_of_word_exist = letters_dict.get(word[0])
            temp_dict = {}

            if first_letter_of_word_exist is None:
                letters_dict[word[0]] = {}

            temp_dict = letters_dict.get(word[0])

            for letter in word[1:]:
                print(letter)
                letter_exist = temp_dict.get(letter)

                # if letter exist the we have the letter's value else None is returned
                if letter_exist is None:
                    temp_dict[letter] = {}
                    print(temp_dict)
                    print(letters_dict)

                temp_dict = temp_dict[letter]
    jsonFile = open("letter_dictionary.json",'wt', encoding='utf-8')
    print(letters_dict)
    jsonFile.writelines(str(letters_dict))
    jsonFile.close()



if __name__ == '__main__':
    prepareDictionaryOfWords('../../corpus/helpingFiles/small_dictionary.txt')

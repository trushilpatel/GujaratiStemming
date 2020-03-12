from utils import readWriteJsonFile


class WordExistInLettersDictionary:
    def __init__(self):
        self.suffix_list = list(
            map(lambda w: w.strip(), open(r'D:\MY\GIT\Gujarati-Stemming\corpus\helpingFiles\suffix.txt',
                                          'rt', encoding='utf-8').readlines()))
        self.letter_dict = readWriteJsonFile.readJsonFile(
            r'D:\MY\GIT\Gujarati-Stemming\corpus\helpingFiles\letters_python_dictionary.json')

    def checkValidSuffix(self, suffix):
        if suffix in self.suffix_list:
            return True
        return False

    def checkWordExistence(self, word):
        try:
            temp_dict = self.letter_dict[word[0]]

            for letter_index in range(1, len(word[:])):
                letter_exist = temp_dict.get(word[letter_index])
                if letter_exist is not None:
                    temp_dict = temp_dict[word[letter_index]]
                else:
                    if self.checkValidSuffix(word[letter_index:]):
                        # got dictionary word and a valid suffix
                        # ex : ભૂજએ is a not proper dictionary word but ભુજ is which in
                        #       the starting of the ભુજએ and suffix is એ which is valid
                        #       suffix
                        return {
                            'is_dictionary_word': True,
                            'dictionary_word': word[0:letter_index],
                            'valid_suffix': True,
                            'suffix': word[letter_index:]
                        }
                    # got dictionary word in start of word bur not a valid suffix
                    # ex : ભૂજજજ is a not proper dictionary word but it contains dictinary word
                    #       in starting of word which is ભુજ but we got જજ as suffix which is
                    #       not a valid suffix
                    return {
                        'is_dictionary_word': True,
                        'dictionary_word': word[0:letter_index],
                        'valid_suffix': False,
                        'suffix': word[letter_index:]
                    }

            word_end = temp_dict.get('end')

            # the word is dictionary word
            # ex : ભુજ is proper dictionary word
            if word_end is not None:
                return {
                    'is_dictionary_word': True,
                    'dictionary_word': word
                }

            # word is not a dictionary word and doesn't contains valid suffix
            # ex : ભૂ is a not proper dictionary word but ભુજ is
            return {
                'is_dictionary_word': False,
                'dictionary_word': word
            }

        except:
            {}


if __name__ == '__main__':
    word_existence_checking = WordExistInLettersDictionary()
    print("Valid : ", word_existence_checking.checkWordExistence('ભુજે'))

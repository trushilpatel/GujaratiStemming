from utils import readWriteJsonFile


class WordExistInLettersDictionary:
    def __init__(self):
        self.suffix_list = list(
            map(lambda w: w.strip(), open(r'../../corpus/helpingFiles/suffix.txt',
                                          'rt', encoding='utf-8').readlines()))

        # suffix_list and final_ suffix list are same
        # but final_suffix list is sorted in length max to min
        # in future we have to merge this to list in to single list
        self.final_suffix_list = list(
            map(lambda w: w.strip(), open(r'../../corpus/helpingFiles/final_suffix.txt',
                                          'rt', encoding='utf-8').readlines()))
        self.letter_dict = readWriteJsonFile.readJsonFile(
            r'../../corpus/helpingFiles/letters_python_dictionary.json')

    def checkValidSuffix(self, suffix):
        if suffix in self.suffix_list:
            return True
        return False

    def checkWordExistence(self, word):
        # removing spaces
        word = word.strip()

        try:
            temp_dict = self.letter_dict[word[0]]
            # for checking word end if yes then assign a dictionary
            temp_word_end = None

            for letter_index in range(1, len(word[:])):
                letter_exist = temp_dict.get(word[letter_index])

                if letter_exist is None:
                    break
                else:
                    temp_dict = temp_dict[word[letter_index]]

                if self.checkValidSuffix(word[letter_index:]):
                    # got dictionary word and a valid suffix
                    # ex : ભૂજએ is a not proper dictionary word but ભુજ is which in
                    #       the starting of the ભુજએ and suffix is એ which is valid
                    #       suffix
                    return {
                        'is_dictionary_word': True,
                        'word': word[0:letter_index],
                        'valid_suffix': True,
                        'suffix': word[letter_index:]
                    }

                # got dictionary word in start of word bur not a valid suffix
                # ex : ભૂજજજ is a not proper dictionary word but it contains dictinary word
                #       in starting of word which is ભુજ but we got જજ as suffix which is
                #       not a valid suffix
                word_end = temp_dict.get('end')
                if word_end is not None:
                    temp_word_end = {
                        'is_dictionary_word': True,
                        'word': word[0:letter_index],
                        'valid_suffix': False,
                        'suffix': word[letter_index:]
                    }

            # the word is dictionary word
            # ex : ભુજ is proper dictionary word
            if word_end is not None:
                return {
                    'is_dictionary_word': True,
                    'word': word
                }

            # word is not a dictionary word and doesn't contains valid suffix
            # ex : ભૂ is a not proper dictionary word but ભુજ is
            return {
                'is_dictionary_word': False,
                'word': word
            }

        except:
            return self.remove_suffix(word)

    def remove_suffix(self, word):
        """
            what if the word is not a dictionary word then we have to remove it from
            the word by checking whether the suffix exist in word or not

        :param word: word who's suffix is being checked
        :return: structured response about word existence and suffix details
        """

        for suffix in self.final_suffix_list:

            if word.endswith(suffix):
                suffix_index = word.index(suffix)
                return {
                    'is_dictionary_word': False,
                    'word': word[0:suffix_index],
                    'valid_suffix': True,
                    'suffix': word[suffix_index:]
                }
        else:
            return {
                'is_dictionary_word': False,
                'word': word,
                'valid_suffix': False,
                'suffix': None
            }


if __name__ == '__main__':
    word_existence_checking = WordExistInLettersDictionary()
    print("Valid : ", word_existence_checking.checkWordExistence('ldrpમાં'))

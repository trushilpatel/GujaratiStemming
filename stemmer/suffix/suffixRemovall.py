"""
    આવનારા ભવિષ્યમાં આ ફાઈલને વધુ સરળ બનાવવા પ્રયત્નો કરવા
    LOL
    also reduce the Time Complexity
"""

import readWriteJsonFile


class SuffixRemoval:
    def __init__(self):
        self.suffix_list = list(
            map(lambda w: w.strip(), open(r'E:\GIT\GujaratiStemming\corpus\helpingFiles\suffix.txt',
                                          'rt', encoding='utf-8').readlines()))

        # suffix_list and final_ suffix list are same
        # but final_suffix list is sorted in length max to min
        # in future we have to merge this to list in to single list
        self.final_suffix_list = list(
            map(lambda w: w.strip(), open(r'E:\GIT\GujaratiStemming\corpus\helpingFiles\final_suffix.txt',
                                          'rt', encoding='utf-8').readlines()))
        self.letter_dict = readWriteJsonFile.readJsonFile(
            r'E:\GIT\GujaratiStemming\stemmer\suffix\NEW_letters_python_dictionary.json')

    def checkValidSuffix(self, suffix):
        if suffix in self.suffix_list:
            return True
        return False

    def suffixRemoval(self, word):
        # removing spaces
        word = word.strip()

        try:
            temp_dict = self.letter_dict[word[0]]
            # for checking word end if yes then assign a dictionary
            temp_word_end = None
            breaked = False

            for letter_index in range(1, len(word[:])):
                letter_exist = temp_dict.get(word[letter_index])

                if letter_exist is None:
                    breaked = True
                    break
                else:
                    temp_dict = temp_dict.get(word[letter_index])

                if self.checkValidSuffix(word[letter_index + 1:]):
                    # got dictionary word and a valid suffix
                    # ex : ભૂજએ is a not proper dictionary word but ભુજ is which in
                    #       the starting of the ભુજએ and suffix is એ which is valid
                    #       suffix
                    return {
                        'is_dictionary_word': True,
                        'word': word[0:letter_index + 1],
                        'valid_suffix': True,
                        'suffix': word[letter_index + 1:]
                    }

                # got dictionary word in start of word bur not a valid suffix
                # ex : ભૂજજજ is a not proper dictionary word but it contains dictionary word
                #       in starting of word which is ભુજ but we got જજ as suffix which is
                #       not a valid suffix
                word_end = temp_dict.get('end')
                if word_end is not None:
                    temp_word_end = {
                        'is_dictionary_word': True,
                        'word': word[0:letter_index + 1],
                        'valid_suffix': False,
                        'suffix': word[letter_index + 1:]
                    }

            # if breaked by for loop
            if breaked and temp_word_end is not None:
                return temp_word_end
            elif breaked and temp_word_end is None:
                return self.remove_suffix(word)

            word_end = temp_dict.get('end')
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

        for word_index in range(len(word)):
            if word[word_index:] in self.final_suffix_list:
                return {
                    'is_dictionary_word': False,
                    'word': word[0:word_index],
                    'valid_suffix': True,
                    'suffix': word[word_index:]
                }
        else:
            return {
                'is_dictionary_word': False,
                'word': word,
                'valid_suffix': False,
                'suffix': None
            }


def checkSuffixRemovalAccuracy(filePath):
    """

    :param filePath: get's comma separated file
    :return: accuracy in percentage
    """
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~‘ \n'''

    file = open(filePath, 'rt', encoding='utf-8')
    lines = file.readlines()
    sr = SuffixRemoval()
    totalWords = len(lines)
    accurateWords = 0

    for lineIndex in range(len(lines)):
        lines[lineIndex] = lines[lineIndex].split(',')
        for wordIndex in range(len(lines[lineIndex])):
            lines[lineIndex][wordIndex] = lines[lineIndex][wordIndex].strip(punctuations)

        wordSR = sr.suffixRemoval(lines[lineIndex][0])['word']
        print(lines[lineIndex], wordSR)

        if wordSR == lines[lineIndex][1]:
            accurateWords += 1

    print("Accuracy : ", (accurateWords / totalWords) * 100)


if __name__ == '__main__':
    word_existence_checking = SuffixRemoval()
    # print("Valid : ", word_existence_checking.suffixRemoval('રાજેશ્વરી').get('word'))
   # checkSuffixRemovalAccuracy(filePath=r'E:\GIT\GujaratiStemming\stemmer\suffix\testStemmingAccuracy.txt')
    print(word_existence_checking.suffixRemoval('અમેરિકા'))
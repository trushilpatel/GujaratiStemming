import readWriteJsonFile


class Suffix:
    def __init__(self):
        self.suffixLettersDict = readWriteJsonFile.readJsonFile(
            file_name=r"E:\GIT\GujaratiStemming\stemmer\suffix\suffix_letters_python_dictionary.json"
        )

    def isValidSuffix(self, word):
        word = word.strip()
        wordLen = len(word)

        if wordLen == 0:
            return False

        try:
            temp_dict = self.suffixLettersDict.get(word[0])

            if temp_dict is None:
                return False

            lastEndWordIndex = 0

            for letter_index in range(1, wordLen):

                get_letter_dict = temp_dict.get(word[letter_index])

                if get_letter_dict is None:
                    return False
                temp_dict = get_letter_dict

                if temp_dict.get('end'):
                    lastEndWordIndex = letter_index

            else:
                if lastEndWordIndex + 1 == wordLen:
                    return True

            return False
        except:
            print("ERROR: IN SUFFIX")
            return False


if __name__ == '__main__':
    suffix = Suffix()
    print(suffix.isValidSuffix(word="હાઈ"))

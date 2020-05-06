from utils import readWriteJsonFile


class Suffix:
    def __init__(self):
        self.suffixLettersDict = readWriteJsonFile.readJsonFile(
            file_name=r"suffix/suffix_letters_python_dictionary.json"
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

            if wordLen == 1 and temp_dict.get('end') is not None:
                return True

            for letter_index in range(1, wordLen):

                get_letter_dict = temp_dict.get(word[letter_index])

                if get_letter_dict is None:
                    return False
                temp_dict = get_letter_dict
                if temp_dict.get('end') is not None:
                    lastEndWordIndex = letter_index

            else:
                if lastEndWordIndex != 0 and lastEndWordIndex + 1 == wordLen :
                    return True

            return False
        except:
            print("ERROR: IN SUFFIX")
            return False

    def findSuffixAndRemove(self, word):
        for wordIndex in range(len(word)):
            if self.isValidSuffix(word[wordIndex:]):
                if wordIndex != 0:
                    return word[0:wordIndex]
        return word


if __name__ == '__main__':
    suffix = Suffix()
    print(suffix.isValidSuffix(word=""))



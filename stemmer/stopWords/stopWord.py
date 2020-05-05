import readWriteJsonFile
from suffix import Suffix


class StopWords:
    def __init__(self):
        self.stopWordsLetterDict = readWriteJsonFile.readJsonFile(
            file_name=r"E:\GIT\GujaratiStemming\stemmer\suffix\stopWords_letters_python_dictionary.json"
        )
        self.suffix = Suffix()

    def isStopWord(self, word):
        word = word.strip()
        wordLen = len(word)

        if wordLen == 0:
            return False

        try:
            temp_dict = self.stopWordsLetterDict.get(word[0])

            if temp_dict is None:
                return False

            lastEndWordIndex = 0
            for letter_index in range(1, wordLen):

                get_letter_dict = temp_dict.get(word[letter_index])

                if get_letter_dict is None:
                    if self.suffix.isValidSuffix(word[lastEndWordIndex + 1:]):
                        return True
                    return False

                temp_dict = get_letter_dict

                if temp_dict.get('end'):
                    lastEndWordIndex = letter_index

            else:
                if lastEndWordIndex + 1 == wordLen:
                    return True
                elif self.suffix.isValidSuffix(word[lastEndWordIndex + 1:]):
                    return True

            return False
        except:
            print("ERROR: IN STOPWORDS")
            return False

    def removeStopWords(self):
        pass


if __name__ == '__main__':
    sw = StopWords()
    print(sw.isStopWord(word=""))

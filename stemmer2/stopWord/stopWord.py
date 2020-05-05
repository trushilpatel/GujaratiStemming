from utils import readWriteJsonFile
from suffix.suffix import Suffix


class StopWords:
    def __init__(self):
        self.stopWordsLetterDict = readWriteJsonFile.readJsonFile(
            file_name=r"stopWord\stopWords_letters_python_dictionary.json"
        )
        self.suffix = Suffix()

    def isValidStopWord(self, word):
        """

        :param word: gets word as input
        :return: True/False based on is valid stop word or not
        """
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

    def removeStopWordsFromList(self, words: list):
        """

        :param words: list of tokenized word
                      EX: [w1,w2]
        :return: None
                cause it directly made changes to the list

                SO BE CAREFUL WHILE USING THIS FUNCTION
        """
        for wordIndex in range(len(words) - 1, -1, -1):
            if self.isValidStopWord(words[wordIndex]):
                words.pop(wordIndex)

    def removeStopWordsFromTokenizedWords(self, tokenizedWords: list):
        """

        :param tokenizedWords: list of tokenized sentences into words
                               EX: [[w1,w2,..],[w3,w4,..],..]
        :return: None
               cause it directly made changes to the list

                SO BE CAREFUL WHILE USING THIS FUNCTION
        """
        for tw in tokenizedWords:
            self.removeStopWordsFromList(tw)


if __name__ == '__main__':
    sw = StopWords()
    words = [["આથી", "ગુજરાત", "માં", "કેમ", "છો", "મજા", "માં"]]
    print(sw.removeStopWordsFromTokenizedWords(tokenizedWords=words))
    print(words)

from suffix.suffix import Suffix
from stopWord.stopWord import StopWords
from tokenizer.tokenizer import Tokenizer

from utils.dataCleaner.dataCleaner import DataCleaner
from utils.gujaratiWordChecker import getOnlyGujaratiWord
from utils.letterPythonDictionaryCreator import runLetterPythonDictionary
from utils import readWriteJsonFile


class GujaratiStemmer:
    def __init__(self):
        self.guDict = readWriteJsonFile.readJsonFile(
            r"helpingFiles\new_gu_dict_letters_python_dictionary.json")
        self.suffix = Suffix()

    def wordStemmingException(self, word, lastLetterIndex):
        temp = self.suffix.findSuffixAndRemove(word)
        if temp == word:
            temp = word[0:lastLetterIndex + 1]
        return temp

    def guWordStemmer(self, word):
        word = word.strip()
        wordLen = len(word)

        if wordLen == 0:
            return False

        try:
            temp_dict = self.guDict.get(word[0])

            if temp_dict is None:
                return False

            lastLetterIndex = 0
            for letter_index in range(1, wordLen):
                get_letter_dict = temp_dict.get(word[letter_index])

                if get_letter_dict is None:
                    if self.suffix.isValidSuffix(word[lastLetterIndex + 1:]):
                        return word[0:lastLetterIndex + 1]
                    return self.wordStemmingException(word, lastLetterIndex)

                temp_dict = get_letter_dict

                if temp_dict.get('end'):
                    lastLetterIndex = letter_index

            else:
                if lastLetterIndex + 1 == wordLen:
                    return word
                elif self.suffix.isValidSuffix(word[lastLetterIndex + 1:]):
                    return word[0:lastLetterIndex + 1]

            return self.wordStemmingException(word, lastLetterIndex)
        except:
            print("ERROR: IN GUJARATI STEMMER2")
            return self.wordStemmingException(word, lastLetterIndex)

    def guWordsListStemmer(self, listOfWords):
        """

        :param listOfWords: list of wordsd
                            EX:- [w,a,...]
        :return: it directly updates the list
                 so returns None
        """
        for wordIndex in range(len(listOfWords)):
            listOfWords[wordIndex] = self.guWordStemmer(listOfWords[wordIndex])

    def guTokenizedWordStemmer(self, tokenizedWords):
        """

        :param tokenizedWords: list
                               EX:- [[..],[..],..]
        :return: it directly updates the list
                 so returns None
        """
        for wordsListIndex in range(len(tokenizedWords)):
            self.guWordsListStemmer(tokenizedWords[wordsListIndex])

    def guStemmer(self, filePath=None, text=None, cleanData=False, saveFileDir=None, saveFileName=None):
        """

        :param filePath: [OPTIONAL] file's location
        :param cleanData: [OPTIONAL] data needed to be cleaned or not
        :param text: [OPTIONAL] text dataset
        :return: stemmed text

        FOR MEMORY SAVING FOLLOWING COULD BE HELPFUL [ YET TO ADD, IT's A NOTION]
        --------------------------------------------
        :param saveFileDir: save file directory
        :param saveFileName: name of file
        """
        if filePath is None and text is None:
            raise Exception("ERROR in guStemmer\n\t Invalid Argument")

        # gathering data
        if filePath is not None:
            file = open(filePath, 'rt', encoding='utf-8')
            text = file.read()
            file.close()

        # cleaning data
        if cleanData is True:
            dc = DataCleaner()
            text = dc.cleanData(data=text)

        # tokenizing the data
        tokenizer = Tokenizer()
        senTok = tokenizer.sentenceTokenizer(text=text)
        worTok = tokenizer.wordTokenizer(sentences=senTok)
        del senTok

        # removing stopwords
        sw = StopWords()
        sw.removeStopWordsFromTokenizedWords(tokenizedWords=worTok)

        # stemming whole tokenized words list
        self.guTokenizedWordStemmer(tokenizedWords=worTok)

        return worTok


if __name__ == "__main__":
    gs = GujaratiStemmer()
    t = """નામ ઑં ઑંકાર એકાક્ષર ગૂઢ રહસ્યમય અક્ષર સનાતન અક્ષર બ્રહ્મ બ્રહ્મનું ઉત્પત્તિ સ્થિતિ અને લય બ્રહ્માંડના અવિર્ભાવનો ધ્વનિ.
    આદિ ધ્વનિ પવિત્ર મંત્ર બીજમંત્ર.
    સોહમ્ ઑં તત્ સત્ નાદબ્રહ્મ નાદધ્વનિ પરબ્રહ્મના 7 આવિર્ભાવનો ધ્વનિ વેદોનું મૂળ વૈદિક મંત્રોચ્ચારના આરંભનો ઉદ્ગાર.
    પરબ્રહ્મ અપર બ્રહ્મ ત્રયીવિદ્યાનું પ્રતિનિધિત્વ બ્રહ્મા વિષ્ણુ મહેશ તત્ ત્વમ્ અસિ.
    પ્રત્યેક મંત્રનો પ્રારંભ એકાક્ષર ઉદ્ગીથ અનંત શાશ્વતતા અમરતા શિવોહમ્ ઑં મંત્ર પ્રણવમંત્ર પ્રણવો પરિષદ પ્રણવોપાસનાનિ.
    અહં બ્રહ્માસ્મિ અનલ હક્ક ઓમકાર જાગ્રત્ આત્માઓ સ્વપ્નશીલ આત્માઓ સુષુપ્ત અને અસ્વપ્નશીલ આત્માઓ.
    ઑંકાર લીંગ ઑંકારનાથ.
    """

    print(gs.guStemmer(text=t, cleanData=True))


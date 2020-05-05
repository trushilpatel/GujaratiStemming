from stemmer.possGujChars.possGujChars import getPossGujChars


class DataCleaner:
    def __init__(self):
        self.possGujChars = {char: True for char in getPossGujChars() if char}
        self.punctuations = '''!()-[]\\{};:'",<>./?@#$%^&*_~‘ \n'''
        # here in punctuation set ':' as per the dataset

    def isGujaratiWord(self, word):
        for char in word:
            if self.possGujChars.get(char) is None:
                break
        else:
            return word
        return ''

    def cleanData(self, filePath=None, data=None):
        """
        get either a filePath or data to process
        if both were given then FILE is preferred

        :param filePath: path of file to be cleaned
        :param data: data to clean
        :return: if filePaht : returns Nothing
                 if data : return cleaned data
        """

        if filePath is None and data is None:
            return
        elif filePath is not None:
            file = open(filePath, 'rt', encoding='utf-8')
            text = file.read()
            file.close()
        else:
            text = data
        print("Total text length :", len(text))

        # make change here
        text = text.replace('\n', ' ')
        text = text.replace('(', ' ( ')
        text = text.replace(')', ' ) ')
        text = text.replace('[', ' [ ')
        text = text.replace(']', ' ] ')
        text = text.replace('{', ' { ')
        text = text.replace('}', ' } ')

        # MAKE CHANGE HERE
        sentences = text.split()
        del text
        print("Total sentences :", len(sentences))

        for sentenceIndex in range(len(sentences)):
            if sentenceIndex % 1000 == 0:
                print(sentenceIndex)
            newSentence = ''
            for word in sentences[sentenceIndex].split():
                gujWord = self.isGujaratiWord(word.strip(self.punctuations))
                if gujWord != '':
                    newSentence += gujWord + ' '
            sentences[sentenceIndex] = newSentence.strip()

        text = ''
        for sentence in sentences:
            if sentence.strip() != '':
                # MAKE CHANGE HERE
                text += sentence + '\n'

        if filePath is not None:
            file = open(filePath, 'wt', encoding='utf-8')
            file.write(text)
            file.close()
        else:
            return text


if __name__ == '__main__':
    dc = DataCleaner()
    dc.cleanData(filePath=r"E:\GIT\python-utils\sqlite\GujaratiDictionary\dictionary\9.txt")

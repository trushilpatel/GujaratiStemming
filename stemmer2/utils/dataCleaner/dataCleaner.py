from utils.possGujChars.possGujChars import getPossGujChars


class DataCleaner:
    def __init__(self):
        self.possGujChars = getPossGujChars()
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

        :param filePath: [OPTIONAL] path of file to be cleaned
        :param data: [OPTIONAL] data to clean
        :return: if filePath : returns Nothing and writes a data to file directly
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
        # text = text.replace('\n', ' ')
        text = text.replace('(', ' ( ')
        text = text.replace(')', ' ) ')
        text = text.replace('[', ' [ ')
        text = text.replace(']', ' ] ')
        text = text.replace('{', ' { ')
        text = text.replace('}', ' } ')

        # MAKE CHANGE HERE
        sentences = text.split('\n')
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
            if len(newSentence.split()) > 1:
                sentences[sentenceIndex] = newSentence.strip()

        sentences = list(set(sentences))

        if filePath is not None:
            file = open(filePath, 'wt', encoding='utf-8')
            for sentence in sentences:
                # MAKE CHANGES HERE
                file.write(sentence + '.\n')
            file.close()
        else:
            text = ''
            for sentence in sentences:
                if sentence.strip() != '':
                    # MAKE CHANGE HERE
                    text += sentence + '\n'
            return text


if __name__ == '__main__':
    dc = DataCleaner()
    dc.cleanData(filePath=r"E:\GIT\DataSet\cleanedDataSet\combined_cleanedDataSet.txt")

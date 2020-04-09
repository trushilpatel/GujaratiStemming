from stemmer.possGujChars.possGujChars import getPossGujChars


class CleanFileData:
    def __init__(self):
        self.possGujChars = getPossGujChars()
        self.punctuations = '''!()-[]\\{};:'",<>./?@#$%^&*_~‘ \n'''

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
            text = ''
            for lines in file.readlines():
                text += lines
            file.close()
        else:
            text = data

        sentences = text.split('\n')

        for sentence in range(len(sentences)):
            newSentence = ''
            for word in sentences[sentence].split():
                gujWord = getOnlyGujaratiWord(word.strip(punctuations))
                if gujWord != '':
                    newSentence += gujWord + ' '
            sentences[sentence] = newSentence.strip()

        text = ''
        for sentence in sentences:
            if sentence.strip() != '':
                text += sentence + '.\n'

        if filePath is not None:
            file = open(filePath, 'wt', encoding='utf-8')
            file.write(text)
            file.close()
        else:
            return text

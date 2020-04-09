from utils.gujaratiWordChecker import getOnlyGujaratiWord


def cleanData(filePath=None, data=None):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~‘'''

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

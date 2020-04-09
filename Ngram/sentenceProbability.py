def getTupleProb(tpl, xgramsProb, x):
    if tpl not in xgramsProb[x]:
        if x == 1:
            xgramsProb[x][tpl] = (1) / (1 + len(xgramsProb[x]))
        else:
            return getTupleProb(tpl[0:x - 1], xgramsProb, x - 1) * getTupleProb(tpl[0:x - 1], xgramsProb, x - 1)

    return xgramsProb[x][tpl]


def calculate_xgram_sentence_probability(sentence, xgramsProb, x):
    """

    :param sentence: string
    :param xgramsProb: Takes all the probability dict created by calcProb.py
    :param x: gram ex: for trigram 3
    :return: sentence probability
    """
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~‘'''
    outputProb = 1
    tplList = []
    words_tokenized = sentence.split()

    for wordIndex in range(len(words_tokenized)):
        words_tokenized[wordIndex] = words_tokenized[wordIndex].strip(punctuations)

    print("INPUT :", ' '.join([word for word in words_tokenized if word]))

    for wordIndex in range(len(words_tokenized) - x + 1):
        temp = []
        for tplWordIndex in range(wordIndex, wordIndex + x):
            temp.append(words_tokenized[tplWordIndex])
        tplList.append(tuple(temp.copy()))

    for i in tplList:
        print(i)

    for i in tplList:
        outputProb *= getTupleProb(tpl=i, xgramsProb=xgramsProb, x=x)

    return outputProb

def calcAllGramsProb(xGrams):
    if len(xGrams.keys()) <= 1:
        return
    else:
        allXgramsProb = {}

        allXgrams = list(xGrams.keys())
        allXgrams.reverse()

        for key in xGrams:
            if key > 1:
                listOfXgram = 'listOf' + str(key) + 'gram'
                xgramCounts = str(key) + 'gramCounts'
                xMinusOneGramCounts = str(key - 1) + 'gramCounts'

                allXgramsProb[key] = calcXgramProb(xGrams[key][listOfXgram], xgramCounts=xGrams[key][xgramCounts],
                                                   xMinusOneGramCounts=xGrams[key - 1][xMinusOneGramCounts], x=key)

        return allXgramsProb


def calcXgramProb(listOfXgram, xgramCounts, xMinusOneGramCounts, x):
    listOfProb = {}

    for xgram in listOfXgram:
        listOfProb[xgram] = (xgramCounts.get(xgram)) / (xMinusOneGramCounts.get(xgram[0:x - 1]))

    return listOfProb


"""
    file = open('bigramProb.txt', 'w')
    file.write('Bigram' + '\t\t\t' + 'Count' + '\t' + 'Probability' + '\n')

    for bigrams in listOfBigrams:
        file.write(str(bigrams) + ' : ' + str(bigramCounts[bigrams]) + ' : ' + str(listOfProb[bigrams]) + '\n')
    file.close()
"""

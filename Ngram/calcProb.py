def calcQuadrigramProb(listOfQuadrigram, quadrigramCounts, trigramCounts):
    listOfProb = {}

    for quadrigram in listOfQuadrigram:
        word1 = quadrigram[0]
        word2 = quadrigram[1]
        word3 = quadrigram[2]

        listOfProb[quadrigram] = (quadrigramCounts.get(quadrigram)) / (trigramCounts.get((word1, word2, word3)))

    return listOfProb


"""
    file = open("trigramProb.txt", 'w')
    file.write('Quadrigram' + '\t\t\t' + 'Count' + '\t' + 'Probability' + '\n')

    for quadrigram in listOfQuadrigram:
        file.write(str(quadrigram) + ':' + str(quadrigramCounts[quadrigram]) + ':' + str(listOfProb[quadrigram]) + '\n')
    file.close()
"""


def calcXgramProb(listOfXgram, xgramCounts, xMinusOneGramCounts, x):
    listOfProg = {}

    for xgram in listOfXgram:
        listOfXgram[xgram] = (xgramCounts.get(xgram)) / (xMinusOneGramCounts.get(xgram[0:x - 1]))

    return listOfProg


def calcTrigramProb(listOfTrigrams, bigramCounts, trigramCounts):
    listOfProb = {}

    for trigram in listOfTrigrams:
        word1 = trigram[0]
        word2 = trigram[1]
        word3 = trigram[2]

        listOfProb[trigram] = (trigramCounts.get(trigram)) / (bigramCounts.get((word1, word2)))

    return listOfProb


"""
    file = open("trigramProb.txt", 'w')
    file.write('Trigram' + '\t\t\t' + 'Count' + '\t' + 'Probability' + '\n')

    for trigram in listOfTrigrams:
        file.write(str(trigram) + ':' + str(trigramCounts[trigram]) + ':' + str(listOfProb[trigram]) + '\n')
    file.close()
"""


def calcBigramProb(listOfBigrams, unigramCounts, bigramCounts):
    listOfProb = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        word2 = bigram[1]

        listOfProb[bigram] = (bigramCounts.get(bigram)) / (unigramCounts.get(word1))
    return listOfProb


"""
    file = open('bigramProb.txt', 'w')
    file.write('Bigram' + '\t\t\t' + 'Count' + '\t' + 'Probability' + '\n')

    for bigrams in listOfBigrams:
        file.write(str(bigrams) + ' : ' + str(bigramCounts[bigrams]) + ' : ' + str(listOfProb[bigrams]) + '\n')
    file.close()
"""

def quadrigramWithAddOneSmoothing(listOfQuadrigrams, quadrigramCounts, trigramCounts):
    listOfProb = {}
    cStar = {}
    trigramCountsLength = len(trigramCounts)
    for quadrigram in listOfQuadrigrams:
        word1 = quadrigram[0]
        word2 = quadrigram[1]
        word3 = quadrigram[2]

        listOfProb[quadrigram] = (quadrigramCounts.get(quadrigram) + 1) / (trigramCounts.get((word1, word2, word3)) +
                                                                           trigramCountsLength)
        cStar[quadrigram] = (quadrigramCounts.get(quadrigram) + 1) * trigramCounts[(word1, word2)] / (
                trigramCounts.get((word1, word2)) + trigramCountsLength)

    return listOfProb, cStar


def xgramWithAddOneSmoothing(listOfXgrams, xgramCounts, xMinusOneGramCounts, x):
    listOfProb = {}
    cStar = {}
    xMinusOneGramCountsLength = len(xMinusOneGramCounts)

    for xgram in listOfXgrams:
        listOfProb[xgram] = (xgramCounts.get(xgram) + 1) / (xMinusOneGramCounts.get(x[0:x-1]) +
                                                            xMinusOneGramCountsLength
                                                            )
        cStar[xgram] = (xgramCounts.get(xgram) + 1) * xMinusOneGramCounts.get(xgram[0:x-1]) / (
            xMinusOneGramCounts.get(xgram[0:-x]) + xMinusOneGramCountsLength
        )

    return listOfProb, cStar


def trigramWithAddOneSmoothing(listOfTrigrams, trigramCounts, bigramCounts):
    listOfProb = {}
    cStar = {}
    bigramCountsLength = len(bigramCounts)
    for trigram in listOfTrigrams:
        word1 = trigram[0]
        word2 = trigram[1]

        listOfProb[trigram] = (trigramCounts.get(trigram) + 1) / (bigramCounts.get((word1, word2)) + bigramCountsLength)
        cStar[trigram] = (trigramCounts.get(trigram) + 1) * bigramCounts.get((word1, word2)) / (
                bigramCounts.get((word1, word2)) + bigramCountsLength
        )

    return listOfProb, cStar


def bigramWithAddOneSmoothing(listOfBigrams, unigramCounts, bigramCounts):
    listOfProb = {}
    cStar = {}

    for bigram in listOfBigrams:
        word1 = bigram[0]
        unigramCountsLength = len(unigramCounts)

        listOfProb[bigram] = (bigramCounts.get(bigram) + 1) / (unigramCounts.get(word1) + unigramCountsLength)
        cStar[bigram] = (bigramCounts[bigram] + 1) * unigramCounts[word1] / (unigramCounts[word1] + unigramCountsLength)

    return listOfProb, cStar

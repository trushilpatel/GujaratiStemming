def highestProbabilitySentenceCreator(text, XgramProb, x):
    text = text.split()
    if len(text) < x:
        return

    sentence_finished = False

    while not sentence_finished:

        highestProb = 0
        hpTuple = ()

        for tpl in XgramProb.keys():
            flag = True
            for t in range(x - 1):
                if tpl[t] != text[len(text) - t - 1]:
                    flag = False

            if flag is True:
                if highestProb <= XgramProb[tpl]:
                    highestProb = XgramProb[tpl]
                    hpTuple = tpl

        text.append(hpTuple[len(hpTuple) - 1])

        noneFlag = 0
        for t in range(x):
            if text[t] is None:
                noneFlag += 1

        if noneFlag == x:
            sentence_finished = True

        if len(text) > 8:
            sentence_finished = True

    return ' '.join([t for t in text if t])

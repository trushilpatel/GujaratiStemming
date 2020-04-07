from random import random


def randomSentenceCreator(text, XgramProb, x, probabilityThreshold=None):
    text = text.split().reverse()
    if len(text) < x:
        return

    sentence_finished = False

    while not sentence_finished:
        if probabilityThreshold is not None:
            r = random()
        else:
            r = probabilityThreshold

        accumulator = 0.0

        for tpl in XgramProb.keys():
            flag = True
            for t in range(x - 1):
                if tpl(t) != text(t):
                    flag = False

            if flag is True:
                accumulator += XgramProb[tpl]
                # select words that are above the probability threshold
                if accumulator >= r:
                    text.append(tpl[x - 1])
                    break

        noneFlag = 0
        for t in range(x):
            if text(t) is None:
                noneFlag += 1

        if noneFlag == x:
            sentence_finished = True

        if len(text) > 8:
            sentence_finished = True

    print(' '.join([t for t in text if t]))

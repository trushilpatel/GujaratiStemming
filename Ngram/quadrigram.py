def createXgram(words_data, x):
    """
        words_data must be cleaned and striped with space...
    :param words_data: list of words
    :param x: maxGram number (like for trigram x=3)
    :return: all the grams 1<= gram <= x are returned
    """
    AG = {}  # allGrams
    dataLength = len(words_data)

    for i in range(1, x + 1):
        listOfXgram = 'listOf' + str(i) + 'gram'
        xgramCounts = str(i) + 'gramCounts'

        AG[i] = {
            listOfXgram: [],
            xgramCounts: {}
        }

        print("Creating the {}gram...".format(str(i)))

        for wordIndex in range(len(words_data)):
            if wordIndex  < dataLength - i + 1:
                tpl = tuple(words_data[wordIndex: wordIndex + i])
                AG[i][listOfXgram].append(tpl)

                if tpl in AG[i][xgramCounts]:
                    AG[i][xgramCounts][tpl] += 1
                else:
                    AG[i][xgramCounts][tpl] = 1

    return AG





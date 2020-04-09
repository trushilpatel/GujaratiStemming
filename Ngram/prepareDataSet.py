def prepareDataSet(filePath):
    file = open(filePath, 'rt', encoding='utf-8')
    sent_data = file.readlines()

    words_data = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~‘ '\n'''

    for i in range(len(sent_data)):
        sent_data[i] = sent_data[i].strip(punctuations).split()
        words_data.extend(sent_data[i])
    print("total words :", len(words_data))

    return words_data

def suffix_frequency(file):
    file = open(file, 'rt', encoding='utf-8')
    suffix_list = list(map(lambda w: w.strip(), open(r'D:\MY\GIT\Gujarati-Stemming\corpus\helpingFiles\suffix.txt',
                                                     'rt', encoding='utf-8').readlines()))


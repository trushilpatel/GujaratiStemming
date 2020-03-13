def suffix_word_frequency(file_path):
    file = open(file_path, 'rt', encoding='utf-8')
    suffix_list = list(map(lambda w: w.strip(), open(r'..\..\corpus\helpingFiles\suffix.txt',
                                                     'rt', encoding='utf-8').readlines()))

    words = list(map(lambda w: w.strip(), file.readlines()))
    file.close()

    suffix_frequency_dict = {}

    for suffix in suffix_list:
        suffix_frequency_dict[suffix] = 0

        for word in words:
            if word.endswith(suffix):
                suffix_frequency_dict[suffix] += 1

    write_suffix_frequency_file = open('../../corpus/output/suffix/suffix_frequency.txt', 'wt', encoding='utf-8')
    suffix_frequency_dict = {k: v for k, v in sorted(suffix_frequency_dict.items(), key=lambda item: item[1],
                                                     reverse=True)}
    for key, value in suffix_frequency_dict.items():
        write_suffix_frequency_file.write(key + ' : ' + str(value) + '\n')
    write_suffix_frequency_file.close()


if __name__ == '__main__':
    suffix_word_frequency(r'..\..\corpus\helpingFiles\unique_words.txt')

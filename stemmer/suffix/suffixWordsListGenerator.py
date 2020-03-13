from word_frequency import uniqueWords
from suffixRemovall import SuffixRemoval


def suffix_words_list_generator(data_file, letter_dictionary_json_file):
    """

    :param data_file: dataset from which we want to generate suffix
    :param letter_dictionary_json_file: It's a JSON file created by letterPythonDictionaryCreator.py
    :return: saves the file as suffix.txt
    """

    words = uniqueWords(data_file, want_return_data=True)
    print(len(words))
    word_existence = SuffixRemoval()

    max_word_length = 0
    for word in words:
        if len(word) > max_word_length:
            max_word_length = len(word)

    print("max word length :", max_word_length)

    file = open('../../corpus/output/suffix/wordsAndSuffix.txt', 'wt', encoding='utf-8')
    csvFile = open('../../corpus/output/suffix/wordsAndSuffix.csv', 'wt', encoding='utf-8')
    notValidSuffix = open('../../corpus/output/suffix/notValidSuffix.txt', 'wt', encoding='utf-8')

    file.write('{:<10}'.format('dictWord') + ' {:<40}'.format('word') +
               ' {:<40}'.format('dictionaryWord') + ' {:<40}'.format('suffix') + '\n')
    file.write('-'*130 + '\n')
    csvFile.write('{:<10}'.format('dictWord') + ' {:<40}'.format('word') +
                  ' {:<40}'.format('dictionaryWord') + ' {:<40}'.format('suffix') + '\n')
    csvFile.write('-' * 130 + '\n')

    for word in words:
        if word == '':
            continue

        word_description = word_existence.checkWordExistence(word)

        if word_description is not None:
            # main file
            file.write('{:<10}'.format(str(word_description.get('is_dictionary_word'))) +
                       ' {:<40}'.format(word_description.get('dictionary_word')))

            if word_description.get('valid_suffix') is not None:
                file.write(' {:<40}'.format(str(word_description.get('valid_suffix'))))
            else:
                file.write(' {:<40}'.format(str(False)))

            if word_description.get('suffix') is not None:
                file.write(' {:<40}'.format(word_description.get('suffix')) + '\n')
            else:
                file.write(' {:<40}'.format(False) + '\n')

            # CSV file
            csvFile.write(str(word_description.get('is_dictionary_word')) + ',' +
                          word_description.get('dictionary_word') + ',')

            if word_description.get('valid_suffix') is not None:
                csvFile.write(str(word_description.get('valid_suffix')) + ',')
            else:
                csvFile.write('' + ',')

            if word_description.get('suffix') is not None:
                csvFile.write(word_description.get('suffix') + '\n')
            else:
                csvFile.write('' + '\n')

            # not_valid_suffix file
            # valid suffix is False then write it down to the not_valid_suffix.txt
            if word_description.get('valid_suffix') is False:
                notValidSuffix.write(word_description.get('suffix') + '\n')

    file.close()
    csvFile.close()
    notValidSuffix.close()


if __name__ == '__main__':
    suffix_words_list_generator(r'D:\MY\GIT\Gujarati-Stemming\corpus\combined_wikipedia_dataset.txt',
                                r'D:\MY\GIT\Gujarati-Stemming\corpus\helpingFiles\letters_python_dictionary.json')

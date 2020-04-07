def sortedAndUniqueWords(file_path):
    # DONE
    """
        Checks the file for :-
            ->  making word unique
            ->  truncates space from words
            ->  removes the empty lines
            ->  saves the words in sorted order

    :param file_path: words file path
    :return: sorted and unique words list

    """
    file = open(file_path, 'rt', encoding='utf-8')
    words_list = []

    # striping the words
    for word in file.readlines():
        words_list.append(word.strip())

    file.close()
    print('Total Words : \n' + '-' * 18, '\n\tbefore removing the redundancy :', len(words_list))

    # removing the redundancy of stop words
    words_list = set(words_list)
    print('\tAfter removing the redundancy :', len(words_list))

    print('-' * 50, '\n')

    # sorting the stop word list
    words_list = list(words_list)
    words_list.sort()

    return words_list


if __name__ == "__main__":
    sortedAndUniqueWords("../../corpus/helpingFiles/prefix-list.txt")

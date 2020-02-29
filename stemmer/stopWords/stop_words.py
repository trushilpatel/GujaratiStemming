class StopWords:

    def __init__(self):
        # creating the stop words list
        file = open('stopWords.txt', 'rt', encoding='utf-8')
        self.stop_words_list = []
        for i in file.readlines():
            self.stop_words_list.append(i.strip())

    def sw_file_reformation(self, file_path):
        # DONE
        """
            Checks the file for :-
                ->  making stop word unique
                ->  truncates space from words
                ->  removes the empty lines
                ->  saves the words in sorted order

        :param file_path: stop words file path
        :return: replaces the file with reformed file

        """
        print('Total stop words : \n' + '-' * 18, '\n\tbefore removing the redundancy :', len(self.stop_words_list))

        # removing the redundancy of stop words
        stopWordsList = set(self.stop_words_list)
        print('\tafter removing the redundancy :', len(stopWordsList))
        print('-' * 50, '\n')

        # sorting the stop word list
        stopWordsList = list(stopWordsList)
        stopWordsList.sort()

        # writing to file
        file = open(file_path, 'w', encoding='utf-8')
        for i in stopWordsList:
            file.write(i + '\n')

        file.close()

    def sw_remove(self, sentence_tokenized_words):
        """

        :param sentence_tokenized_words: takes wordTokenized list of sentence (for more info visit tokenizer.py LOL )
            input expamle : [   ['આ', 'બેઠક', 'નીચે', 'જણાવેલ', 'વિભાગોનું', 'પ્રતિનિધિત્વ', 'કરે', 'છે'],
                                ['ગાંધીનગર', 'દક્ષિણ', 'એ', 'પશ્ચિમ', 'ભારતમાં', 'સ્થિત', 'ગુજરાત', 'રાજ્યની', '૧૮૨',
                                 'વિધાનસભા', 'બેઠકોમાંની', 'એક', 'છે']
                            ]
        :return: return list without stop words
        """
        for sentence_words in sentence_tokenized_words:
            temp = []  # stop words occurred in sentence_tokenized_words
            for word in sentence_words:
                if word in self.stop_words_list:
                    temp.append(word)

            # removing stop words
            for i in temp:
                sentence_words.remove(i)

        return sentence_tokenized_words


if __name__ == '__main__':
    s = StopWords()
    s.sw_file_reformation('stopWords.txt')
"""
    print(s.sw_remove([['આ', 'બેઠક', 'નીચે', 'જણાવેલ', 'વિભાગોનું', 'પ્રતિનિધિત્વ', 'કરે', 'છે'],
                       ['ગાંધીનગર', 'દક્ષિણ', 'એ', 'પશ્ચિમ', 'ભારતમાં', 'સ્થિત', 'ગુજરાત', 'રાજ્યની', '૧૮૨',
                        'વિધાનસભા', 'બેઠકોમાંની', 'એક', 'છે']
                       ]))
"""


from sys import getsizeof

class SentenceTokenizerHelper:  # DONE
    def sentenceTokenizerHelper(self, sentence_data):
        """

        :param sentence_data: paragraph of sentences as a input
        :return: list of tokenized sentences
        """
        sentence_data = sentence_data.replace("\n", "")
        tokenized_sentence_list = sentence_data.split(".")

        # removing extra space from starting and ending
        for i in range(len(tokenized_sentence_list)):
            tokenized_sentence_list[i] = tokenized_sentence_list[i].strip()

        # Here asume last element as a "zyx.\n"
        # after removing \n
        # this will be taken as ["zyx.",""]
        # so we must have to remove this "" element which is empty string
        if tokenized_sentence_list[-1] == "":
            tokenized_sentence_list.pop(-1)

        return tokenized_sentence_list


class WordTokenizerHelper:  # DONE
    """
    end_special_characters :
            this are the characters which occurs at the end of any words
    start_special_character :
            this are the characters which occurs at the starting of any words
    """

    def __init__(self):

        self.end_special_characters = (",", ".", "?", ")", "!", '"', "'", "]", "}")
        self.start_special_characters = ("'", '"', "(", "[", "{")

    def wordTokenizerHelper(self, sentence):
        tokenized_words = sentence.split()

        # removing starting special characters
        for word in tokenized_words:
            for ssc in self.start_special_characters:
                if word.startswith(ssc):
                    tokenized_words[tokenized_words.index(word)] = word.replace(ssc, "")

        # removing ending special characters
        for word in tokenized_words:
            for esc in self.end_special_characters:
                if word.endswith(esc):
                    tokenized_words[tokenized_words.index(word)] = word.replace(esc, "")

        return tokenized_words


class Tokenizer:

    def sentenceTokenizer(self, paragraph='', file="", save_as_file=''):  # DONE
        """

        :param paragraph: for paragraph's sentence Tokenizing
        :param file: for given files sentence tokenizing
        :param save_as_file: location to save tokenized sentences
        :return: tokenized sentences either in list or saved in given file location

        Notice : Enter the file name with it's extension
        """

        # Preparing a sentence_data
        if file != '':
            open_file = open(file, 'rt', encoding="utf8")
            sentences_data = open_file.read()
        else:
            sentences_data = paragraph

        # Creating TokenizerHelper object
        tz = SentenceTokenizerHelper()

        if save_as_file == '':
            return tz.sentenceTokenizerHelper(sentences_data)
        else:
            file = open(save_as_file, 'w', encoding="utf8")
            for tokenized_sentences in tz.sentenceTokenizerHelper(sentences_data):
                file.write(tokenized_sentences)
                file.write("\n")
            file.close()

    def wordTokenizer(self, sentences):  # DONE

        """

        :param sentences: takes list of sentences a argument
        :return: word tokenized list is returned

        ;future : special character remover

        """

        wth = WordTokenizerHelper()
        tokenized_words = []
        for sentence in sentences:
            tokenized_words.append(wth.wordTokenizerHelper(sentence))

        return tokenized_words


if __name__ == "__main__":
    t = Tokenizer()

    ans = t.sentenceTokenizer(file="whole_dataset.txt")

    print(len(ans))
    print(getsizeof(ans))
    word_tokenized_sentences = t.wordTokenizer(ans)

    word_tokenized_output = open("word_tokenized_output.txt",'w',encoding = "utf8")

    for tokenized_sentence in word_tokenized_sentences:
        for word in tokenized_sentence:
            word_tokenized_output.write(word)
            word_tokenized_output.write("\t")
        word_tokenized_output.write("\n")

    word_tokenized_output.close()
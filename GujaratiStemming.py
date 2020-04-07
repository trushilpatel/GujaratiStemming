from stopWords.stop_words import *

from dataCleaning.cleanData import *

from utils.file_reformation import *
from utils.uniqueWords import *
from utils.readWriteJsonFile import *
from utils.word_frequency_calculator import *


if __name__ == "__main__":
    file = open(r"D:\MY\GIT\GujaratiStemming\corpus\dataSet\combined.txt", 'rt', encoding='utf-8')
    count = 0
    text = ''
    for i in file.readlines():
        text += i
    print("texting done")
    sentences = text.split('.')
    print(len(sentences))
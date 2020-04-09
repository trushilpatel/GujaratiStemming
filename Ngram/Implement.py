import pickle

from Ngram.prepareDataSet import *
from Ngram.Xgram import *
from Ngram.addOneSmoothingProb import *
from Ngram.calcProb import *
from Ngram.highestProbabilitySentenceCreator import *
from Ngram.sentenceProbability import *
from Ngram.randomSentenceCreator import *
from Ngram.nextWordPro import *  # Yet to implement

if __name__ == '__main__':
    filePath = r"D:\MY\GIT\DataSet\cleanedDataSet\cleaned_wikipediaArticles.txt"
    words_data = prepareDataSet(filePath=filePath)
    xgrams = createXgram(words_data=words_data, x=4)
    xgramsProb = calcAllGramsProb(xgrams)
    xgrams.clear()
    words_data.clear()

    file = open(r"D:\MY\GIT\GujaratiStemming\Ngram\Pickeled\xgramsProb.pickle", 'wb')
    pickle.dump(xgramsProb, file, protocol=2)
    file.close()

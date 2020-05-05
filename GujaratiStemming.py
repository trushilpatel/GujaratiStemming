from dataCleaning.cleanData import *

if __name__ == "__main__":
    file = open(r"D:\MY\GIT\GujaratiStemming\corpus\dataSet\combined.txt", 'rt', encoding='utf-8')
    count = 0
    text = ''
    for i in file.readlines():
        text += i
    print("texting done")
    sentences = text.split('.')
    print(len(sentences))
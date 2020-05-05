from langdetect import detect_langs

"""
    deprecated use PossGujChars's function
"""


def getOnlyGujaratiWord(word):
    try:
        numberOfLanguages = detect_langs(word)
        if len(numberOfLanguages) == 1:
            languageDetails = str(numberOfLanguages[0]).split(":")  # ['gu', '0.9999996586648434']
            if languageDetails[0] == 'gu' and float(languageDetails[1]) >= 0.9999999:
                return word
        return ''
    except:
        return ''


if __name__ == '__main__':
    print(getOnlyGujaratiWord('કેમ'))

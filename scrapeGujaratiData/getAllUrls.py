from bs4 import BeautifulSoup
import urllib.request
import langdetect

def getOnlyGujaratiData(paragraphText):
    if paragraphText is not None:
        numberOfLanguages = langdetect.detect_langs(paragraphText)
        if len(numberOfLanguages) == 1:
            languageDetails = str(numberOfLanguages[0]).split(":")  # ['gu', '0.9999996586648434']
            if languageDetails[0] == 'gu':  # and (float(languageDetails[0]) - 0.999) <= 0.000001):
                return paragraphText


def getAllLinksOfPage(parentUrl):
    try:
        resp = urllib.request.urlopen(parentUrl)
        soup = BeautifulSoup(resp, features='lxml')
        for pTag in soup.find_all('p'):
            try:
                getOnlyGujaratiData(pTag.string)
            except:
                pass

        allLinks = list()
        for link in soup.find_all('a', href=True):
            if link['href'].startswith(parentUrl) and link['href'] not in allLinks:
                ull = link['href']
            elif link['href'].startswith('/') and parentUrl + link['href'] not in allLinks:
                url = parentUrl + link['href'][1:]
            elif not link["href"].startswith('http') and not link['href'].startswith('www') and not link['href'].startswith('mailto'):
                url = parentUrl + link['href']
            allLinks.append(url)

        return allLinks
    except:
        print("Error occurred during requesting to " + parentUrl)
       # print("Check your network connection or your URL")


def getAllUrls(websiteUrl):
    allUrls = list()
    allUrls.append(websiteUrl)

    for url in allUrls:
        print(url)
        try:
            for link in getAllLinksOfPage(url):
                if link not in allUrls:
                    allUrls.append(link)
        except:
            print("Error occurred in getAllUrls \n ")
        #   print("Possibly the None is returned by getAllLinksOfPage function\n")

    return allUrls


if __name__ == '__main__':
    print(getAllUrls('https://eaglenews.in/'))

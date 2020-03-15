# ReadGujarati-https://www.aksharnaad.com/
# Using BeautifulSoup and requests
# install "lxml" library
import requests
from bs4 import BeautifulSoup
import urllib.request
import bs4
import langdetect


def error(parentUrl):
    print("Error occurred during requesting to " + parentUrl)
    print("Check your network connection or your URL")


class ScrappingToolBS:
    def __init__(self, withDescriptions=False):
        self.withDescriptions = withDescriptions
        self.allUrls = list()
        self.allUrlsDict = dict()
        self.urlCount = 0
        self.fileCount = 0
        self.parentUrl = str()
        self.directoryName = str()

    def extractWebsiteData(self):
        websiteUrl = input("(at the end add extra space so you can then enter)\n"
                           "Enter website Name  : ").strip()
        # name for saving the file
        # ----------------------------------
        # only for wikipedia and eaglenews.com
        self.parentUrl = websiteUrl
        # ----------------------------------

        self.directoryName = input("Enter directory name relevant to the Website Name : ")
        print("Started scrapping :", websiteUrl)
        print("-" * 45)

        # this will adds new links into self.allUrls
        self.allUrls.append(websiteUrl)

        for url in self.allUrls:
            try:
                if self.withDescriptions:
                    self.urlCount += 1
                    print(self.urlCount, '.', url)
                self.getAllLinksOfPageAndReturnData(url)
            except:
                error(url)

    def getOnlyGujaratiData(self, paragraphText):
        if paragraphText is not None:
            numberOfLanguages = langdetect.detect_langs(paragraphText)
            if len(numberOfLanguages) == 1:
                languageDetails = str(numberOfLanguages[0]).split(":")  # ['gu', '0.9999996586648434']
                if languageDetails[0] == 'gu':  # and (float(languageDetails[0]) - 0.999) <= 0.000001):
                    return paragraphText
        return ''

    def getAllLinksOfPageAndReturnData(self, parentUrl):
        try:
            resp = urllib.request.urlopen(parentUrl)
            soup = BeautifulSoup(resp, features='lxml')

            # write data to file
            paragraphData = str()
            for pTag in soup.find_all('p'):
                try:
                    paragraphData += self.getOnlyGujaratiData(pTag.text)
                except:
                    pass

            if paragraphData != '':
                self.fileCount += 1
                print("hello")
                file = open('./scrapedDataSet/' + self.directoryName + '/' + str(self.fileCount) + '.txt',
                            'at', encoding='utf-8')
                file.write(paragraphData)
                file.close()
                print("\tWT...")

            for link in soup.find_all('a', href=True):
                url = link['href']
                if url.count('#') > 0:
                    continue
                # """
                if url.startswith(self.parentUrl) and self.allUrlsDict.get(url) is None:
                    self.allUrlsDict[url] = True
                    self.allUrls.append(url)
                """
                if url.startswith(parentUrl) and self.allUrlsDict.get(url) is None:
                    self.allUrls.append(url)
                    self.allUrlsDict[url] = True
                elif url.startswith('/') and self.allUrlsDict.get(parentUrl + url[1:]) is None:
                    self.allUrls.append(parentUrl + url[1:])
                    self.allUrlsDict[parentUrl + url[1:]] = True
                elif not link["href"].startswith('http') and not url.startswith('www') and not link[
                        'href'].startswith('mailto') and self.allUrlsDict.get(parentUrl + url) is None:
                    self.allUrls.append(parentUrl + url)
                    self.allUrlsDict[parentUrl + url] = True
                """
        except:
            print("Error occurred during requesting to " + parentUrl)
        # print("Check your network connection or your URL")


if __name__ == '__main__':
    abc = ScrappingToolBS(withDescriptions=True)
    # Enter Website Name here
    abc.extractWebsiteData()
    print("----Process completed----")

"""
Pro Tips:
    - Always add "/" at the end of URL

________________________________________________________________________________________

Scraped websites:-
----------------------
2) http://sandesh.com/
2) http://www.readgujarati.com/
6) https://kutchuday.in/  saves data in <span> tag
3) http://www.matrulipi.com/  saves data in <div> tag  dont fetch from this it's a wast of time
1) https://www.aksharnaad.com/ 
6) http://www.sanjsamachar.net/
3) https://www.akilanews.com/  most details are in <strong> tag
8) https://eaglenews.in/    it provides direct link for it's url
22) https://www.gujaratimidday.com/
20) https://www.aajkaaldaily.com/
18) http://www.nobat.com/ <span>
17) http://www.gujarattoday.in/
15) https://gujarattimesusa.com/ <spam>
14) https://www.iamgujarat.com/
16) https://kutchuday.in/
5) https://gu.wikipedia.org/  smartly do it again it contains lots of information
    this file scrapped in example.txt
    to scrap wikipedia use this link as permanent parent link




_______________________________________________________________________________________

Up Next:-
-----------------------
4) https://gujarati.pratilipi.com/
   https://www.gujaratsamachar.com/
    don't scrape these websites they are smarter that's why they are using 
    angular
4) https://www.navgujaratsamay.com/
5) http://www.bombaysamachar.com/
13) https://gujarati.oneindia.com/
23) 


19) http://sardargurjari.com/   <span>  not scrappable
"""

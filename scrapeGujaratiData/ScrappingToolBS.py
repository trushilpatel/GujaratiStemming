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
        self.file = None
        self.allUrls = list()

    def __del__(self):
        # saving the file
        self.file.close()

    def extractWebsiteData(self):
        websiteUrl = input("(at the end add extra space so you can then enter)\n"
                           "Enter website Name  : ").strip()
        # name for saving the file
        fileName = input("Enter File name relevant to the Website Name : ")
        self.file = open("../scrapeGujaratiData/scrapedDataSet/" + fileName + ".txt", 'at', encoding='utf-8')
        print("Started scrapping :", websiteUrl)
        print("-" * 45)

        # this will adds new links into self.allUrls
        self.getAllLinksOfPageAndSaveDataToFile(websiteUrl)

        for url in self.allUrls:
            try:
                if self.withDescriptions:
                    print(self.allUrls.index(url), '.', url)
                self.getAllLinksOfPageAndSaveDataToFile(url)
            except:
                error(url)

    def getOnlyGujaratiData(self, paragraphText):
        if paragraphText is not None:
            numberOfLanguages = langdetect.detect_langs(paragraphText)
            if len(numberOfLanguages) == 1:
                languageDetails = str(numberOfLanguages[0]).split(":")  # ['gu', '0.9999996586648434']
                if languageDetails[0] == 'gu':  # and (float(languageDetails[0]) - 0.999) <= 0.000001):
                    self.file.write(paragraphText)

    def getAllLinksOfPageAndSaveDataToFile(self, parentUrl):
        try:
            resp = urllib.request.urlopen(parentUrl)
            soup = BeautifulSoup(resp, features='lxml')

            # write data to file
            for pTag in soup.find_all('p'):
                try:
                    self.getOnlyGujaratiData(pTag.string)
                except:
                    pass

            for link in soup.find_all('a', href=True):
                if link['href'].startswith(parentUrl) and link['href'] not in self.allUrls:
                    self.allUrls.append(link['href'])
                elif link['href'].startswith('/') and parentUrl + link['href'] not in self.allUrls:
                    self.allUrls.append(parentUrl + link['href'][1:])
                elif not link["href"].startswith('http') and not link['href'].startswith('www') and not link[
                        'href'].startswith('mailto'):
                    self.allUrls.append(parentUrl + link['href'])

        except:
            print("Error occurred during requesting to " + parentUrl)
        # print("Check your network connection or your URL")


if __name__ == '__main__':
    abc = ScrappingToolBS()
    # Enter Website Name here
    abc.extractWebsiteData()
    print("----Process completed----")

"""
Pro Tips:
    - Always add "/" at the end of URL

________________________________________________________________________________________

Scraped websites:-
----------------------
1) https://www.aksharnaad.com/
2) http://www.readgujarati.com/  remaining 
3) http://www.matrulipi.com/
4) https://gujarati.pratilipi.com/
   https://www.gujaratsamachar.com/
    don't scrape these websites they are smarter that's why they are using 
    angular
5)
_______________________________________________________________________________________

Up Next:-
-----------------------
1) https://gu.wikipedia.org/
2) http://sandesh.com/
3) https://www.akilanews.com/
4) https://www.navgujaratsamay.com/
5) http://www.bombaysamachar.com/
6) http://www.sanjsamachar.net/
7) https://rakhewaldaily.com/
8) https://eaglenews.in/
9) http://www.dhabkar.in/
10) http://www.aaspassindia.com/
11) http://www.loksansar.in/
12) https://gujarati.webdunia.com/
13) https://gujarati.oneindia.com/
14) https://www.iamgujarat.com/
15) https://gujarattimesusa.com/
16) https://kutchuday.in/
17) http://www.gujarattoday.in/
18) http://www.nobat.com/
19) http://sardargurjari.com/
20) https://www.aajkaaldaily.com/
21) https://www.kutchmitradaily.com/
22) https://www.gujaratimidday.com/
23) 
"""

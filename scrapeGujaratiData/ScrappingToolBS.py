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


def getAllLinksOfPage(parentUrl):
    try:
        resp = urllib.request.urlopen(parentUrl)
    except:
        error(parentUrl)
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features='lxml')
    allLinks = list()

    for link in soup.find_all('a', href=True):
        if link['href'].startswith(parentUrl):
            if link['href'] not in allLinks:
                allLinks.append(link['href'])
        if link['href'].startswith('/'):
            if link['href'] not in allLinks:
                allLinks.append(parentUrl + link['href'])
    return allLinks


def getAllUrls(websiteUrl):
    allUrls = list()
    allUrls.append(websiteUrl)

    for url in allUrls:
        print(url)
        for link in getAllLinksOfPage(url):
            if link not in allUrls:
                allUrls.append(link)

    return allUrls


class ScrappingToolBS:
    def __init__(self):
        self.file = None
        self.allUrls = list()

    def __del__(self):
        # saving the file
        self.save_file.close()

    def extractWebsiteData(self):
        websiteUrl = input("(at the end add extra space so you can then enter)\n"
                           "Enter website Name  : ").strip()
        # name for saving the file
        fileName = input("Enter File name relevant to the Website Name : ")
        self.file = open("../scrapeGujaratiData/scrapedDataSet/" + fileName + ".txt", 'wt', encoding='utf-8')
        print("Started scrapping :", websiteUrl)
        print("-" * 30)
        print("Getting all the urls...")
        self.allUrls.extend(getAllUrls(websiteUrl))

        for url in self.allUrls:
            try:
                websiteData = requests.get(url)
                self.extractParagraphTagData(websiteData)
            except:
                error(url)

    def extractParagraphTagData(self, websiteData):
        # 'lxml' is used instead of 'html.parser' bcs of speed issue
        soup = bs4.BeautifulSoup(websiteData.text, 'lxml')
        # if most of the data contains in p tag so find_all('p') or depend upon website
        for i in soup.find_all('p'):
            try:
                self.getGujaratiData(i.string)
            except:
                pass
        return

    def getGujaratiData(self, paragraphText):
        if paragraphText is not None:
            numberOfLanguages = langdetect.detect_langs(paragraphText)
            if len(numberOfLanguages) == 1:
                languageDetails = str(numberOfLanguages[0]).split(":")  # ['gu', '0.9999996586648434']
                if languageDetails[0] == 'gu':  # and (float(languageDetails[0]) - 0.999) <= 0.000001):
                    self.save_file.write(paragraphText)
                return
            return


if __name__ == '__main__':
    abc = ScrappingToolBS()
    # Enter Website Name here
    abc.extractWebsiteData()
    print("----Process completed----")

"""
Scraped websites:-
----------------------
1) https://www.aksharnaad.com
2) http://www.readgujarati.com/
3) http://www.matrulipi.com/

_______________________________________________________________________________________

Up Next:-
-----------------------
1)
"""

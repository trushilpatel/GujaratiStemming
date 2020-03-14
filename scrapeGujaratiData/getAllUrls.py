from bs4 import BeautifulSoup
import urllib.request

"""
parentUrl = 'https://www.google.com'
resp = urllib.request.urlopen(parentUrl)
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features='lxml')
allLinks = list()

for link in soup.find_all('a', href=True):
    if link['href'].startswith(parentUrl) :
        if link['href'] not in allLinks:
            allLinks.append(link['href'])
    if link['href'].startswith('/'):
        if link['href'] not in allLinks:
            allLinks.append(parentUrl + link['href'])
print(allLinks)
"""


def getAllLinksOfPage(parentUrl):
    try:
        resp = urllib.request.urlopen(parentUrl)
    except:
        print("Error occurred during requesting to " + parentUrl)
        print("Check your network connection or your URL")
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


if __name__ == '__main__':
    getAllUrls('http://www.google.com')

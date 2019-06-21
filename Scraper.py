#import libraries
import urllib3
import certifi
import random
from bs4 import BeautifulSoup

websiteURL = 'https://www.youtube.com/'

def connectToURL(url):
    # Validate the certificate for a secure connection
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    # The html of the page is in the soup variable
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features="html.parser")
    return soup

def extractVideoElements(soup):
    allATags = soup.find_all('a', href=True, title=True)
    videoTags = []
    for aTag in allATags:
        if aTag['href'][:6] == "/watch":
            videoTags.append(aTag)

    for videoTag in videoTags:
        for tag in videoTag.find_all():
            if len(list(tag.parents)) > 0:
                tag.extract()

    return videoTags

def getLinksFromElements(videoElements):
    videoLinks = []
    for i in range(0, len(videoElements)):
        videoLinks.append(videoElements[i]['href'])
    return videoLinks

def getTitlesFromElements(videoElements):
    videoTitles = []
    for i in range(0, len(videoElements)):
        videoTitles.append(videoElements[i]['title'])
    return videoTitles

def surfRecommended(numIterations):
    videoElements = extractVideoElements(connectToURL(websiteURL))
    videoTitles = getTitlesFromElements(videoElements)
    videoLinks = getLinksFromElements(videoElements)

    for i in range(1, numIterations):
        nextPick = random.randint(0, len(videoLinks) - 1)
        selectedVideoLink = videoLinks[nextPick]
        selectedVideoTitles = videoTitles[nextPick]
        print("Video Choice: ", nextPick, " Title: ", selectedVideoTitles, " Extension: ", selectedVideoLink)
        videoElements = extractVideoElements(connectToURL(websiteURL + selectedVideoLink))
        videoTitles = getTitlesFromElements(videoElements)
        videoLinks = getLinksFromElements(videoElements)





surfRecommended(1000)



import time
import os
from urllib.request import urlopen, Request
from urllib.error import URLError
from bs4 import BeautifulSoup

def getURL(url):
    Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    # to perform a GET request and load the 
    # content of the website and store it in a var, raise error if url is incorrect
    try:
        response = urlopen(url).read()
        return response
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        

def getElement(response):
    # create a beautiful soup object to parse html
    soup = BeautifulSoup(response, 'html.parser')
    # select the span element we are looking for on rightmove's website
    content = soup.find('span', {"class": "searchHeader-resultCount"})
    # get the text value of the numOfProperties
    numOfProperties = content.get_text()
    return numOfProperties


print("running...")
url = input("Please enter the URL of your rightmove.co.uk search: ")

while True:
    response = getURL(url)
    numOfPropertiesBefore = getElement(response)
    print(numOfPropertiesBefore)
    
    #wait for 2 mins to check if the number of properties has changed
    time.sleep(120)

    response = getURL(url)
    numOfPropertiesAfter = getElement(response)
    print(numOfPropertiesAfter)

    if (numOfPropertiesBefore == numOfPropertiesAfter):
        continue

    else:
        # notify
        for x in range(3):
            os.system('say new property alert')

        
        # wait for 30 seconds
        time.sleep(30)
        continue



    
    
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package
import requests

'''
    URL = 'https://en.wikipedia.org/wiki/List_of_game_engines'
    content = requests.get(URL)
    soup = BeautifulSoup(content.text, 'html.parser')
    row = soup.find('tr') # Extract and return first occurrence of tr
    print(row)            # Print row with HTML formatting
    print("=========Text Result==========")
    print(row.get_text()) # Print row as text

'''


site = input("Enter your URL: ")
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, features="html.parser")
images = soup.findAll("img", {"class": "my-3"})
basePath = 'D:/downloads/92/'
count = 1
for image in images:
    url = image['src']
    path = basePath + 'AOT_' + str(count) + '.jpg'
    urlretrieve(url, path)
    print("DONE for : " + str(count))
    count = count + 1

print("=========DONE==========")

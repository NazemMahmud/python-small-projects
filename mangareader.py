from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
import json

BASE_PATH = 'D:' + os.sep + 'downloads' + os.sep # it is changeable
HTTPS = 'https:'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}


def create_folder(path):
    folder_path = BASE_PATH + path
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def download_images(urls, file_base_name, chapter, path):
    for idx, url in enumerate(urls):
        req = Request(url, headers=HEADERS)
        response = urlopen(req)
        download_path = path + os.sep + file_base_name + '_' + chapter + '_' + str(idx+1) + '.jpg'
        print(f"downloading: {file_base_name}_{chapter}_{str(idx+1)}.jpg")
        f = open(download_path, 'wb')
        f.write(response.read())
        f.close()


def main():
    site = input("Enter your URL: ")
    req = Request(site, headers=HEADERS)
    page = urlopen(req)
    soup = BeautifulSoup(page, features="html.parser")

    script_data = soup.findAll("script")[1].string
    data = script_data.replace('document["mj"]=', '')
    data_dict = json.loads(data)
    manga_name = data_dict["mn"].title()
    chapter = data_dict["cn"]
    path = manga_name + os.sep + chapter
    folder_path = create_folder(path)

    page_links = []
    for item in data_dict['im']:
        page_links.append(HTTPS + item['u'])

    name = manga_name.split()
    file_name = ''
    for idx, item in enumerate(name):
        file_name = file_name + item
        if idx < (len(name) - 1):
            file_name = file_name + '_'

    download_images(page_links, file_name, chapter, folder_path)
    print("=========DONE==========")


main()

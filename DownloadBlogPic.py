#! python3

# simple program to download porn images

import requests
import os
import bs4
import re
import tkinter.filedialog
from tkinter import *
from pathlib import *

from requests.models import MissingSchema

url = str(input("Copy URL:\n"))  # desired url

# Download the page.
print('Downloading page %s...' % url)
res = requests.get(url, headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pt-BR;q=0.8,pt;q=0.7",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.google.com.br",
    "User-Agent": "Chrome/89.0.4389.128"})
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find the URL of the blog.
postElem = soup.select("#single img")
if postElem == []:
    print('Could not find article image.')
else:
    # make a directory to save pictures
    Tk().withdraw()
    homedir = tkinter.filedialog.askdirectory(mustexist=True)
    Tk().destroy()
    if not homedir:
        print("Select a directory")
    else:
        #title = soup.title.string.replace(">", "")
        title = re.sub('[!@#$>\\<|]', "", soup.title.string)
        newdir = homedir + "\\" + title
        # make a directory if it doesn't exist
        os.makedirs(newdir, exist_ok=True)

        for element in range(len(postElem)):
            try:
                # Download the image.
                imageUrl = postElem[element].get('data-src')
                res = requests.get(imageUrl)
                res.raise_for_status()
                print('Downloading image %s...' % (imageUrl))
                # Save the image to the new folder.
                imageFile = open(os.path.join(
                    newdir, os.path.basename(imageUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except MissingSchema:
                print("failed to find URL")

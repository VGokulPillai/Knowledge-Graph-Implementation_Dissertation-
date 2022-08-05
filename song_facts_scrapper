import json
import urllib.request 
import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus, quote
from urllib.error import HTTPError, URLError
from random import randint
import requests
import re
from time import sleep
import ssl
import csv
import datetime
import bs4
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession

#any URLS from songfacts works

my_url = "https://www.songfacts.com/songs/the-beatles"
#my _url =[]
#ing_main = []
from urllib.parse import urlparse
domain = urlparse(my_url).netloc



_pages_read={}
from requests_html import HTMLSession
s = HTMLSession()

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


print(my_url)


resp= requests.get(my_url,headers=hdr)
soup = soup(resp.content)

new_links = set()
unwanted_links = set()
useful_links = set()
flag=0

for link in soup.find_all("a", href=True):
    if my_url in link["href"]:
        new_links.add(link["href"])
    if link["href"].startswith("https://"):#add the http which is the secured websites 
        unwanted_links.add(link["href"])
    if(link["href"].startswith("/")):
        x=link["href"][1:]
        abss = my_url + x
        flag=1
    absolute_url = my_url + link["href"]
    if(flag==1):
        new_links.add(abss)
    else:
        new_links.add(absolute_url)
        
print(new_links)

file = open(domain,"w")
for url in new_links:
    try:
        url = url.replace(" ","")
        print(url)
        html = urllib.request.urlopen(url) 
    except HTTPError as hp:
        print(hp)
        continue
    htmlParse = BeautifulSoup(html, 'html.parser')
    for para in htmlParse.find_all({"p","span","h3"}):
        x=para.get_text()
        file.write(x)
file.close()

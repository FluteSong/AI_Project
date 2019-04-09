import requests
from bs4 import BeautifulSoup
import re
import nltk
import matplotlib.pyplot as plt
import time
import random
import csv


web=input("input the webname:")

if web =="seekingalpha":
    n=input("input the num of pages:")


    word=[]

    for i in range(n):
        url = "https://seekingalpha.com/latest-articles?page="+str(i)
        headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"]


        randdom_header = random.choice(headers)
        headers = {'User-Agent': randdom_header}
        page = requests.get(url,headers = headers)
        time.sleep(8)
        #print(randdom_header)
        print(page)
        soup = BeautifulSoup(page.text, "html.parser")

        title=soup.find_all('a',{'class':"a-title"})

        for i in title:
            print(i.get_text())

if web =="wallstreet":
    url = "https://wallstreetcn.com/live/us-stock"
    hdr = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) Apple WebKit / 537.36(KHTML, like Gecko) Chrome / 72.0.3626.121 Safari / 537.36'}
    req = urllib.request.Request(url=url, headers=hdr)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # html.read().decode('utf-8')

    soup = BeautifulSoup(html, "lxml")

    # print(soup.find_all("a",{"target": "_blank"}))
    # soup.get_text()
    title = soup.find_all('p')

    for i in title:
        print(i.get_text())




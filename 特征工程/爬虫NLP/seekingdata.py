import requests
from bs4 import BeautifulSoup
import re
import nltk
import matplotlib.pyplot as plt
import time
import random
import csv


word=[]




for i in range(100):
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

    # title=soup.find_all('a',{'class':"a-title"})

    symbol=soup.find_all('a',{'href':re.compile('/symbol/*')})


    #print(symbol)
    #print(title)
    # for i in title:
    #     print(i.get_text())


    for s in symbol:
        #print(i.get_text())
        word.append(s.get_text())



freq = nltk.FreqDist(word)
out = open('data100.csv','a', newline='')
csv_write = csv.writer(out,dialect='excel')
for key,val in freq.items():
    #print (str(key) + ':' + str(val))
    data=[key,val]
    csv_write.writerow(data)
freq.plot(50, cumulative=False)
plt.show()
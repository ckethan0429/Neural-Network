from bs4 import BeautifulSoup 
import urllib.request as req
from urllib.parse import urljoin

url = "https://sports.news.naver.com/mlb/news/read.nhn?oid=460&aid=0000000995&rc=N" 
res = req.urlopen(url) 
soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("#newsEndContents > p:nth-child(1) > img")
for img in img_list:
    src = img.attrs['src'] 
    print(urljoin(url,src))
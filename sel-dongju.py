from bs4 import BeautifulSoup 
import urllib.request as req
url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC" 
res = req.urlopen(url) 
soup = BeautifulSoup(res, "html.parser")

a_list1 = soup.select("#mw-content-text > div > ul:nth-child(6) > li >b > a")

a_list2 = soup.select("#mw-content-text > div > ul:nth-child(6) > li > ul > li:nth-child(1) > a")
for a in a_list1: 
    name = a.string 
    print("-", name)

for a in a_list2: 
    name = a.string 
    print("-", name)

    #mw-content-text > div > ul:nth-child(6) > li > b > a
    #mw-content-text > div > ul:nth-child(6) > li > b > a
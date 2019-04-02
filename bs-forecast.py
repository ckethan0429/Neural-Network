from bs4 import BeautifulSoup   
import urllib.request as req
url ="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

#urlopen()
res = req.urlopen(url)

#BeautifulSoup으로 분석
soup = BeautifulSoup(res, "html.parser")

#원하는 데이터 추출
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)
print('------------')
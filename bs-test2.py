from bs4 import BeautifulSoup

#분석하고 싶은 HTML
html ="""
<html><body>
 <h1>스크레핑이란?</h1>
 <p>웹페이지를 분석하는 것</p>
 <p>원하는 부분을 출력하는 것</p>
</body></html>
"""

#HTML 분석하기
soup = BeautifulSoup(html,'html.parser')

#원하는 부분 추출하기
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

#요소 글자출력
print("h1 = "+ h1.string)
print("p = "+ p1.string)
print("p = "+ p2.string)
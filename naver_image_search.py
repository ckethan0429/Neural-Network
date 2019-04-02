import requests
import urllib.parse as parse
import urllib.request as request
import json
import os


# 네이버 검색 클라이언트 ID, Secret ID 헤더 설정
headers = {
"X-Naver-Client-Id" : "dlsSwlP25A0lM6IdPiz3",
"X-Naver-Client-Secret" : "JZZ87AuLXY"
}
# 검색 url
url = "https://openapi.naver.com/v1/search/image"

count =1
for i in range(0,3,1):
    
    # 검색 파라미터
    params = {
    "query" : "고양이",
    "start" : count,
    "display" : 100
    }

    res = requests.get(url, headers=headers, params=params) 
    print(res.status_code) # 응답 코드 
    list = json.loads(res.text) # json 문자열 파싱 #파이썬 비슷한 자료구조인 딕셔너리
   
    for ix, item in enumerate(list["items"]): #index 추가하기위해 enumerate
        title = item["title"] # 이미지 타이틀  
        link = item["link"] # 이미지 링크 
        info = parse.urlparse(link) # 이미지 링크 url 분석 
        fileName = os.path.split(info.path)[1] # 이미지 파일명 추출 
        print(ix+count, title, fileName) 

        # link를 이용하여 파일 다운로드 진행
        path = "c:/temp/download/{}".format(fileName)
        request.urlretrieve(link, path)
        
    count += 100   
    
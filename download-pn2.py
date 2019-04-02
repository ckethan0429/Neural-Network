import urllib.request

#url과 저장 경로 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png" 

#다운로드
mem = urllib.request.urlopen(url).read()

#파일저장
with open(savename, mode="wb") as f:
    f.write(mem)
    print('저장')